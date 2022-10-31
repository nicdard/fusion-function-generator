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
from typing import List

from ffg.gen.gen_configuration import BITVECTOR, BOOLEAN, INTEGER, REAL, STRING
from ffg.gen.gen_configuration import get_fringe_operators, get_operator_class
from ffg.operators.bitvector_theory import *
from ffg.operators.boolean_theory import *
from ffg.operators.generic import Operator
from ffg.operators.integer_theory import *
from ffg.operators.real_theory import *
from ffg.operators.string_theory import *


class InitializationVisitor(BooleanVisitor, IntegerVisitor, RealVisitor, StringVisitor, BitVectorVisitor):
    def __init__(self, in_variables: List[str], out_variable: str):
        self.in_variables = in_variables
        self.out_variable = out_variable
        self._reset()

    def _reset(self):
        self._var_idx = 0
        self._const_idx = 0
        self._size = {}
        self._is_var = {}

    def visit_boolean_not(self, operator: BooleanNot):
        self._visit_operator(operator, 1)

    def visit_boolean_xor(self, operator: BooleanXor):
        self._visit_operator(operator, 2)

    def visit_boolean_ite(self, operator: BooleanIte):
        self._visit_ite(operator, BOOLEAN)

    def visit_boolean_or(self, operator: BooleanOr):
        self._visit_operator(operator, 2)

    def visit_boolean_and(self, operator: BooleanAnd):
        self._visit_operator(operator, 2)

    def visit_boolean_implies(self, operator: BooleanImplies):
        self._visit_operator(operator, 2)

    def visit_boolean_distinct(self, operator: BooleanDistinct):
        self._visit_operator(operator, 2)

    def visit_integer_distinct(self, operator: IntegerDistinct):
        self._visit_operator(operator, 2)

    def visit_real_distinct(self, operator: RealDistinct):
        self._visit_operator(operator, 2)

    def visit_string_distinct(self, operator: StringDistinct):
        self._visit_operator(operator, 2)

    def visit_bit_vector_distinct(self, operator: BitVectorDistinct):
        self._visit_operator(operator, 2)

    def visit_integer_less(self, operator: IntegerLess):
        self._visit_operator(operator, 2)

    def visit_integer_less_or_equal(self, operator: IntegerLessOrEqual):
        self._visit_operator(operator, 2)

    def visit_integer_greater(self, operator: IntegerGreater):
        self._visit_operator(operator, 2)

    def visit_integer_greater_or_equal(self, operator: IntegerGreaterOrEqual):
        self._visit_operator(operator, 2)

    def visit_real_less(self, operator: RealLess):
        self._visit_operator(operator, 2)

    def visit_real_less_or_equal(self, operator: RealLessOrEqual):
        self._visit_operator(operator, 2)

    def visit_real_greater(self, operator: RealGreater):
        self._visit_operator(operator, 2)

    def visit_real_greater_or_equal(self, operator: RealGreaterOrEqual):
        self._visit_operator(operator, 2)

    def visit_string_less(self, operator: StringLess):
        self._visit_operator(operator, 2)

    def visit_string_less_equal(self, operator: StringLessEqual):
        self._visit_operator(operator, 2)

    def visit_string_prefix_of(self, operator: StringPrefixOf):
        self._visit_operator(operator, 2)

    def visit_string_suffix_of(self, operator: StringSuffixOf):
        self._visit_operator(operator, 2)

    def visit_string_contains(self, operator: StringContains):
        self._visit_operator(operator, 2)

    def visit_boolean_variable(self, operator: BooleanVariable):
        self._visit_variable(operator)

    def visit_boolean_constant(self, operator: BooleanConstant):
        self._visit_constant(operator)

    def visit_boolean_literal(self, operator: BooleanLiteral):
        pass

    def visit_boolean_equality(self, operator: BooleanEquality):
        if isinstance(operator.operator_1, BooleanVariable):
            operator.operator_1.name = self.out_variable
        else:
            operator.operator_1.accept(self)

        operator.operator_2.accept(self)
        self._reset()

    def visit_integer_negation(self, operator: IntegerNegation):
        self._visit_operator(operator, 1)

    def visit_integer_addition(self, operator: IntegerAddition):
        self._visit_operator(operator, 2)

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        self._visit_operator(operator, 2)

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        self._visit_operator(operator, 2)

    def visit_integer_division(self, operator: IntegerDivision):
        self._visit_operator(operator, 2)

    def visit_bit_vector_to_integer(self, operator: BitVectorToInteger):
        self._visit_operator(operator, 1)

    def visit_string_to_integer(self, operator: StringToInteger):
        self._visit_operator(operator, 1)

    def visit_string_to_integer_built_in(self, operator: StringToIntegerBuiltIn):
        self._visit_operator(operator, 1)

    def visit_integer_ite(self, operator: IntegerIte):
        self._visit_ite(operator, INTEGER)

    def visit_string_length(self, operator: StringLength):
        self._visit_operator(operator, 1)

    def visit_string_index_of(self, operator: StringIndexOf):
        self._visit_operator(operator, 3)

    def visit_integer_variable(self, operator: IntegerVariable):
        self._visit_variable(operator)

    def visit_integer_constant(self, operator: IntegerConstant):
        self._visit_constant(operator)

    def visit_integer_literal(self, operator: IntegerLiteral):
        pass

    def visit_integer_equality(self, operator: IntegerEquality):
        if isinstance(operator.operator_1, IntegerVariable):
            operator.operator_1.name = self.out_variable
        else:
            operator.operator_1.accept(self)

        operator.operator_2.accept(self)
        self._reset()

    def visit_real_negation(self, operator: RealNegation):
        self._visit_operator(operator, 1)

    def visit_real_addition(self, operator: RealAddition):
        self._visit_operator(operator, 2)

    def visit_real_subtraction(self, operator: RealSubtraction):
        self._visit_operator(operator, 2)

    def visit_real_multiplication(self, operator: RealMultiplication):
        self._visit_operator(operator, 2)

    def visit_real_division(self, operator: RealDivision):
        self._visit_operator(operator, 2)

    def visit_real_ite(self, operator: RealIte):
        self._visit_ite(operator, REAL)

    def visit_integer_to_real(self, operator: IntegerToReal):
        self._visit_operator(operator, 1)

    def visit_real_variable(self, operator: RealVariable):
        self._visit_variable(operator)

    def visit_real_constant(self, operator: RealConstant):
        self._visit_constant(operator)

    def visit_real_literal(self, operator: RealLiteral):
        pass

    def visit_real_equality(self, operator: RealEquality):
        if isinstance(operator.operator_1, RealVariable):
            operator.operator_1.name = self.out_variable
        else:
            operator.operator_1.accept(self)

        operator.operator_2.accept(self)
        self._reset()

    def _visit_string_concatenation(self, operator: StringOperator):
        self._visit_operator(operator, 2)

    def visit_string_concatenation1n1(self, operator: StringConcatenation1n1):
        self._visit_string_concatenation(operator)

    def visit_string_concatenation1n2(self, operator: StringConcatenation1n2):
        self._visit_string_concatenation(operator)

    def visit_string_concatenation1n3(self, operator: StringConcatenation1n3):
        self._visit_string_concatenation(operator)

    def visit_string_concatenation2n1(self, operator: StringConcatenation2n1):
        self._visit_string_concatenation(operator)

    def visit_string_concatenation2n2(self, operator: StringConcatenation2n2):
        self._visit_string_concatenation(operator)

    def visit_string_concatenation2n3(self, operator: StringConcatenation2n3):
        self._visit_string_concatenation(operator)

    def visit_integer_to_string(self, operator: IntegerToString):
        self._visit_operator(operator, 1)

    def visit_string_from_integer_built_in(self, operator: StringFromIntegerBuiltIn):
        self._visit_operator(operator, 1)

    def visit_string_at(self, operator: StringAt):
        self._visit_operator(operator, 2)

    def visit_string_ite(self, operator: StringIte):
        self._visit_ite(operator, STRING)

    def visit_string_replacement(self, operator: StringReplacement):
        self._visit_operator(operator, 3)

    def visit_real_to_integer(self, operator: RealToInteger):
        self._visit_operator(operator, 1)

    def visit_substring(self, operator: Substring):
        self._visit_operator(operator, 3)

    def visit_string_variable(self, operator: StringVariable):
        self._visit_variable(operator)

    def visit_string_constant(self, operator: StringLiteral):
        self._visit_constant(operator)

    def visit_string_literal(self, operator: StringConstant):
        pass

    def visit_string_equality(self, operator: StringEquality):
        if isinstance(operator.operator_1, StringVariable):
            operator.operator_1.name = self.out_variable
        else:
            operator.operator_1.accept(self)

        operator.operator_2.accept(self)
        self._reset()

    def visit_bit_vector_not(self, operator: BitVectorNot):
        if operator in self._size:
            operator.size = self._size[operator]
            self._size[operator.operator_1] = self._size[operator]
            self._visit_operator(operator, 1)
        else:
            self._visit_operator(operator, 1)
            operator.size = operator.operator_1.size
            self._is_var[operator] = self._is_var[operator.operator_1]

    def visit_bit_vector_negation(self, operator: BitVectorNegation):
        if operator in self._size:
            operator.size = self._size[operator]
            self._size[operator.operator_1] = operator.size
            self._visit_operator(operator, 1)
        else:
            self._visit_operator(operator, 1)
            operator.size = operator.operator_1.size
            self._is_var[operator] = self._is_var[operator.operator_1]

    def visit_bit_vector_xor(self, operator: BitVectorXor):
        if operator in self._size:
            operator.size = self._size[operator]
            self._size[operator.operator_1] = operator.size
            self._size[operator.operator_2] = operator.size
            self._visit_operator(operator, 2)
        else:
            self._visit_operator(operator, 2)
            operator.size = max(
                [operator.operator_1.size, operator.operator_2.size])
            self._is_var[operator] = self._is_var[operator.operator_1] and self._is_var[operator.operator_2]

    def visit_bit_vector_concatenation(self, operator: BitVectorConcatenation):
        if operator in self._size:
            excess = self._size[operator] - operator.size
            left_is_var = self._is_var[operator.operator_1]
            right_is_var = self._is_var[operator.operator_2]
            if left_is_var and right_is_var:
                excess_1 = excess * round(random.random())
            elif not left_is_var and not right_is_var:
                excess_1 = random.randint(0, excess)
            else:
                excess_1 = excess * int(right_is_var)
            excess_2 = excess - excess_1
            self._size[operator.operator_1] = operator.operator_1.size + excess_1
            self._size[operator.operator_2] = operator.operator_2.size + excess_2
            self._visit_operator(operator, 2)
        else:
            self._visit_operator(operator, 2)
            operator.size = operator.operator_1.size + operator.operator_2.size
            self._is_var[operator] = self._is_var[operator.operator_1] and self._is_var[operator.operator_2]

    def visit_integer_to_bit_vector(self, operator: IntegerToBitVector):
        if operator in self._size:
            operator.size = self._size[operator]
        self._visit_operator(operator, 1)

    def visit_bit_vector_ite(self, operator: BitVectorIte):
        if operator in self._size:
            operator.size = self._size[operator]
            self._size[operator.operator_1] = operator.size
            self._size[operator.operator_2] = operator.size
            self._visit_ite(operator, BITVECTOR)
        else:
            self._visit_ite(operator, BITVECTOR)
            operator.size = max(
                [operator.operator_1.size, operator.operator_2.size])
            self._is_var[operator] = self._is_var[operator.operator_1] and self._is_var[operator.operator_2]

    def visit_bit_vector_extraction(self, operator: BitVectorExtraction):
        # operator_2 and operator_3 of type IntegerLiteral
        output_size = operator.operator_3.value - operator.operator_2.value + 1

        if operator in self._size:
            excess = self._size[operator] - operator.size
            if excess > 0:
                operator.size += excess
                operator.operator_3.value += excess

            self._size[operator.operator_1] = max(
                operator.operator_1.size, output_size)
            self._visit_operator(operator, 3)
        else:
            self._visit_operator(operator, 3)
            operator.size = output_size
            self._is_var[operator] = self._is_var[operator.operator_1]

    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        if operator in self._size:
            excess = self._size[operator] - operator.size
            if excess > 0:
                # transfer to new variable
                var = BitVectorVariable()
                var.__dict__ = operator.__dict__.copy()
                # define new constant
                const = BitVectorConstant()
                const.accept(self)
                const.size = excess
                # convert to concatenation
                concat = BitVectorConcatenation(var, const)
                operator.__class__ = concat.__class__
                operator.__dict__ = concat.__dict__
                operator.size = self._size[operator]
        else:
            self._visit_variable(operator)
            operator.size = random.choice([1, 8, 16, 20, 32, 64])
            self._is_var[operator] = True

    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        if operator in self._size:
            operator.size = self._size[operator]
        else:
            self._visit_constant(operator)
            operator.size = random.randint(1, 64)
            self._is_var[operator] = False

    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        if operator in self._size:
            excess = self._size[operator] - operator.size
            if excess > 0:
                operator.value = excess * [0] + operator.value
                operator.size = self._size[operator]
        else:
            operator.size = len(operator.value)
            self._is_var[operator] = False

    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        # initially, find minimum viable assignment
        operator.operator_2.accept(self)
        if isinstance(operator.operator_1, BitVectorVariable):
            operator.operator_1.name = self.out_variable
            operator.operator_1.size = operator.operator_2.size
            self._is_var[operator.operator_1] = False  # only in-vars relevant
        else:
            operator.operator_1.accept(self)

        operator.size = max(
            [operator.operator_1.size, operator.operator_2.size])

        # propagate size through tree
        self._size[operator.operator_1] = operator.size
        self._size[operator.operator_2] = operator.size
        self._visit_operator(operator, 2)
        self._reset()

    def _visit_operator(self, operator, arity):
        for i in range(arity):
            getattr(operator, f"operator_{i + 1}").accept(self)

    def _visit_variable(self, operator):
        operator.name = self.in_variables[self._var_idx]
        self._var_idx += 1

    def _visit_constant(self, operator):
        operator.name = f"c{self._const_idx}"
        self._const_idx += 1

    def _visit_ite(self, operator: Operator, param_type):
        # Set the fringe operator to be used as condition
        fringe_operators = get_fringe_operators(BOOLEAN, 2, [param_type])
        op_name = random.choice(fringe_operators)
        op = get_operator_class(BOOLEAN, op_name)(operator.operator_1, operator.operator_2)
        operator.fringe_operator_1 = op
        self._visit_operator(operator, 2)
