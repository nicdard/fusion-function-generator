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
from ffg.operators.generic import BooleanOperator


class BooleanNot(BooleanOperator):
    def __init__(self, input_1: BooleanOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_not(self)


class BooleanXor(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_xor(self)


class BooleanVariable(BooleanOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_variable(self)


class BooleanConstant(BooleanOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_constant(self)


class BooleanLiteral(BooleanOperator):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_literal(self)


class BooleanEquality(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_equality(self)


class BooleanVisitor(ABC):
    @abstractmethod
    def visit_boolean_not(self, operator: BooleanNot):
        pass

    @abstractmethod
    def visit_boolean_xor(self, operator: BooleanXor):
        pass

    @abstractmethod
    def visit_boolean_variable(self, operator: BooleanVariable):
        pass

    @abstractmethod
    def visit_boolean_constant(self, operator: BooleanConstant):
        pass

    @abstractmethod
    def visit_boolean_literal(self, operator: BooleanLiteral):
        pass

    @abstractmethod
    def visit_boolean_equality(self, operator: BooleanEquality):
        pass
