# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

import random
from abc import ABC, abstractmethod
from src.operators.generic import RealOperator


class RealAddition(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'RealAddition'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_addition(self)


class RealSubtraction(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'RealSubtraction'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_subtraction(self)


class RealMultiplication(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'RealMultiplication'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_multiplication(self)


class RealDivision(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'RealDivision'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_division(self)


class RealVariable(RealOperator):
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: 'RealVariable'):
        return self.name == other.name

    def __hash__(self):
       return hash(self.name)

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_variable(self)


class RealConstant(RealOperator):
    def __init__(self, name: str):
        self.name = name
        self.value = random.random() * 1000

    def __eq__(self, other: 'RealConstant'):
        return self.name == other.name

    def __hash__(self):
       return hash(self.name)

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visit_real_constant(self)


class RealEquality(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'RealEquality'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

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
