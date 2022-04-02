import random
from typing import List, Tuple

from operators import gen_configuration
from operators.gen.boolean_theory import *
from operators.gen.integer_theory import *
from operators.gen.real_theory import *


# Ordered Tree Encoding:
# an n-tuple for a tree of n nodes:
#   t = (t1, t2, ..., ti,..., tn)
# ti is the i-th node of the tree t.
# A parent node implies ti > 0, while a leaf node implies ti = 0.
# The nodes are visited in preorder (depth-first left to right) to determine the order of the tree.
# The last node of the tree is thus tn, so tn = 0
# and ti is in [0, n - 1].
# Note: we use a list for simplicity/efficiency.
def generate_arity_tree(root: int, n: int, bounds: Tuple[int, int]):
    """
    Generates a list of integers representing a tree containing n
    nodes. The first node is already set to root.
    Note: the algorithm creates a tree of n - 1 nodes, counting also the
    root, and the last 0 of the tuple is dangling.
    """
    if root < bounds[0] or root > bounds[1]:
        raise ValueError(f"The root of the tree should be an operator taking a number of arguments in ({bounds})")
    tree = [root]
    
    def expected_nodes():
        return sum(tree) + 1

    def missing_nodes():
        return expected_nodes() - len(tree)
    
    while len(tree) < n:
        remaining = n - expected_nodes()
        lower = bounds[0]
        upper = min(bounds[1], remaining)
        branching_choices = list(range(lower, upper+1))
        
        if not (missing_nodes() == 1 and remaining > 1):
            branching_choices.append(0)
        
        tree.append(random.choice(branching_choices))
    
    return tree


def generate_operator_tree(arity_tree, num_variables):
    num_leaves = len([n for n in arity_tree if n == 0])

    def recursive_generation(idx, operator_type):
        nonlocal num_leaves, num_variables
        n = arity_tree[idx]
        idx += 1
        params = []

        if n == 0:
            if num_variables == 0:
                op_name = gen_configuration.get_constant(operator_type)
                is_variable = False
            elif num_variables < num_leaves:
                op_name, is_variable = gen_configuration.get_leaf(operator_type)
            else:
                op_name = gen_configuration.get_variable(operator_type)
                is_variable = True

            num_leaves -= 1
            if is_variable:
                params.append(f"x{num_variables}")
                num_variables -= 1
        else:
            op_name = gen_configuration.get_eligible_operator(operator_type, n)

            for _ in range(n):
                param, idx = recursive_generation(idx, operator_type)
                params.append(param)

        return globals()[op_name](*params), idx

    root_type = random.choice(gen_configuration.get_theories())
    operator_tree, _ = recursive_generation(0, root_type)
    root_name = gen_configuration.get_root(root_type)

    output_var = globals()[gen_configuration.get_variable(root_type)]("x0")
    root = globals()[root_name](output_var, operator_tree)

    return root


def validate(tree: List[int]) -> bool:
    """
    Returns true if a tree of n nodes respect the property:
        sum from i to n of ti = n - 1 
    """
    return sum(tree) == len(tree) - 1 and tree[len(tree) - 1] == 0
