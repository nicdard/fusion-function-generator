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
from ffg.operators.generic import IntegerOperator, StringOperator


class StringConcatenation1n1(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation1n1(self)


class StringConcatenation1n2(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation1n2(self)


class StringConcatenation1n3(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation1n3(self)


class StringConcatenation2n1(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation2n1(self)


class StringConcatenation2n2(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation2n2(self)


class StringConcatenation2n3(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation2n3(self)


class IntegerToString(StringOperator):
    def __init__(self, input_1: IntegerOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_integer_to_string(self)


class StringIte(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_ite(self)


class StringReplacement(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator, input_3: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2
        self.operator_3 = input_3

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_replacement(self)


class Substring(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: IntegerOperator, input_3: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2
        self.operator_3 = input_3

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_substring(self)


class StringFromIntegerBuiltIn(StringOperator):
    def __init__(self, input_1: IntegerOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_from_integer_built_in(self)


class StringAt(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_at(self)


class StringVariable(StringOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_variable(self)


class StringConstant(StringOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_constant(self)


class StringLiteral(StringOperator):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_literal(self)


class StringEquality(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_equality(self)


class StringVisitor(ABC):
    @abstractmethod
    def visit_string_concatenation1n1(self, operator: StringConcatenation1n1):
        pass

    @abstractmethod
    def visit_string_concatenation1n2(self, operator: StringConcatenation1n2):
        pass

    @abstractmethod
    def visit_string_concatenation1n3(self, operator: StringConcatenation1n3):
        pass

    @abstractmethod
    def visit_string_concatenation2n1(self, operator: StringConcatenation2n1):
        pass

    @abstractmethod
    def visit_string_concatenation2n2(self, operator: StringConcatenation2n2):
        pass

    @abstractmethod
    def visit_string_concatenation2n3(self, operator: StringConcatenation2n3):
        pass

    @abstractmethod
    def visit_integer_to_string(self, operator: IntegerToString):
        pass

    @abstractmethod
    def visit_string_ite(self, operator: StringIte):
        pass

    @abstractmethod
    def visit_string_replacement(self, operator: StringReplacement):
        pass

    @abstractmethod
    def visit_substring(self, operator: Substring):
        pass

    @abstractmethod
    def visit_string_from_integer_built_in(self, operator: StringFromIntegerBuiltIn):
        pass

    @abstractmethod
    def visit_string_at(self, operator: StringAt):
        pass

    @abstractmethod
    def visit_string_variable(self, operator: StringVariable):
        pass

    @abstractmethod
    def visit_string_constant(self, operator: StringConstant):
        pass

    @abstractmethod
    def visit_string_literal(self, operator: StringLiteral):
        pass

    @abstractmethod
    def visit_string_equality(self, operator: StringEquality):
        pass
