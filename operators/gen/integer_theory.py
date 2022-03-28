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

class IntegerAddition(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerAddition(self)

class IntegerSubtraction(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerSubtraction(self)

class IntegerMultiplication(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerMultiplication(self)

class IntegerDivision(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerDivision(self)

class IntegerConstant(IntegerOperator):
    def __init__(self, value: int):
        self.value = value

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerConstant(self)

class IntegerVariable(IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerVariable(self)

class IntegerEquality(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'IntegerVisitor'):
        return visitor.visitIntegerEquality(self)


class IntegerVisitor(ABC):
    @abstractmethod
    def visitIntegerAddition(self, operator: IntegerAddition):
        pass

    @abstractmethod
    def visitIntegerSubtraction(self, operator: IntegerSubtraction):
        pass

    @abstractmethod
    def visitIntegerMultiplication(self, operator: IntegerMultiplication):
        pass

    @abstractmethod
    def visitIntegerDivision(self, operator: IntegerDivision):
        pass

    @abstractmethod
    def visitIntegerConstant(self, operator: IntegerConstant):
        pass

    @abstractmethod
    def visitIntegerVariable(self, operator: IntegerVariable):
        pass

    @abstractmethod
    def visitIntegerEquality(self, operator: IntegerEquality):
        pass