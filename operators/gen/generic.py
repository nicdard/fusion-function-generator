# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.


from abc import ABC, abstractmethod


class Operator(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class BooleanOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class IntegerOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class RealOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass
