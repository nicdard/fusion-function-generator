import random
from typing import List, Tuple

# Ordered Tree Encoding:
# an n-tuple for a tree of n nodes:
#   t = (t1, t2, ..., ti,..., tn)
# ti is the i-th node of the tree t.
# A parent node implies ti > 0, while a leaf node implies ti = 0.
# The nodes are visited in preorder (depth-first left to right) to determine the order of the tree.
# The last node of the tree is thus tn, so tn = 0
# and ti is in [0, n - 1].
# Note: we use a list for simplicity/efficiency.
def generate_arbitrary_ordered_tree(root: int, n: int, bounds: Tuple[int, int]):
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

def validate(tree: List[int]) -> bool:
    """
    Returns true if a tree of n nodes respect the property:
        sum from i to n of ti = n - 1 
    """
    return sum(tree) == len(tree) - 1 and tree[len(tree) - 1] == 0
