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
from typing import Dict, List, Set

BOOLEAN = "BooleanOperator"
INTEGER = "IntegerOperator"
REAL = "RealOperator"
STRING = "StringOperator"
BITVECTOR = "BitVectorOperator"

CONSTANT = "const"
VARIABLE = "var"
LITERAL = "lit"

# A map from theories name to theory operation.
# Each operation specifies either the number of input parameters (having the same theory operator type).
# or the list of parameters with the names and types of each one.
# Insert here new theories and their operations!
main_operators: Dict[str, Dict[str, List[str]]] = {
    BOOLEAN: {
        "BooleanNot": [BOOLEAN],
        "BooleanXor": [BOOLEAN, BOOLEAN],
        "BooleanIte": [BOOLEAN, BOOLEAN]
    },
    INTEGER: {
        "IntegerNegation": [INTEGER],
        "IntegerAddition": [INTEGER, INTEGER],
        "IntegerSubtraction": [INTEGER, INTEGER],
        "IntegerMultiplication": [INTEGER, INTEGER],
        "BitVectorToInteger": [BITVECTOR],
        "IntegerIte": [INTEGER, INTEGER]
    },
    REAL: {
        "RealNegation": [REAL],
        "RealAddition": [REAL, REAL],
        "RealSubtraction": [REAL, REAL],
        "RealMultiplication": [REAL, REAL],
        "IntegerToReal": [INTEGER],
        "RealIte": [REAL, REAL]
    },
    STRING: {
        "StringConcatenation1n1": [STRING, STRING],
        "StringConcatenation1n2": [STRING, STRING],
        "StringConcatenation1n3": [STRING, STRING],
        "StringConcatenation2n1": [STRING, STRING],
        "StringConcatenation2n2": [STRING, STRING],
        "StringConcatenation2n3": [STRING, STRING],
        "IntegerToString": [INTEGER],
        "StringIte": [STRING, STRING]
    },
    BITVECTOR: {
        "BitVectorNot": [BITVECTOR],
        "BitVectorNegation": [BITVECTOR],
        "BitVectorXor": [BITVECTOR, BITVECTOR],
        "BitVectorConcatenation": [BITVECTOR, BITVECTOR],
        "BitVectorIte": [BITVECTOR, BITVECTOR]
    },
}

# These operators are not invertible and thus not used in generation, but necessary
# to define the inverse of some main operators
fringe_operators: Dict[str, Dict[str, List[str]]] = {
    BOOLEAN: {
        "BooleanOr": [BOOLEAN, BOOLEAN],
        "BooleanAnd": [BOOLEAN, BOOLEAN],
        "BooleanImplies": [BOOLEAN, BOOLEAN],
        "BooleanDistinct": [BOOLEAN, BOOLEAN],
        "IntegerDistinct": [BOOLEAN, BOOLEAN],
        "RealDistinct": [BOOLEAN, BOOLEAN],
        "StringDistinct": [BOOLEAN, BOOLEAN],
        "BitVectorDistinct": [BITVECTOR, BITVECTOR],
        "IntegerLess": [INTEGER, INTEGER],
        "IntegerLessOrEqual": [INTEGER, INTEGER],
        "IntegerGreater": [INTEGER, INTEGER],
        "IntegerGreaterOrEqual": [INTEGER, INTEGER],
        "RealLess": [REAL, REAL],
        "RealLessOrEqual": [REAL, REAL],
        "RealGreater": [REAL, REAL],
        "RealGreaterOrEqual": [REAL, REAL],
        "StringLess": [STRING, STRING],
        "StringLessEqual": [STRING, STRING],
        "StringPrefixOf": [STRING, STRING],
        "StringSuffixOf": [STRING, STRING],
        "StringContains": [STRING, STRING]
    },
    INTEGER: {
        "IntegerDivision": [INTEGER, INTEGER],
        "StringLength": [STRING],
        "StringIndexOf": [STRING, STRING, INTEGER],
        "RealToInteger": [REAL],
        "StringToInteger": [STRING],
        "StringToIntegerBuiltIn": [STRING]
    },
    REAL: {
        "RealDivision": [REAL, REAL]
    },
    STRING: {
        "StringReplacement": [STRING, STRING, STRING],
        "Substring": [STRING, INTEGER, INTEGER],
        "StringFromIntegerBuiltIn": [INTEGER],
        "StringAt": [STRING, INTEGER]
    },
    BITVECTOR: {
        "BitVectorExtraction": [BITVECTOR, INTEGER, INTEGER],
        "IntegerToBitVector": [INTEGER]
    },
}

theory_declarations: Dict[str, Dict[str, List[str]]] = {
    k: {**main_operators[k], **fringe_operators[k]} for k in main_operators
}

leaf_operators: Dict[str, Dict[str, str]] = {
    BOOLEAN: {
        CONSTANT: "BooleanConstant",
        VARIABLE: "BooleanVariable",
        LITERAL: "BooleanLiteral"
    },
    INTEGER: {
        CONSTANT: "IntegerConstant",
        VARIABLE: "IntegerVariable",
        LITERAL: "IntegerLiteral"
    },
    REAL: {
        CONSTANT: "RealConstant",
        VARIABLE: "RealVariable",
        LITERAL: "RealLiteral"
    },
    STRING: {
        CONSTANT: "StringConstant",
        VARIABLE: "StringVariable",
        LITERAL: "StringLiteral"
    },
    BITVECTOR: {
        CONSTANT: "BitVectorConstant",
        VARIABLE: "BitVectorVariable",
        LITERAL: "BitVectorLiteral"
    },
}

root_operators: Dict[str, str] = {
    BOOLEAN: "BooleanEquality",
    INTEGER: "IntegerEquality",
    REAL: "RealEquality",
    STRING: "StringEquality",
    BITVECTOR: "BitVectorEquality"
}

BOOLEAN_OPTION = "bool"
INT_OPTION = "int"
REAL_OPTION = "real"
STRING_OPTION = "string"
BITVECTOR_OPTION = "bitvector"

# A map from command line options to the internal representation.
_option_to_operator_type: Dict[str, str] = {
    BOOLEAN_OPTION: BOOLEAN,
    INT_OPTION: INTEGER,
    REAL_OPTION: REAL,
    STRING_OPTION: STRING,
    BITVECTOR_OPTION: BITVECTOR
}


THEORY_OPTIONS = list(_option_to_operator_type.keys())


_available_theories: Set[str] = set(theory_declarations.keys())


def set_available_theories(theories) -> None:
    global _available_theories
    _available_theories = set(
        [_option_to_operator_type[opt] for opt in theories])


def get_theories() -> List[str]:
    return list(_available_theories)


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


def get_fringe_operators(theory: str, arity: int, params_type=None) -> List[str]:
    operator_choices = []

    if params_type is None:
        params_type = _available_theories

    for operator in fringe_operators[theory].keys():
        params = get_operator_parameters(theory, operator)
        if arity == len(params):
            if set(params).issubset(params_type):
                operator_choices.append(operator)

    return operator_choices


def get_theory_name(theory: str) -> str:
    return theory.split("Operator")[0]


def get_module_name(theory: str) -> str:
    return get_theory_name(theory).lower() + "_theory"


def get_operator_class(theory: str, name: str) -> 'Operator.__class__':
    module_name = get_module_name(theory)
    module = importlib.import_module('ffg.operators.' + module_name)
    return getattr(module, name)
