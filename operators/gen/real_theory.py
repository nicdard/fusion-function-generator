# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.


from abc import ABC, abstractmethod
from operators.gen.generic import Operator


class RealOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def accept(self, visitor: 'RealVisitor'):
        pass

class RealAdditionOperator(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealAddition(self)

class RealSubtractionOperator(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealSubtraction(self)

class RealMultiplicationOperator(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealMultiplication(self)

class RealDivisionOperator(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealDivision(self)

class RealConstantOperator(RealOperator):
    def __init__(self, value: int):
        self.value = value

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealConstant(self)

class RealVariableOperator(RealOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealVariable(self)

class RealEqualityOperator(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealEquality(self)


class RealVisitor(ABC):
    @abstractmethod
    def visitRealAddition(self, operator: RealAdditionOperator):
        pass

    @abstractmethod
    def visitRealSubtraction(self, operator: RealSubtractionOperator):
        pass

    @abstractmethod
    def visitRealMultiplication(self, operator: RealMultiplicationOperator):
        pass

    @abstractmethod
    def visitRealDivision(self, operator: RealDivisionOperator):
        pass

    @abstractmethod
    def visitRealConstant(self, operator: RealConstantOperator):
        pass

    @abstractmethod
    def visitRealVariable(self, operator: RealVariableOperator):
        pass

    @abstractmethod
    def visitRealEquality(self, operator: RealEqualityOperator):
        pass
