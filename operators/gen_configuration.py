from cgi import parse_multipart
from copy import deepcopy
from re import A
from typing import Dict, List, Union

# A map from theories name to theory operation.
# Each operation specifies either the number of input parameters (having the same theory operator type).
# or the list of parameters with the names and types of each one.
# Insert here new theories and their operations!
theories: Dict[str, Dict[str, Union[str, int]]] = {
    "Boolean": {
        "XOR": 2,
        "NOT": 1,
        "Constant": "value: bool",
        "Variable": "name: str",
        "Equality": 2
    },
    "Integer": {
        "Addition"      : 2,
        "Subtraction"   : 2,
        "Multiplication": 2,
        "Division"      : 2,
        "Constant": "value: int",
        "Variable": "name: str",
        "Equality": 2
    },
    "Real": {
        "Addition"      : 2,
        "Subtraction"   : 2,
        "Multiplication": 2,
        "Division"      : 2,
        "Constant": "value: int",
        "Variable": "name: str",
        "Equality": 2
    }
}


def reverse_theory_dict() -> Dict[int, Dict[str, List[str]]]:
    """
    Returns a reverse dictionary from the (arity, theory) to operators.
    """
    parse_arity = lambda params : len(params) != 0 if len(params.split(",")) else 0
    arity_map = {}
    for theory in theories.keys():
        theory = theories[theory]
        # We assume to have at least one bnary operator in a theory, 
        # since we want to be able to fuse functions. Including theories
        # without such an operation would be useless.
        for op in theory:
            args = theory[op]
            arity = parse_arity(args)
            if arity in arity_map.keys():
                if theory in arity_map[arity]:
                    arity_map[arity][theory].append(op)
                else:
                    arity_map[arity][theory] = [op]
            else:
                arity_map[arity] = {}
                arity_map[arity][theory] = []
    return arity_map
