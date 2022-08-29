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


from ffg.operators.boolean_theory import *
from ffg.operators.integer_theory import *
from ffg.operators.real_theory import *
from ffg.operators.string_theory import *
from ffg.operators.bitvector_theory import *


class VariableVisitor(BooleanVisitor, IntegerVisitor, RealVisitor, StringVisitor, BitVectorVisitor):
    def visit_boolean_not(self, operator: BooleanNot):
        return self._visit_operator(operator, 1)

    def visit_boolean_xor(self, operator: BooleanXor):
        return self._visit_operator(operator, 2)

    def visit_boolean_variable(self, operator: BooleanVariable):
        return {operator.name: "Bool"}

    def visit_boolean_constant(self, operator: BooleanConstant):
        return {}

    def visit_boolean_literal(self, operator: BooleanLiteral):
        return {}

    def visit_boolean_equality(self, operator: BooleanEquality):
        return self._visit_operator(operator, 2)

    def visit_integer_negation(self, operator: IntegerNegation):
        return self._visit_operator(operator, 1)

    def visit_integer_addition(self, operator: IntegerAddition):
        return self._visit_operator(operator, 2)

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return self._visit_operator(operator, 2)

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return self._visit_operator(operator, 2)

    def visit_integer_division(self, operator: IntegerDivision):
        return self._visit_operator(operator, 2)

    def visit_integer_variable(self, operator: IntegerVariable):
        return {operator.name: "Int"}

    def visit_integer_constant(self, operator: IntegerConstant):
        return {}

    def visit_integer_literal(self, operator: IntegerLiteral):
        return {}

    def visit_integer_equality(self, operator: IntegerEquality):
        return self._visit_operator(operator, 2)

    def visit_real_negation(self, operator: RealNegation):
        return self._visit_operator(operator, 1)

    def visit_real_addition(self, operator: RealAddition):
        return self._visit_operator(operator, 2)

    def visit_real_subtraction(self, operator: RealSubtraction):
        return self._visit_operator(operator, 2)

    def visit_real_multiplication(self, operator: RealMultiplication):
        return self._visit_operator(operator, 2)

    def visit_real_division(self, operator: RealDivision):
        return self._visit_operator(operator, 2)

    def visit_integer_to_real(self, operator: IntegerToReal):
        return self._visit_operator(operator, 1)

    def visit_real_variable(self, operator: RealVariable):
        return {operator.name: "Real"}

    def visit_real_constant(self, operator: RealConstant):
        return {}

    def visit_real_literal(self, operator: RealLiteral):
        return {}

    def visit_real_equality(self, operator: RealEquality):
        return self._visit_operator(operator, 2)

    def _visit_string_concatenation(self, operator: StringOperator):
        return self._visit_operator(operator, 2)

    def visit_string_concatenation1n1(self, operator: StringConcatenation1n1):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation1n2(self, operator: StringConcatenation1n2):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation1n3(self, operator: StringConcatenation1n3):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2n1(self, operator: StringConcatenation2n1):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2n2(self, operator: StringConcatenation2n2):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2n3(self, operator: StringConcatenation2n3):
        return self._visit_string_concatenation(operator)

    def visit_string_length(self, operator: StringLength):
        return operator.operator_1.accept(self)

    def visit_string_indexof(self, operator: StringIndexof):
        return self._visit_operator(operator, 3)

    def visit_real_to_integer(self, operator: RealToInteger):
        return self._visit_operator(operator, 1)

    def visit_substring(self, operator: Substring):
        return self._visit_operator(operator, 3)

    def visit_string_replacement(self, operator: StringReplacement):
        return self._visit_operator(operator, 3)

    def visit_string_variable(self, operator: StringVariable):
        return {operator.name: "String"}

    def visit_string_constant(self, operator: StringLiteral):
        return {}

    def visit_string_literal(self, operator: StringLiteral):
        return {}

    def visit_string_equality(self, operator: StringEquality):
        return self._visit_operator(operator, 2)

    def visit_bit_vector_not(self, operator: BitVectorNot):
        return self._visit_operator(operator, 1)

    def visit_bit_vector_negation(self, operator: BitVectorNegation):
        return self._visit_operator(operator, 1)

    def visit_bit_vector_xor(self, operator: BitVectorXor):
        return self._visit_operator(operator, 2)

    def visit_bit_vector_concatenation(self, operator: BitVectorConcatenation):
        return self._visit_operator(operator, 2)

    def visit_bit_vector_extraction(self, operator: BitVectorExtraction):
        return self._visit_operator(operator, 3)

    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        return {operator.name: f"(_ BitVec {operator.size})"}

    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        return {}

    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        return {}

    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        return self._visit_operator(operator, 2)

    def _visit_operator(self, operator, arity):
        out = dict()
        for i in range(arity):
            op_out = getattr(operator, f'operator_{i + 1}').accept(self)
            out.update(op_out)
        return out
