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

class RealAddition(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealAddition(self)

class RealSubtraction(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealSubtraction(self)

class RealMultiplication(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealMultiplication(self)

class RealDivision(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealDivision(self)

class RealConstant(RealOperator):
    def __init__(self, value: int):
        self.value = value

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealConstant(self)

class RealVariable(RealOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealVariable(self)

class RealEquality(RealOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'RealVisitor'):
        return visitor.visitRealEquality(self)


class RealVisitor(ABC):
    @abstractmethod
    def visitRealAddition(self, operator: RealAddition):
        pass

    @abstractmethod
    def visitRealSubtraction(self, operator: RealSubtraction):
        pass

    @abstractmethod
    def visitRealMultiplication(self, operator: RealMultiplication):
        pass

    @abstractmethod
    def visitRealDivision(self, operator: RealDivision):
        pass

    @abstractmethod
    def visitRealConstant(self, operator: RealConstant):
        pass

    @abstractmethod
    def visitRealVariable(self, operator: RealVariable):
        pass

    @abstractmethod
    def visitRealEquality(self, operator: RealEquality):
        pass
