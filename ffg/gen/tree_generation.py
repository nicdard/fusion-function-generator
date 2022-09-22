# MIT License
#
# Copyright (c) 2022 Nicola Dardanis, Lucas Weitzendorf
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import math
import random
import re

from typing import List, Union, Tuple, Any
from ffg.operators.generic import Operator
from ffg.gen.gen_configuration import (
    get_constant,
    get_variable,
    get_eligible_operators,
    get_root,
    get_operator_class,
    get_arities,
    get_operator_parameters
)
from ffg.visitors.initialization_visitor import InitializationVisitor

constant_name_pattern = re.compile(r"^c\d+$")


def generate_tree(theory: str, size: int, in_variables: Union[int, List[str]], out_variable: str) -> Tuple[Any, int]:
    if isinstance(in_variables, int):
        in_variables = [f'x{i+1}' for i in range(in_variables)]
    else:
        # Check that names do not clash with constant generated names.
        for v in in_variables:
            if constant_name_pattern.match(v):
                ValueError("The list of variables should not "
                           "contain a name matching the constant name pattern: c[0-9]")

    def get_leaf_bounds(tree_type, tree_size):
        available_arities = get_arities(tree_type)
        min_op_arity = min(available_arities)
        max_op_arity = max(available_arities)

        def get_bound(arity):
            return (tree_size * (arity - 1) + 1) / arity

        low = math.ceil(get_bound(min_op_arity))
        high = math.floor(get_bound(max_op_arity))
        return low, high

    tree_size = 2  # root and output var
    gen_size = size - tree_size
    gen_num_var = len(in_variables)
    min_leaf, max_leaf = get_leaf_bounds(theory, gen_size)

    if min_leaf > max_leaf:
        gen_size += 1  # maybe print a message here
        min_leaf, max_leaf = get_leaf_bounds(theory, gen_size)

    if max_leaf < gen_num_var:
        raise ValueError(
            f"Tree of size {size} cannot accommodate {gen_num_var} variables")

    gen_num_leaf = random.randint(max(gen_num_var, min_leaf), max_leaf)
    gen_num_internal = gen_size - gen_num_leaf
    gen_num_const = gen_num_leaf - gen_num_var

    leaf_idx = 0
    leaf_type = [False] * gen_num_const + [True] * gen_num_var
    random.shuffle(leaf_type)

    def is_var():
        nonlocal leaf_idx
        leaf_idx += 1
        return leaf_type[leaf_idx-1]

    def generate_subtree(op_type, num_internal, num_leaf):
        available_arities = get_arities(op_type)

        def get_closest_feasible_num_internal():
            new_num_internal = 0
            target = new_num_internal + num_leaf - 1

            lowest_dev = float('inf')
            best_num_internal = 0
            possible_sums = {0}

            while True:
                dev = abs(new_num_internal - num_internal)
                if dev <= lowest_dev:
                    if target in possible_sums:
                        lowest_dev = dev
                        best_num_internal = new_num_internal
                elif new_num_internal >= num_internal:
                    break

                new_sums = set()
                for prev_sum in possible_sums:
                    for arity in available_arities:
                        new_sums.add(prev_sum + arity)

                possible_sums = new_sums
                new_num_internal += 1
                target = new_num_internal + num_leaf - 1

            return best_num_internal

        num_internal = get_closest_feasible_num_internal()

        if num_internal >= 1:
            max_sub_leaf = (num_internal - 1) * \
                (max(available_arities) - 1) + 1
            min_arity = num_leaf - max_sub_leaf + 1
            min_sub_leaf = (num_internal - 1) * \
                (min(available_arities) - 1) + 1
            max_arity = num_leaf - min_sub_leaf + 1
            op_choices = get_eligible_operators(op_type, min_arity, max_arity)
            op_name = random.choice(op_choices)
        else:
            op_func = get_variable if is_var() else get_constant
            op_name = op_func(op_type)

        parameters = get_operator_parameters(op_type, op_name)
        op_arity = len(parameters)

        children = []
        rem_internal = num_internal - 1  # not sure if max is necessary here
        rem_leaf = num_leaf

        for idx, input_type in enumerate(parameters):
            if idx < op_arity - 1:
                # guarantee at least one leaf per subtree
                rem_children = op_arity - (idx + 1)
                child_leaf = random.randint(1, rem_leaf - rem_children)
                rem_leaf -= child_leaf

                def get_bound(num_leaves, arity):
                    return (num_leaves - 1) / (arity - 1) if arity > 1 else 1e6

                child_available_arities = get_arities(input_type)
                min_op_arity = min(child_available_arities)
                max_op_arity = max(child_available_arities)

                min_internal_to_cover = math.ceil(
                    get_bound(rem_leaf, max_op_arity))
                child_internal_high = math.floor(
                    get_bound(child_leaf, min_op_arity))
                child_internal_high = min(
                    child_internal_high, rem_internal - min_internal_to_cover)

                child_internal_low = math.ceil(
                    get_bound(child_leaf, max_op_arity))
                child_internal_low = min(
                    child_internal_low, child_internal_high)
                child_internal = random.randint(
                    child_internal_low, child_internal_high)
                rem_internal -= child_internal
            else:
                child_internal = rem_internal
                child_leaf = rem_leaf

            child = generate_subtree(input_type, child_internal, child_leaf)
            children.append(child)

        nonlocal tree_size
        tree_size += 1

        return get_operator_class(op_type, op_name)(*children)

    operator_tree = generate_subtree(theory, gen_num_internal, gen_num_leaf)
    output_var = get_operator_class(theory, get_variable(theory))()

    tree = get_operator_class(theory, get_root(theory))(
        output_var, operator_tree)
    tree.accept(InitializationVisitor(in_variables, out_variable))

    return tree, tree_size
