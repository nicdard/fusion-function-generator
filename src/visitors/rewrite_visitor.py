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


class RewriteVisitor(BooleanVisitor, IntegerVisitor, RealVisitor, StringVisitor, BitVectorVisitor):
    def __init__(self):
        self.output = {}

    def visit_boolean_not(self, operator: BooleanNot):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanNot(output)
        return operator.operator_1.accept(self)

    def visit_boolean_xor(self, operator: BooleanXor):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanXor(operator.operator_2, output)
        self.output[operator.operator_2] = BooleanXor(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_boolean_constant(self, operator: BooleanConstant):
        return {}

    def visit_boolean_variable(self, operator: BooleanVariable):
        return {operator: self.output[operator]}

    def visit_boolean_literal(self, operator: BooleanLiteral):
        return {}

    def visit_boolean_equality(self, operator: BooleanEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        return [BooleanEquality(var, operator) for var, operator in inverse_dict.items()]

    def visit_integer_addition(self, operator: IntegerAddition):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerSubtraction(
            output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtraction(
            output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerAddition(
            output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtraction(
            operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerDivision(
            output, operator.operator_2)
        self.output[operator.operator_2] = IntegerDivision(
            output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_integer_division(self, operator: IntegerDivision):
        return {}

    def visit_integer_constant(self, operator: IntegerConstant):
        return {}

    def visit_integer_variable(self, operator: IntegerVariable):
        return {operator: self.output[operator]}

    def visit_integer_literal(self, operator: IntegerLiteral):
        return {}

    def visit_integer_equality(self, operator: IntegerEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {}
        return [IntegerEquality(var, operator) for var, operator in inverse_dict.items()]

    def visit_real_addition(self, operator: RealAddition):
        output = self.output[operator]
        self.output[operator.operator_1] = RealSubtraction(
            output, operator.operator_2)
        self.output[operator.operator_2] = RealSubtraction(
            output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_real_subtraction(self, operator: RealSubtraction):
        output = self.output[operator]
        self.output[operator.operator_1] = RealAddition(
            output, operator.operator_2)
        self.output[operator.operator_2] = RealSubtraction(
            operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_real_multiplication(self, operator: RealMultiplication):
        output = self.output[operator]
        self.output[operator.operator_1] = RealDivision(
            output, operator.operator_2)
        self.output[operator.operator_2] = RealDivision(
            output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_real_division(self, operator: RealDivision):
        output = self.output[operator]
        self.output[operator.operator_1] = RealMultiplication(
            output, operator.operator_2)
        self.output[operator.operator_2] = RealDivision(
            operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return {**inverse_1, **inverse_2}

    def visit_real_constant(self, operator: RealConstant):
        return {}

    def visit_real_variable(self, operator: RealVariable):
        return {operator: self.output[operator]}

    def visit_real_literal(self, operator: RealLiteral):
        return {}

    def visit_real_equality(self, operator: RealEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {}
        return [RealEquality(var, operator) for var, operator in inverse_dict.items()]

    def _visit_string_concatenation(self, operator: StringOperator, inv1: int, inv2: int):
        output = self.output[operator]

        def inv_1_rule_1():
            return Substring(output, IntegerLiteral(0), StringLength(operator.operator_1))

        def inv_1_rule_2():
            return Substring(output, IntegerLiteral(0),
                             StringIndexof(output, operator.operator_2, StringLength(operator.operator_1)))

        def inv_2_rule_1():
            return Substring(output, StringLength(operator.operator_1), StringLength(operator.operator_2))

        def inv_2_rule_2():
            return Substring(output,
                             StringIndexof(output, operator.operator_2, StringLength(
                                 operator.operator_1)),
                             StringLength(operator.operator_2))

        def inv_2_rule_3():
            return StringReplacement(output, operator.operator_1, StringLiteral(""))

        output_1 = [inv_1_rule_1, inv_1_rule_2][inv1 - 1]()
        output_2 = [inv_2_rule_1, inv_2_rule_2, inv_2_rule_3][inv2 - 1]()

        self.output[operator.operator_1] = output_1
        self.output[operator.operator_2] = output_2

        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)

        return {**inverse_1, **inverse_2}

    def visit_string_concatenation1_1(self, operator: StringConcatenation1_1):
        return self._visit_string_concatenation(operator, 1, 1)

    def visit_string_concatenation1_2(self, operator: StringConcatenation1_2):
        return self._visit_string_concatenation(operator, 1, 2)

    def visit_string_concatenation1_3(self, operator: StringConcatenation1_3):
        return self._visit_string_concatenation(operator, 1, 3)

    def visit_string_concatenation2_1(self, operator: StringConcatenation2_1):
        return self._visit_string_concatenation(operator, 2, 1)

    def visit_string_concatenation2_2(self, operator: StringConcatenation2_2):
        return self._visit_string_concatenation(operator, 2, 2)

    def visit_string_concatenation2_3(self, operator: StringConcatenation2_3):
        return self._visit_string_concatenation(operator, 2, 3)

    def visit_string_length(self, operator: StringLength):
        return {}

    def visit_string_indexof(self, operator: StringIndexof):
        return {}

    def visit_substring(self, operator: Substring):
        return {}

    def visit_string_replacement(self, operator: StringReplacement):
        return {}

    def visit_string_variable(self, operator: StringVariable):
        return {operator: self.output[operator]}

    def visit_string_constant(self, operator: StringLiteral):
        return {}

    def visit_string_literal(self, operator: StringLiteral):
        return {}

    def visit_string_equality(self, operator: StringEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {}
        return [StringEquality(var, operator) for var, operator in inverse_dict.items()]

    def visit_bit_vector_not(self, operator: BitVectorNot):
        output = self.output[operator]
        self.output[operator.operator_1] = BitVectorNot(output)
        self.output[operator.operator_1].size = output.size
        return operator.operator_1.accept(self)

    def visit_bit_vector_negation(self, operator: BitVectorNegation):
        output = self.output[operator]
        self.output[operator.operator_1] = BitVectorNegation(output)
        self.output[operator.operator_1].size = output.size
        return operator.operator_1.accept(self)

    def visit_bit_vector_xor(self, operator: BitVectorXor):
        output = self.output[operator]
        self.output[operator.operator_1] = BitVectorXor(operator.operator_2, output)
        self.output[operator.operator_1].size = output.size
        self.output[operator.operator_2] = BitVectorXor(operator.operator_1, output)
        self.output[operator.operator_2].size = output.size
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)}

    def visit_bit_vector_concatenation(self, operator: BitVectorConcatenation):
        output = self.output[operator]
        zero = IntegerLiteral(0)
        index_1 = IntegerLiteral(operator.operator_2.size - 1)
        index_2 = IntegerLiteral(operator.operator_2.size)
        index_3 = IntegerLiteral(output.size - 1)
        self.output[operator.operator_2] = BitVectorExtraction(output, zero, index_1)
        self.output[operator.operator_2].size = operator.operator_2.size
        self.output[operator.operator_1] = BitVectorExtraction(output, index_2, index_3)
        self.output[operator.operator_1].size = operator.operator_1.size
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)}

    def visit_bit_vector_extraction(self, operator: BitVectorExtraction):
        return {}

    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        return {operator: self.output[operator]}

    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        return {}

    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        return {}

    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {}
        return [BitVectorEquality(var, operator) for var, operator in inverse_dict.items()]
