# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

import random
from abc import ABC, abstractmethod
from src.operators.generic import StringOperator, IntegerOperator


class StringConcatenation(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_concatenation(self)


class StringLength(IntegerOperator):
    def __init__(self, input_1: StringOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_length(self)


class Substring(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: IntegerOperator, input_3: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2
        self.operator_3 = input_3

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_substring(self)


class StringReplacement(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator, input_3: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2
        self.operator_3 = input_3

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_replacement(self)


class StringVariable(StringOperator):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_variable(self)


class StringLiteral(StringOperator):
    def __init__(self, name: str):
        self.name = name
        self.value = ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(0, 50))])

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_literal(self)


class StringEquality(StringOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'StringVisitor'):
        return visitor.visit_string_equality(self)


class StringVisitor(ABC):
    @abstractmethod
    def visit_string_concatenation(self, operator: StringConcatenation):
        pass

    @abstractmethod
    def visit_string_length(self, operator: StringLength):
        pass

    @abstractmethod
    def visit_substring(self, operator: Substring):
        pass

    @abstractmethod
    def visit_string_replacement(self, operator: StringReplacement):
        pass

    @abstractmethod
    def visit_string_variable(self, operator: StringVariable):
        pass

    @abstractmethod
    def visit_string_literal(self, operator: StringLiteral):
        pass

    @abstractmethod
    def visit_string_equality(self, operator: StringEquality):
        pass
