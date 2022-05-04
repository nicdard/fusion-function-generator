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
import importlib
from typing import Dict, List

# A map from theories name to theory operation.
# Each operation specifies either the number of input parameters (having the same theory operator type).
# or the list of parameters with the names and types of each one.
# Insert here new theories and their operations!
main_operators: Dict[str, Dict[str, List[str]]] = {
    "BooleanOperator": {
        "BooleanXor": ["BooleanOperator", "BooleanOperator"],
        "BooleanNot": ["BooleanOperator"],
    },
    "IntegerOperator": {
        "IntegerAddition": ["IntegerOperator", "IntegerOperator"],
        "IntegerSubtraction": ["IntegerOperator", "IntegerOperator"],
        "IntegerMultiplication": ["IntegerOperator", "IntegerOperator"],
    },
    "RealOperator": {
        "RealAddition": ["RealOperator", "RealOperator"],
        "RealSubtraction": ["RealOperator", "RealOperator"],
        "RealMultiplication": ["RealOperator", "RealOperator"],
        "RealDivision": ["RealOperator", "RealOperator"],
    }
}

# These operators are not invertible and thus not used in generation, but necessary
# to define the inverse of some main operators
fringe_operators: Dict[str, Dict[str, List[str]]] = {
    "BooleanOperator": {},
    "IntegerOperator": {
        "IntegerDivision": ["IntegerOperator", "IntegerOperator"],
    },
    "RealOperator": {}
}

theory_declarations = {k: main_operators[k] | fringe_operators[k] for k in main_operators}

leaf_operators = {
    "BooleanOperator": {
        "BooleanConstant": "random.random() > 0.5",
        "BooleanVariable": str,
    },
    "IntegerOperator": {
        "IntegerConstant": "random.randint(0, 1000)",
        "IntegerVariable": str,
    },
    "RealOperator": {
        "RealConstant": "random.random() * 1000",
        "RealVariable": str,
    }
}

root_operators: Dict[str, str] = {
    "BooleanOperator": "BooleanEquality",
    "IntegerOperator": "IntegerEquality",
    "RealOperator": "RealEquality",
}


def get_theories():
    return list(theory_declarations.keys())


def get_operators(theory: str):
    return list(theory_declarations[theory].keys())


def get_arities(theory: str) -> List[int]:
    arities = []

    for op in get_operators(theory):
        arities.append(len(get_operator_parameters(theory, op)))

    return arities


def get_operator_parameters(theory: str, operator: str):
    return theory_declarations[theory][operator]


def get_constant(operator_type):
    return list(leaf_operators[operator_type].keys())[0]


def get_constant_initializer(operator_type):
    return leaf_operators[operator_type][get_constant(operator_type)]


def get_variable(operator_type):
    return list(leaf_operators[operator_type].keys())[1]


def get_root(operator_type):
    return root_operators[operator_type]


def get_eligible_operator(operator_type, arity):
    if operator_type is None:
        operator_type = random.choice(get_theories())

    theory = main_operators[operator_type]
    operator_choices = []

    for operator in theory.keys():
        n = len([p for p in theory[operator] if "Operator" in p])
        if n == arity:
            operator_choices.append(operator)

    return random.choice(operator_choices)


def get_theory_name(theory: str) -> str:
    return theory.split("Operator")[0]


def get_module_name(theory: str) -> str:
    return get_theory_name(theory).lower() + "_theory"


def get_operator_class(theory, name):
    module_name = get_module_name(theory)
    module = importlib.import_module('src.operators.' + module_name)
    return getattr(module, name)
