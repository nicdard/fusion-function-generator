# Autmatic inversion of generated functions.

Goal: given a fusion function represented as a tree `T1` with the properties described in the proposal we want to find the trees representing the inversion function for each input.

## One theory at the time

High level idea:
* explitly distinguish between input variables and output variables nodes.
* an output variable stores the tree of operators it embodies.
* Leaves can be either input variables or constants.
* each node will store a ref to its children.
* explicitly pass parent during inversion, i.e. when calling the next inversion the current node is already passed in the inverted form. The output variable node (root) will start the visit from the root of the operator tree by passing itself as an input variable.
* starting from the root (which is the output variable), explore the whole tree with post-order traversal. Each step returns a rom variable names to their respective inverted operators trees:

    * for the leaves, we either return an empty dictionary (for constants) or a dictionary containing only one variable (for input variables) associated to its inverted function.
    * for each intermediate node return the dictionary containing all the variables found in its subtree

