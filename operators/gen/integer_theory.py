# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

import random
from abc import ABC, abstractmethod
from operators.gen.generic import IntegerOperator


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


class IntegerVariable(IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_variable(self)


class IntegerConstant(IntegerOperator):
    def __init__(self):
        self.value = random.randint(0, 1000)

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_constant(self)


class IntegerEquality(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_equality(self)


class IntegerVisitor(ABC):
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
    def visit_integer_variable(self, operator: IntegerVariable):
        pass

    @abstractmethod
    def visit_integer_constant(self, operator: IntegerConstant):
        pass

    @abstractmethod
    def visit_integer_equality(self, operator: IntegerEquality):
        pass
