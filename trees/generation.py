from random import randint
from typing import List
from operators.gen_configuration import reverse_theory_dict

# The reverse index from arity to theory to operators
_index = reverse_theory_dict()

# L and U
_bounds = min(_index.keys()), max(_index.keys())

# Ordered Tree Encoding:
# an n-tuple for a tree of n nodes:
#   t = (t1, t2, ..., ti,..., tn)
# ti is the i-th node of the tree t.
# A parent node implies ti > 0, while a leaf node implies ti = 0.
# The nodes are visited in preorder (depth-first left to right).
# The last node of the tree is thus tn, so tn = 0
# and ti is in [0, n - 1].
# Note: we use a list for simplicity/efficiency.
def generate_arbitrary_ordered_tree(n: int):
    """
    Generates a list of integers representing a tree containing n
    nodes.  
    """
    s = 0
    upper_bound = n
    t = [1]
    for i in range(n):
        lower_bound = 1 - sign(t[i] + s - 1)
        upper_bound = upper_bound - t[i]
        ti = randint(lower_bound, upper_bound)
        t.append(ti)
        s = s + ti
    return t
    

def sign(n: int):
    return 1 if n > 0 else -1 if n < 0 else 0

def validate(tree: List[int]) -> bool:
    """
    Returns true if a tree of n nodes respect the property:
        sum from i to n of ti = n - 1 
    """
    sum(tree) == len(tree) - 1
