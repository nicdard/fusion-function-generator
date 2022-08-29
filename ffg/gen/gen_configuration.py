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


import importlib
from typing import Dict, List

# A map from theories name to theory operation.
# Each operation specifies either the number of input parameters (having the same theory operator type).
# or the list of parameters with the names and types of each one.
# Insert here new theories and their operations!
main_operators: Dict[str, Dict[str, List[str]]] = {
    "BooleanOperator": {
        "BooleanNot": ["BooleanOperator"],
        "BooleanXor": ["BooleanOperator", "BooleanOperator"],
    },
    "IntegerOperator": {
        "IntegerNegation": ["IntegerOperator"],
        "IntegerAddition": ["IntegerOperator", "IntegerOperator"],
        "IntegerSubtraction": ["IntegerOperator", "IntegerOperator"],
        "IntegerMultiplication": ["IntegerOperator", "IntegerOperator"],
    },
    "RealOperator": {
        "RealNegation": ["RealOperator"],
        "RealAddition": ["RealOperator", "RealOperator"],
        "RealSubtraction": ["RealOperator", "RealOperator"],
        "RealMultiplication": ["RealOperator", "RealOperator"],
        "IntegerToReal": ["IntegerOperator"],
    },
    "StringOperator": {
        "StringConcatenation1n1": ["StringOperator", "StringOperator"],
        "StringConcatenation1n2": ["StringOperator", "StringOperator"],
        "StringConcatenation1n3": ["StringOperator", "StringOperator"],
        "StringConcatenation2n1": ["StringOperator", "StringOperator"],
        "StringConcatenation2n2": ["StringOperator", "StringOperator"],
        "StringConcatenation2n3": ["StringOperator", "StringOperator"],
    },
    "BitVectorOperator": {
        "BitVectorNot": ["BitVectorOperator"],
        "BitVectorNegation": ["BitVectorOperator"],
        "BitVectorXor": ["BitVectorOperator", "BitVectorOperator"],
        "BitVectorConcatenation": ["BitVectorOperator", "BitVectorOperator"],
    },
}

# These operators are not invertible and thus not used in generation, but necessary
# to define the inverse of some main operators
fringe_operators: Dict[str, Dict[str, List[str]]] = {
    "BooleanOperator": {},
    "IntegerOperator": {
        "IntegerDivision": ["IntegerOperator", "IntegerOperator"],
        "StringLength": ["StringOperator"],
        "StringIndexof": ["StringOperator", "StringOperator", "IntegerOperator"],
        "RealToInteger": ["RealOperator"],
    },
    "RealOperator": {
        "RealDivision": ["RealOperator", "RealOperator"],
    },
    "StringOperator": {
        "StringReplacement": ["StringOperator", "StringOperator", "StringOperator"],
        "Substring": ["StringOperator", "IntegerOperator", "IntegerOperator"],
    },
    "BitVectorOperator": {
        "BitVectorExtraction": ["BitVectorOperator", "IntegerOperator", "IntegerOperator"],
    },
}

theory_declarations: Dict[str, Dict[str, List[str]]] = {
    k: {**main_operators[k], **fringe_operators[k]} for k in main_operators
}

leaf_operators: Dict[str, Dict[str, str]] = {
    "BooleanOperator": {
        "const": "BooleanConstant",
        "var": "BooleanVariable",
        "lit": "BooleanLiteral"
    },
    "IntegerOperator": {
        "const": "IntegerConstant",
        "var": "IntegerVariable",
        "lit": "IntegerLiteral"
    },
    "RealOperator": {
        "const": "RealConstant",
        "var": "RealVariable",
        "lit": "RealLiteral"
    },
    "StringOperator": {
        "const": "StringConstant",
        "var": "StringVariable",
        "lit": "StringLiteral"
    },
    "BitVectorOperator": {
        "const": "BitVectorConstant",
        "var": "BitVectorVariable",
        "lit": "BitVectorLiteral"
    },
}

root_operators: Dict[str, str] = {
    "BooleanOperator": "BooleanEquality",
    "IntegerOperator": "IntegerEquality",
    "RealOperator": "RealEquality",
    "StringOperator": "StringEquality",
    "BitVectorOperator": "BitVectorEquality",
}

# A map from command line options to the internal representation.
_option_to_operator_type: Dict[str, str] = {
    "bool": "BooleanOperator",
    "int": "IntegerOperator",
    "real": "RealOperator",
    "string": "StringOperator",
    "bitvector": "BitVectorOperator",
}

_available_theories: List[str] = list(theory_declarations.keys())


def set_available_theories(theories) -> None:
    global _available_theories
    _available_theories = [_option_to_operator_type[opt] for opt in theories]


def get_theories() -> List[str]:
    return _available_theories


def get_operators(theory: str) -> List[str]:
    return list(theory_declarations[theory].keys())


def get_all_nodes(theory: str) -> List[str]:
    return [*get_operators(theory), get_variable(theory),
            get_constant(theory), get_literal(theory), get_root(theory)]


def get_operator_types(theory: str) -> List[str]:
    type_set = {theory}
    for op in theory_declarations[theory]:
        for in_type in theory_declarations[theory][op]:
            type_set.add(in_type)
    return list(type_set)


def get_arities(theory: str) -> List[int]:
    arities = set()
    for op in main_operators[theory].keys():
        params = get_operator_parameters(theory, op)
        if set(params).issubset(_available_theories):
            arities.add(len(params))
    return list(arities)


def get_operator_parameters(theory: str, operator: str) -> List[str]:
    if operator in leaf_operators[theory].values():
        return []
    return theory_declarations[theory][operator]


def get_constant(theory: str) -> str:
    return leaf_operators[theory]["const"]


def get_variable(theory: str) -> str:
    return leaf_operators[theory]["var"]


def get_literal(theory: str) -> str:
    return leaf_operators[theory]["lit"]


def get_root(theory: str) -> str:
    return root_operators[theory]


def get_eligible_operators(theory: str, min_arity: int, max_arity: int) -> List[str]:
    operator_choices = []

    for operator in main_operators[theory].keys():
        params = get_operator_parameters(theory, operator)
        if min_arity <= len(params) <= max_arity:
            if set(params).issubset(_available_theories):
                operator_choices.append(operator)

    return operator_choices


def get_theory_name(theory: str) -> str:
    return theory.split("Operator")[0]


def get_module_name(theory: str) -> str:
    return get_theory_name(theory).lower() + "_theory"


def get_operator_class(theory: str, name: str) -> 'Operator.__class__':
    module_name = get_module_name(theory)
    module = importlib.import_module('src.operators.' + module_name)
    return getattr(module, name)
