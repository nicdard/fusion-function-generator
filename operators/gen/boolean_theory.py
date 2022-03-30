# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.


from abc import ABC, abstractmethod
from operators.gen.generic import Operator


class BooleanOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def accept(self, visitor: 'BooleanVisitor'):
        pass

class BooleanXOROperator(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanXOR(self)

class BooleanNOTOperator(BooleanOperator):
    def __init__(self, input_1: BooleanOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanNOT(self)

class BooleanConstantOperator(BooleanOperator):
    def __init__(self, value: bool):
        self.value = value

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanConstant(self)

class BooleanVariableOperator(BooleanOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanVariable(self)

class BooleanEqualityOperator(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visitBooleanEquality(self)


class BooleanVisitor(ABC):
    @abstractmethod
    def visitBooleanXOR(self, operator: BooleanXOROperator):
        pass

    @abstractmethod
    def visitBooleanNOT(self, operator: BooleanNOTOperator):
        pass

    @abstractmethod
    def visitBooleanConstant(self, operator: BooleanConstantOperator):
        pass

    @abstractmethod
    def visitBooleanVariable(self, operator: BooleanVariableOperator):
        pass

    @abstractmethod
    def visitBooleanEquality(self, operator: BooleanEqualityOperator):
        pass
