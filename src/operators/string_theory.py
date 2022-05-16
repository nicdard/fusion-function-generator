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

import random
from abc import ABC, abstractmethod
from src.operators.generic import StringOperator, IntegerOperator


class StringConcatenation(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation(self)


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


class StringVariable(StringOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_variable(self)


class StringLiteral(StringOperator):
    def __init__(self, name: str):
        self.name = name
        self.value = ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(0, 50))])

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
    def visit_string_concatenation(self, operator: StringConcatenation):
        pass

    @abstractmethod
    def visit_string_replacement(self, operator: StringReplacement):
        pass

    @abstractmethod
    def visit_substring(self, operator: Substring):
        pass

    @abstractmethod
    def visit_string_variable(self, operator: StringVariable):
        pass

    @abstractmethod
    def visit_string_literal(self, operator: StringLiteral):
        pass

    @abstractmethod
    def visit_string_equality(self, operator: StringEquality):
        pass
