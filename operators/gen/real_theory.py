# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.

import random
from abc import ABC, abstractmethod
from operators.gen.generic import RealOperator


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
    def __init__(self):
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

