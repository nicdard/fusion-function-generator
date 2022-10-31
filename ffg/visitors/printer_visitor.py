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


class PrinterVisitor(BooleanVisitor, IntegerVisitor, RealVisitor, StringVisitor, BitVectorVisitor):
    class CompoundError(NotImplementedError):
        def __init__(self):
            msg = "Compound operation cannot be expressed in SMT syntax. Use CompoundVisitor for expansion."
            super().__init__(msg)

    def visit_boolean_xor(self, operator: BooleanXor):
        return f"(xor {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_boolean_not(self, operator: BooleanNot):
        return f"(not {operator.operator_1.accept(self)})"

    def visit_boolean_ite(self, operator: BooleanIte):
        return self._visit_ite(operator)

    def visit_boolean_or(self, operator: BooleanOr):
        return f"(or {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_boolean_and(self, operator: BooleanAnd):
        return f"(and {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_boolean_implies(self, operator: BooleanImplies):
        return f"(=> {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_boolean_distinct(self, operator: BooleanDistinct):
        return f"(distinct {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_distinct(self, operator: IntegerDistinct):
        return f"(distinct {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_distinct(self, operator: RealDistinct):
        return f"(distinct {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_distinct(self, operator: StringDistinct):
        return f"(distinct {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_bit_vector_distinct(self, operator: BitVectorDistinct):
        return f"(distinct {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_less(self, operator: IntegerLess):
        return f"(< {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_less_or_equal(self, operator: IntegerLessOrEqual):
        return f"(<= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_greater(self, operator: IntegerGreater):
        return f"(> {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_greater_or_equal(self, operator: IntegerGreaterOrEqual):
        return f"(>= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_less(self, operator: RealLess):
        return f"(< {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_less_or_equal(self, operator: RealLessOrEqual):
        return f"(<= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_greater(self, operator: RealGreater):
        return f"(> {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_greater_or_equal(self, operator: RealGreaterOrEqual):
        return f"(>= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_less(self, operator: StringLess):
        return f"(< {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_less_equal(self, operator: StringLessEqual):
        return f"(<= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_prefix_of(self, operator: StringPrefixOf):
        return f"(str.prefixof {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_suffix_of(self, operator: StringSuffixOf):
        return f"(str.suffixof {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_string_contains(self, operator: StringContains):
        return f"(str.contains {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_boolean_constant(self, operator: BooleanConstant):
        return operator.name

    def visit_boolean_variable(self, operator: BooleanVariable):
        return operator.name

    def visit_boolean_literal(self, operator: BooleanLiteral):
        return str(operator.value).lower()

    def visit_boolean_equality(self, operator: BooleanEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_negation(self, operator: IntegerNegation):
        return f"(- {operator.operator_1.accept(self)})"

    def visit_integer_addition(self, operator: IntegerAddition):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_integer_division(self, operator: IntegerDivision):
        return f"(div {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_bit_vector_to_integer(self, operator: BitVectorToInteger):
        return f"(bv2nat {operator.operator_1.accept(self)})"

    def visit_string_to_integer(self, operator: StringToInteger):
        raise self.CompoundError()

    def visit_string_to_integer_built_in(self, operator: StringToIntegerBuiltIn):
        return f"(str.to_int {operator.operator_1.accept(self)})"

    def visit_integer_ite(self, operator: IntegerIte):
        return self._visit_ite(operator)

    def visit_integer_constant(self, operator: IntegerConstant):
        return operator.name

    def visit_integer_variable(self, operator: IntegerVariable):
        return operator.name

    def visit_integer_literal(self, operator: IntegerLiteral):
        return str(operator.value)

    def visit_integer_equality(self, operator: IntegerEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_negation(self, operator: RealNegation):
        return f"(- {operator.operator_1.accept(self)})"

    def visit_real_addition(self, operator: RealAddition):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_subtraction(self, operator: RealSubtraction):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_multiplication(self, operator: RealMultiplication):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_division(self, operator: RealDivision):
        return f"(/ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visit_real_ite(self, operator: RealIte):
        return self._visit_ite(operator)

    def visit_integer_to_real(self, operator: IntegerToReal):
        return f"(to_real {operator.operator_1.accept(self)})"

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

    def visit_string_ite(self, operator: StringIte):
        return self._visit_ite(operator)

    def visit_string_length(self, operator: StringLength):
        return f"(str.len {operator.operator_1.accept(self)})"

    def visit_string_index_of(self, operator: StringIndexOf):
        return f"(str.indexof {operator.operator_1.accept(self)} " \
               f"{operator.operator_2.accept(self)} {operator.operator_3.accept(self)})"

    def visit_real_to_integer(self, operator: RealToInteger):
        return f"(to_int {operator.operator_1.accept(self)})"

    def visit_substring(self, operator: Substring):
        return f"(str.substr {operator.operator_1.accept(self)} " \
               f"{operator.operator_2.accept(self)} {operator.operator_3.accept(self)})"

    def visit_string_replacement(self, operator: StringReplacement):
        return f"(str.replace {operator.operator_1.accept(self)} " \
               f"{operator.operator_2.accept(self)} {operator.operator_3.accept(self)})"

    def visit_integer_to_string(self, operator: IntegerToString):
        raise self.CompoundError()

    def visit_string_from_integer_built_in(self, operator: StringFromIntegerBuiltIn):
        return f"(str.from_int {operator.operator_1.accept(self)})"

    def visit_string_at(self, operator: StringAt):
        return f"(str.at {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

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

    def visit_integer_to_bit_vector(self, operator: IntegerToBitVector):
        return f"((_ nat2bv {operator.size}) {operator.operator_1.accept(self)})"

    def visit_bit_vector_ite(self, operator: BitVectorIte):
        return self._visit_ite(operator)

    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        return operator.name

    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        return operator.name

    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        return f"#b{''.join([str(bit) for bit in operator.value])}"

    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def _visit_ite(self, operator):
        condition = (operator.fringe_operator_1.accept(self))
        return f"(ite {condition} {operator.operator_1.accept(self)} " + \
            f"{operator.operator_2.accept(self)})"
