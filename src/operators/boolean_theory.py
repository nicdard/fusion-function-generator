# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

import random
from abc import ABC, abstractmethod
from src.operators.generic import BooleanOperator


class BooleanXor(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'BooleanXor'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_xor(self)


class BooleanNot(BooleanOperator):
    def __init__(self, input_1: BooleanOperator):
        self.operator_1 = input_1

    def __eq__(self, other: 'BooleanNot'):
        return \
            self.operator_1 == other.operator_1

    def __hash__(self):
       return hash(str(self))

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_not(self)


class BooleanVariable(BooleanOperator):
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: 'BooleanVariable'):
        return self.name == other.name

    def __hash__(self):
       return hash(self.name)

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_variable(self)


class BooleanConstant(BooleanOperator):
    def __init__(self, name: str):
        self.name = name
        self.value = random.random() > 0.5

    def __eq__(self, other: 'BooleanConstant'):
        return self.name == other.name

    def __hash__(self):
       return hash(self.name)

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_constant(self)


class BooleanEquality(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __eq__(self, other: 'BooleanEquality'):
        return \
            self.operator_1 == other.operator_1 and \
            self.operator_2 == other.operator_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_equality(self)


class BooleanVisitor(ABC):
    @abstractmethod
    def visit_boolean_xor(self, operator: BooleanXor):
        pass

    @abstractmethod
    def visit_boolean_not(self, operator: BooleanNot):
        pass

    @abstractmethod
    def visit_boolean_variable(self, operator: BooleanVariable):
        pass

    @abstractmethod
    def visit_boolean_constant(self, operator: BooleanConstant):
        pass

    @abstractmethod
    def visit_boolean_equality(self, operator: BooleanEquality):
        pass
