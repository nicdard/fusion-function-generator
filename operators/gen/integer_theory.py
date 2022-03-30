# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.


from abc import ABC, abstractmethod
from operators.gen.generic import Operator


class IntegerOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def accept(self, visitor: 'IntegerVisitor'):
        pass

class IntegerAdditionOperator(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerAddition(self)

class IntegerSubtractionOperator(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerSubtraction(self)

class IntegerMultiplicationOperator(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerMultiplication(self)

class IntegerDivisionOperator(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerDivision(self)

class IntegerConstantOperator(IntegerOperator):
    def __init__(self, value: int):
        self.value = value

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerConstant(self)

class IntegerVariableOperator(IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerVariable(self)

class IntegerEqualityOperator(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerEquality(self)


class IntegerVisitor(ABC):
    @abstractmethod
    def visitIntegerAddition(self, operator: IntegerAdditionOperator):
        pass

    @abstractmethod
    def visitIntegerSubtraction(self, operator: IntegerSubtractionOperator):
        pass

    @abstractmethod
    def visitIntegerMultiplication(self, operator: IntegerMultiplicationOperator):
        pass

    @abstractmethod
    def visitIntegerDivision(self, operator: IntegerDivisionOperator):
        pass

    @abstractmethod
    def visitIntegerConstant(self, operator: IntegerConstantOperator):
        pass

    @abstractmethod
    def visitIntegerVariable(self, operator: IntegerVariableOperator):
        pass

    @abstractmethod
    def visitIntegerEquality(self, operator: IntegerEqualityOperator):
        pass
