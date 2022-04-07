from math import ceil
from typing import List, Set, Union
from operators import gen_configuration
# ==================================================================
# necessary for operators to be in global namespace for generation
from operators.gen.boolean_theory import *
from operators.gen.integer_theory import *
from operators.gen.real_theory import *
# ==================================================================


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
    max_op_arity = max(arities)

    def expected_nodes():
        return sum(tree) + 1

    def missing_nodes():
        return expected_nodes() - len(tree)
    
    while len(tree) < size:
        remaining = size - expected_nodes()

        if remaining in range(1, min_op_arity):
            discrepancy = min_op_arity - remaining
            print(f"Cannot match tree size {size} exactly, increasing to {size + discrepancy}...")
            size += discrepancy
            remaining += discrepancy

        rem_operators = size - len(tree) - rem_leaves
        max_sub_leaves = (rem_operators - 1) * (max_op_arity - 1) + 1
        min_arity = max(1, rem_leaves - missing_nodes() - max_sub_leaves + 2)

        branching_choices = [n for n in arities if n in range(min_arity, remaining+1)]
        
        if not (missing_nodes() == 1 and remaining > 0):
            branching_choices.extend([0, 0])  # two different leaf operators

        arity = random.choice(branching_choices)
        tree.append(arity)

        if arity == 0:
            rem_leaves -= 1

    return tree


def get_operator_class(name):
    return globals()[name]


def _generate_operator_tree(theory, arity_tree, in_variables, out_variable):
    num_leaves = len([n for n in arity_tree if n == 0])
    num_variables = len(in_variables)
    num_constants = num_leaves - num_variables

    if num_leaves < num_variables:
        raise ValueError("Not enough leaves to accommodate requested number of variables.")

    leaves = [False] * num_constants + [True] * num_variables
    random.shuffle(leaves)

    def recursive_generation(idx, operator_type):
        nonlocal num_leaves, num_variables
        n = arity_tree[idx]
        idx += 1
        params = []

        if n == 0:
            num_leaves -= 1
            is_variable = leaves[num_leaves]

            if is_variable:
                op_name = gen_configuration.get_variable(operator_type)
                num_variables -= 1
                params.append(in_variables[num_variables])
            else:
                op_name = gen_configuration.get_constant(operator_type)
        else:
            op_name = gen_configuration.get_eligible_operator(operator_type, n)

            for _ in range(n):
                param, idx = recursive_generation(idx, operator_type)
                params.append(param)

        return get_operator_class(op_name)(*params), idx

    operator_tree, _ = recursive_generation(0, theory)
    root_name = gen_configuration.get_root(theory)

    output_var = get_operator_class(gen_configuration.get_variable(theory))(out_variable)
    root = get_operator_class(root_name)(output_var, operator_tree)

    return root


def generate_tree(theory: str, size: int, in_variables: Union[int, List[str]] = 2, out_variable: str = 'z'):
    if isinstance(in_variables, int):
        in_variables = [f'x{i+1}' for i in range(in_variables)]

    num_variables = len(in_variables)
    arities = gen_configuration.get_arities(theory)

    if (size - num_variables) * (max(arities) - 1) + 1 < num_variables:
        raise ValueError("Tree size too small to accommodate all variables")

    tree = _generate_arity_tree(size, arities, num_variables)
    return _generate_operator_tree(theory, tree, in_variables, out_variable)


def validate(tree: List[int]) -> bool:
    """
    Returns true if a tree of n nodes respect the property:
        sum from i to n of ti = n - 1 
    """
    return sum(tree) == len(tree) - 1 and tree[len(tree) - 1] == 0
