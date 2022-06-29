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


from src.operators.boolean_theory import *
from src.operators.integer_theory import *
from src.operators.real_theory import *
from src.operators.string_theory import *
from src.operators.bitvector_theory import *


class PrinterVisitor(BooleanVisitor, IntegerVisitor, RealVisitor, StringVisitor, BitVectorVisitor):
    def visit_boolean_xor(self, operator: BooleanXor):
        return f"(xor {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_boolean_not(self, operator: BooleanNot):
        return f"(not {operator.operator_1.accept(self)})"

    def visit_boolean_constant(self, operator: BooleanConstant):
        return operator.name

    def visit_boolean_variable(self, operator: BooleanVariable):
        return operator.name

    def visit_boolean_literal(self, operator: BooleanLiteral):
        return str(operator.value).lower()

    def visit_boolean_equality(self, operator: BooleanEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_addition(self, operator: IntegerAddition):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_division(self, operator: IntegerDivision):
        return f"(div {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_constant(self, operator: IntegerConstant):
        return operator.name

    def visit_integer_variable(self, operator: IntegerVariable):
        return operator.name

    def visit_integer_literal(self, operator: IntegerLiteral):
        return str(operator.value)

    def visit_integer_equality(self, operator: IntegerEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_addition(self, operator: RealAddition):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_subtraction(self, operator: RealSubtraction):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_multiplication(self, operator: RealMultiplication):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_division(self, operator: RealDivision):
        return f"(/ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_constant(self, operator: RealConstant):
        return operator.name

    def visit_real_variable(self, operator: RealVariable):
        return operator.name

    def visit_real_literal(self, operator: RealLiteral):
        return str(operator.value)

    def visit_real_equality(self, operator: RealEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def _visit_string_concatenation(self, operator: StringOperator):
        return f"(str.++ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_concatenation1_1(self, operator: StringConcatenation1_1):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation1_2(self, operator: StringConcatenation1_2):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation1_3(self, operator: StringConcatenation1_3):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2_1(self, operator: StringConcatenation2_1):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2_2(self, operator: StringConcatenation2_2):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2_3(self, operator: StringConcatenation2_3):
        return self._visit_string_concatenation(operator)

    def visit_string_length(self, operator: StringLength):
        return f"(str.len {operator.operator_1.accept(self)})"

    def visit_string_indexof(self, operator: StringIndexof):
        return f"(str.indexof {operator.operator_1.accept(self)} " \
               f"{operator.operator_2.accept(self)} {operator.operator_3.accept(self)})"

    def visit_substring(self, operator: Substring):
        return f"(str.substr {operator.operator_1.accept(self)} " \
               f"{operator.operator_2.accept(self)} {operator.operator_3.accept(self)})"

    def visit_string_replacement(self, operator: StringReplacement):
        return f"(str.replace {operator.operator_1.accept(self)} " \
               f"{operator.operator_2.accept(self)} {operator.operator_3.accept(self)})"

    def visit_string_variable(self, operator: StringVariable):
        return operator.name

    def visit_string_constant(self, operator: StringLiteral):
        return operator.name

    def visit_string_literal(self, operator: StringLiteral):
        return f"\"{operator.value}\""

    def visit_string_equality(self, operator: StringEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_bit_vector_not(self, operator: BitVectorNot):
        return f"(bvnot {operator.operator_1.accept(self)})"

    def visit_bit_vector_negation(self, operator: BitVectorNegation):
        return f"(bvneg {operator.operator_1.accept(self)})"

    def visit_bit_vector_xor(self, operator: BitVectorXor):
        return f"(bvxor {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_bit_vector_concatenation(self, operator: BitVectorConcatenation):
        return f"(concat {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_bit_vector_extraction(self, operator: BitVectorExtraction):
        return f"((_ extract {operator.operator_3.accept(self)} {operator.operator_2.accept(self)}) " \
               f"{operator.operator_1.accept(self)})"

    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        return operator.name

    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        return operator.name

    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        return f"#b{''.join([str(bit) for bit in operator.value])}"

    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"
