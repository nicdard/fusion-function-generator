from typing import Dict, Union

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
