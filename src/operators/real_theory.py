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
from src.operators.generic import RealOperator


class RealAddition(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_addition(self)


class RealSubtraction(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_subtraction(self)


class RealMultiplication(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_multiplication(self)


class RealDivision(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_division(self)


class RealVariable(RealOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_variable(self)


class RealConstant(RealOperator):
    def __init__(self, name: str):
        self.name = name
        self.value = random.random() * 1000

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_constant(self)


class RealEquality(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_equality(self)


class RealVisitor(ABC):
    @abstractmethod
    def visit_real_addition(self, operator: RealAddition):
        pass

    @abstractmethod
    def visit_real_subtraction(self, operator: RealSubtraction):
        pass

    @abstractmethod
    def visit_real_multiplication(self, operator: RealMultiplication):
        pass

    @abstractmethod
    def visit_real_division(self, operator: RealDivision):
        pass

    @abstractmethod
    def visit_real_variable(self, operator: RealVariable):
        pass

    @abstractmethod
    def visit_real_constant(self, operator: RealConstant):
        pass

    @abstractmethod
    def visit_real_equality(self, operator: RealEquality):
        pass
