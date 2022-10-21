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

BOOLEAN_OPERATOR = "BooleanOperator"
INTEGER_OPERATOR = "IntegerOperator"
REAL_OPERATOR = "RealOperator"
STRING_OPERATOR = "StringOperator"
BITVECTOR_OPERATOR = "BitVectorOperator"

# A map from theories name to theory operation.
# Each operation specifies either the number of input parameters (having the same theory operator type).
# or the list of parameters with the names and types of each one.
# Insert here new theories and their operations!
main_operators: Dict[str, Dict[str, List[str]]] = {
    BOOLEAN_OPERATOR: {
        "BooleanNot": [BOOLEAN_OPERATOR],
        "BooleanXor": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "BooleanIte": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR]
    },
    INTEGER_OPERATOR: {
        "IntegerNegation": [INTEGER_OPERATOR],
        "IntegerAddition": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "IntegerSubtraction": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "IntegerMultiplication": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "IntegerIte": [INTEGER_OPERATOR, INTEGER_OPERATOR]
    },
    REAL_OPERATOR: {
        "RealNegation": [REAL_OPERATOR],
        "RealAddition": [REAL_OPERATOR, REAL_OPERATOR],
        "RealSubtraction": [REAL_OPERATOR, REAL_OPERATOR],
        "RealMultiplication": [REAL_OPERATOR, REAL_OPERATOR],
        "IntegerToReal": [INTEGER_OPERATOR],
        "RealIte": [REAL_OPERATOR, REAL_OPERATOR]
    },
    STRING_OPERATOR: {
        "StringConcatenation1n1": [STRING_OPERATOR, STRING_OPERATOR],
        "StringConcatenation1n2": [STRING_OPERATOR, STRING_OPERATOR],
        "StringConcatenation1n3": [STRING_OPERATOR, STRING_OPERATOR],
        "StringConcatenation2n1": [STRING_OPERATOR, STRING_OPERATOR],
        "StringConcatenation2n2": [STRING_OPERATOR, STRING_OPERATOR],
        "StringConcatenation2n3": [STRING_OPERATOR, STRING_OPERATOR],
        "StringIte": [STRING_OPERATOR, STRING_OPERATOR]
    },
    BITVECTOR_OPERATOR: {
        "BitVectorNot": [BITVECTOR_OPERATOR],
        "BitVectorNegation": [BITVECTOR_OPERATOR],
        "BitVectorXor": [BITVECTOR_OPERATOR, BITVECTOR_OPERATOR],
        "BitVectorConcatenation": [BITVECTOR_OPERATOR, BITVECTOR_OPERATOR],
        "BitVectorIte": [BITVECTOR_OPERATOR, BITVECTOR_OPERATOR]
    },
}

# These operators are not invertible and thus not used in generation, but necessary
# to define the inverse of some main operators
fringe_operators: Dict[str, Dict[str, List[str]]] = {
    BOOLEAN_OPERATOR: {
        "BooleanOr": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "BooleanAnd": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "BooleanImplies": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "BooleanDistinct": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "IntegerDistinct": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "RealDistinct": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "StringDistinct": [BOOLEAN_OPERATOR, BOOLEAN_OPERATOR],
        "BitVectorDistinct": [BITVECTOR_OPERATOR, BITVECTOR_OPERATOR],
        "IntegerLess": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "IntegerLessOrEqual": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "IntegerGreater": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "IntegerGreaterOrEqual": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "RealLess": [REAL_OPERATOR, REAL_OPERATOR],
        "RealLessOrEqual": [REAL_OPERATOR, REAL_OPERATOR],
        "RealGreater": [REAL_OPERATOR, REAL_OPERATOR],
        "RealGreaterOrEqual": [REAL_OPERATOR, REAL_OPERATOR],
        "StringLess": [STRING_OPERATOR, STRING_OPERATOR],
        "StringLessEqual": [STRING_OPERATOR, STRING_OPERATOR],
        "StringPrefixOf": [STRING_OPERATOR, STRING_OPERATOR],
        "StringSuffixOf": [STRING_OPERATOR, STRING_OPERATOR],
        "StringContains": [STRING_OPERATOR, STRING_OPERATOR],
    },
    INTEGER_OPERATOR: {
        "IntegerDivision": [INTEGER_OPERATOR, INTEGER_OPERATOR],
        "StringLength": [STRING_OPERATOR],
        "StringIndexof": [STRING_OPERATOR, STRING_OPERATOR, INTEGER_OPERATOR],
        "RealToInteger": [REAL_OPERATOR],
    },
    REAL_OPERATOR: {
        "RealDivision": [REAL_OPERATOR, REAL_OPERATOR],
    },
    STRING_OPERATOR: {
        "StringReplacement": [STRING_OPERATOR, STRING_OPERATOR, STRING_OPERATOR],
        "Substring": [STRING_OPERATOR, INTEGER_OPERATOR, INTEGER_OPERATOR],
    },
    BITVECTOR_OPERATOR: {
        "BitVectorExtraction": [BITVECTOR_OPERATOR, INTEGER_OPERATOR, INTEGER_OPERATOR],
    },
}

theory_declarations: Dict[str, Dict[str, List[str]]] = {
    k: {**main_operators[k], **fringe_operators[k]} for k in main_operators
}

leaf_operators: Dict[str, Dict[str, str]] = {
    BOOLEAN_OPERATOR: {
        "const": "BooleanConstant",
        "var": "BooleanVariable",
        "lit": "BooleanLiteral"
    },
    INTEGER_OPERATOR: {
        "const": "IntegerConstant",
        "var": "IntegerVariable",
        "lit": "IntegerLiteral"
    },
    REAL_OPERATOR: {
        "const": "RealConstant",
        "var": "RealVariable",
        "lit": "RealLiteral"
    },
    STRING_OPERATOR: {
        "const": "StringConstant",
        "var": "StringVariable",
        "lit": "StringLiteral"
    },
    BITVECTOR_OPERATOR: {
        "const": "BitVectorConstant",
        "var": "BitVectorVariable",
        "lit": "BitVectorLiteral"
    },
}

root_operators: Dict[str, str] = {
    BOOLEAN_OPERATOR: "BooleanEquality",
    INTEGER_OPERATOR: "IntegerEquality",
    REAL_OPERATOR: "RealEquality",
    STRING_OPERATOR: "StringEquality",
    BITVECTOR_OPERATOR: "BitVectorEquality",
}

BOOLEAN_OPTION = "bool"
INT_OPTION = "int"
REAL_OPTION = "real"
STRING_OPTION = "string"
BITVECTOR_OPTION = "bitvector"


# A map from command line options to the internal representation.
_option_to_operator_type: Dict[str, str] = {
    BOOLEAN_OPTION: BOOLEAN_OPERATOR,
    INT_OPTION: INTEGER_OPERATOR,
    REAL_OPTION: REAL_OPERATOR,
    STRING_OPTION: STRING_OPERATOR,
    BITVECTOR_OPTION: BITVECTOR_OPERATOR,
}


THEORY_OPTIONS = list(_option_to_operator_type.keys())


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


def get_fringe_operators(theory: str, arity: int, params_type: List[str] = []) -> List[str]:
    operator_choices = []
    if (len(params_type) == 0):
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
