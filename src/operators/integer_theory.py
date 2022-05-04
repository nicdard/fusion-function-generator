# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

import random
from abc import ABC, abstractmethod
from src.operators.generic import IntegerOperator


class IntegerAddition(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'IntegerAddition'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_addition(self)


class IntegerSubtraction(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'IntegerSubtraction'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_subtraction(self)


class IntegerMultiplication(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'IntegerMultiplication'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_multiplication(self)


class IntegerDivision(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'IntegerDivision'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_division(self)


class IntegerVariable(IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: 'IntegerVariable'):
        return self.name == other.name

    def __hash__(self):
       return hash(self.name)

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_variable(self)


class IntegerConstant(IntegerOperator):
    def __init__(self, name: str):
        self.name = name
        self.value = random.randint(0, 1000)

    def __eq__(self, other: 'IntegerConstant'):
        return self.name == other.name

    def __hash__(self):
       return hash(self.name)

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visit_integer_constant(self)


class IntegerEquality(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'IntegerEquality'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

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
