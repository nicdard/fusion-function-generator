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


# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

from abc import ABC, abstractmethod
from src.operators.generic import IntegerOperator, RealOperator, StringOperator


class IntegerNegation(IntegerOperator):
    def __init__(self, input_1: IntegerOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_negation(self)


class IntegerAddition(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_addition(self)


class IntegerSubtraction(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_subtraction(self)


class IntegerMultiplication(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_multiplication(self)


class IntegerDivision(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_division(self)


class StringLength(IntegerOperator):
    def __init__(self, input_1: StringOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_string_length(self)


class StringIndexof(IntegerOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator, input_3: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2
        self.operator_3 = input_3

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_string_indexof(self)


class RealToInteger(IntegerOperator):
    def __init__(self, input_1: RealOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_real_to_integer(self)


class IntegerVariable(IntegerOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_variable(self)


class IntegerConstant(IntegerOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_constant(self)


class IntegerLiteral(IntegerOperator):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_literal(self)


class IntegerEquality(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_equality(self)


class IntegerVisitor(ABC):
    @abstractmethod
    def visit_integer_negation(self, operator: IntegerNegation):
        pass

    @abstractmethod
    def visit_integer_addition(self, operator: IntegerAddition):
        pass

    @abstractmethod
    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        pass

    @abstractmethod
    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        pass

    @abstractmethod
    def visit_integer_division(self, operator: IntegerDivision):
        pass

    @abstractmethod
    def visit_string_length(self, operator: StringLength):
        pass

    @abstractmethod
    def visit_string_indexof(self, operator: StringIndexof):
        pass

    @abstractmethod
    def visit_real_to_integer(self, operator: RealToInteger):
        pass

    @abstractmethod
    def visit_integer_variable(self, operator: IntegerVariable):
        pass

    @abstractmethod
    def visit_integer_constant(self, operator: IntegerConstant):
        pass

    @abstractmethod
    def visit_integer_literal(self, operator: IntegerLiteral):
        pass

    @abstractmethod
    def visit_integer_equality(self, operator: IntegerEquality):
        pass
