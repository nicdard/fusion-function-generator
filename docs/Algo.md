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


## Mixing more theories

### Iddea 1: replacing sub patterns / expressions

 We know how to invert addition;
 
 we have the (str.len String Int) operator that maps a string into its length;
 
 we can search the two seed formulas f_1 f_2 for a len expression in each of them, len_1 and len_2, and use a fusion function (let's call it mixture relation) such as:

> k = len_1 + len_2  

This formula is invertible:

> len_1 = k - len_2
> len_2 = k - len_1

and provides us the possibility to join different theories (in this case strings and integers)

This requires a bit of work: 
* we need to discover such relations
* we need to extend our representation to handle those mixtures, specifically those operators that are used to map from one theory to another, maybe using special type of nodes which wrap the basic operation. 
Those wrappers will need to not being inverted, but their content can be. Actually by thinking a bit more, we cannot invert functions from one theory to another, so we could in practice discard the wrapper idea and use the operators as they are, since we will not need to distinguish cases where we want to invert or not them. 
Also, in presence of different operators mapping from one theory to another with the same gurantees, we can define general forms of those mixtures relations where than the tool can generate random subexpression operators that math the types.
* we need to modify yinyang in order to perform subexpression (there should be something similar already implemented in `GenTypeAwareMutation`) subtitution and its configuration format

#### Further considerations:
The operation shown in the example is fairly simple, but we can have also an operator which operates on the result of a len operation over a complex string expression and on the other side over a complex integer expression. Then our resulting fusion function will have input variables in the domain of integers and the domain of string (more precisely, string subexpression outputting integers). Thus, we are extending the idea of fusion function to subexpression fusion within the seed formulas, and at the level of applying multiple layers of fusion function for each theory that we exploit. A fusion function could have a signature where each input variable is defined to be equal to a pattern (a subexpression of a certain general shape (something similar to like type holes)) or as a simple variable.

Discussion:
* do we need to encode this at the generator level? hat about encoding this at yinyang level directly? what about applying multiple fusion functions over the same formula, which may have variables from different domains?

I think that we could also modify yinyang to handle subexpression substitution, generate simple mixture functions as the one in the example and then instruct it to perform multiple substitutions one on top of the other with fusion functions of different theories, but I am not sure about how the two approaches would behave in comparison.


