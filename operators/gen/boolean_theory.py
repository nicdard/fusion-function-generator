# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.
import random
from abc import ABC, abstractmethod
from operators.gen.generic import BooleanOperator


class BooleanXOR(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanXOR(self)


class BooleanNOT(BooleanOperator):
    def __init__(self, input_1: BooleanOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanNOT(self)


class BooleanConstant(BooleanOperator):
    def __init__(self):
        self.value = random.random() > 0.5

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanConstant(self)


class BooleanVariable(BooleanOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanVariable(self)


class BooleanEquality(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanEquality(self)


class BooleanVisitor(ABC):
    @abstractmethod
    def visitBooleanXOR(self, operator: BooleanXOR):
        pass

    @abstractmethod
    def visitBooleanNOT(self, operator: BooleanNOT):
        pass

    @abstractmethod
    def visitBooleanConstant(self, operator: BooleanConstant):
        pass

    @abstractmethod
    def visitBooleanVariable(self, operator: BooleanVariable):
        pass

    @abstractmethod
    def visitBooleanEquality(self, operator: BooleanEquality):
        pass
