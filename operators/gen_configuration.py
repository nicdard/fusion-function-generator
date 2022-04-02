import random
from typing import Dict, List

# A map from theories name to theory operation.
# Each operation specifies either the number of input parameters (having the same theory operator type).
# or the list of parameters with the names and types of each one.
# Insert here new theories and their operations!
theories_declaration: Dict[str, Dict[str, List[str]]] = {
    "BooleanOperator": {
        "BooleanXOR": ["BooleanOperator", "BooleanOperator"],
        "BooleanNOT": ["BooleanOperator"],
        "BooleanConstant": ["bool"],
        "BooleanVariable": ["str"],
    },
    "IntegerOperator": {
        "IntegerAddition": ["IntegerOperator", "IntegerOperator"],
        "IntegerSubtraction": ["IntegerOperator", "IntegerOperator"],
        "IntegerMultiplication": ["IntegerOperator", "IntegerOperator"],
        "IntegerDivision": ["IntegerOperator", "IntegerOperator"],
        "IntegerConstant": ["int"],
        "IntegerVariable": ["str"],
    },
    "RealOperator": {
        "RealAddition": ["RealOperator", "RealOperator"],
        "RealSubtraction": ["RealOperator", "RealOperator"],
        "RealMultiplication": ["RealOperator", "RealOperator"],
        "RealDivision": ["RealOperator", "RealOperator"],
        "RealConstant": ["float"],
        "RealVariable": ["str"],
    }
}

leaf_operators = {
    "BooleanOperator": {
        "BooleanConstant": bool,
        "BooleanVariable": str,
    },
    "IntegerOperator": {
        "IntegerConstant": int,
        "IntegerVariable": str,
    },
    "RealOperator": {
        "RealConstant": float,
        "RealVariable": str,
    }
}

root_operators: Dict[str, str] = {
    "BooleanOperator": "BooleanEquality",
    "IntegerOperator": "IntegerEquality",
    "RealOperator": "RealEquality",
}


def get_theories():
    return list(theories_declaration.keys())


def get_leaf(operator_type):
    theory = leaf_operators[operator_type]
    op = random.choice(list(theory.keys()))
    return op, "variable" in op.lower()


def get_constant(operator_type):
    return list(leaf_operators[operator_type].keys())[0]


def get_variable(operator_type):
    return list(leaf_operators[operator_type].keys())[1]


def get_root(operator_type):
    return root_operators[operator_type]


def get_eligible_operator(operator_type, arity):
    if operator_type is None:
        operator_type = random.choice(list(theories_declaration.keys()))

    theory = theories_declaration[operator_type]
    operator_choices = []

    for operator in theory.keys():
        n = len([p for p in theory[operator] if "operator" in p.lower()])
        if n == arity:
            operator_choices.append(operator)

    return random.choice(operator_choices)
