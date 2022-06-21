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


import random
import re

from typing import List, Union
from src.operators.generic import Operator
from src.gen.gen_configuration import (
    get_constant,
    get_variable,
    get_eligible_operator,
    get_root,
    get_operator_class,
    get_arities,
    get_operator_parameters
)
from src.visitors.initialization_visitor import InitializationVisitor

constant_name_pattern = re.compile(r"^c\d+$")


# Ordered Tree Encoding:
# an n-tuple for a tree of n nodes:
#   t = (t1, t2, ..., ti,..., tn)
# ti is the i-th node of the tree t.
# A parent node implies ti > 0, while a leaf node implies ti = 0.
# The nodes are visited in preorder (depth-first left to right) to determine the order of the tree.
# The last node of the tree is thus tn, so tn = 0
# and ti is in [0, n - 1].
# Note: we use a list for simplicity/efficiency.
def _generate_arity_tree(size: int, arities: List[int], min_leaves: int):
    """
    Generates a list of integers representing a tree containing n
    nodes. The first node is already set to root.
    """
    tree = []
    rem_leaves = min_leaves
    min_op_arity = min(arities)

    while len(tree) < size:
        max_arity = size - sum(tree) - 1

        if 0 < max_arity < min_op_arity:
            discrepancy = min_op_arity - max_arity
            print(
                f"Cannot match tree size {size} exactly, increasing to {size + discrepancy}...")
            size += discrepancy
            max_arity += discrepancy

        rem_operators = size - len(tree) - rem_leaves
        max_sub_leaves = (rem_operators - 1) * (max(arities) - 1) + 1
        min_arity = rem_leaves - (sum(tree) - len(tree)) - max_sub_leaves + 1

        branching_choices = [
            n for n in arities if (min_arity <= n <= max_arity)]

        if not (sum(tree) == len(tree) and max_arity > 0):
            branching_choices.extend([0, 0])  # two different leaf operators

        arity = random.choice(branching_choices)
        tree.append(arity)

        if arity == 0:
            rem_leaves -= 1

    return tree


def _generate_operator_tree(theory, arity_tree, num_variables) -> Operator:
    num_leaves = len([n for n in arity_tree if n == 0])
    num_constants = num_leaves - num_variables

    if num_leaves < num_variables:
        raise ValueError(
            "Not enough leaves to accommodate requested number of variables.")

    leaves = [False] * num_constants + [True] * num_variables
    random.shuffle(leaves)

    def recursive_generation(idx, operator_type):
        n = arity_tree[idx]
        idx += 1
        params = []

        if n == 0:
            nonlocal num_leaves
            num_leaves -= 1
            is_variable = leaves[num_leaves]

            if is_variable:
                op_name = get_variable(operator_type)
            else:
                op_name = get_constant(operator_type)
        else:
            op_name = get_eligible_operator(operator_type, n)

            for input_type in get_operator_parameters(operator_type, op_name):
                param, idx = recursive_generation(idx, input_type)
                params.append(param)

        return get_operator_class(operator_type, op_name)(*params), idx

    operator_tree, _ = recursive_generation(0, theory)
    root_name = get_root(theory)

    output_var = get_operator_class(theory, get_variable(theory))()
    root = get_operator_class(theory, root_name)(output_var, operator_tree)

    return root


def generate_tree(theory: str, size: int, in_variables: Union[int, List[str]] = 2, out_variable: str = 'z') -> Operator:
    if isinstance(in_variables, int):
        in_variables = [f'x{i+1}' for i in range(in_variables)]
    else:
        # Check that names do not clash with constant generated names.
        for v in in_variables:
            if constant_name_pattern.match(v) is not None:
                ValueError(
                    "The list of variables should not contain a name matching the constant name pattern: c[0-9]")

    num_variables = len(in_variables)
    arities = get_arities(theory)

    if (size - num_variables) * (max(arities) - 1) + 1 < num_variables:
        raise ValueError("Tree size too small to accommodate all variables")

    tree = _generate_arity_tree(size, arities, num_variables)
    tree = _generate_operator_tree(theory, tree, num_variables)

    init_visitor = InitializationVisitor(in_variables, out_variable)
    tree.accept(init_visitor)
    return tree


def validate(tree: List[int]) -> bool:
    """
    Returns true if a tree of n nodes respect the property:
        sum from i to n of ti = n - 1 
    """
    return sum(tree) == len(tree) - 1 and tree[len(tree) - 1] == 0
