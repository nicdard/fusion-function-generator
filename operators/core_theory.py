from operators.generic import Operator, OutputVariable
from abc import abstractmethod
from typing import List, Dict


class BooleanOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: 'BooleanOperator') -> Dict[str, 'BooleanOperator']:
        return {}


class XOR(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def invert(self, output: BooleanOperator) -> Dict[str, BooleanOperator]:
        inverse_1 = self.operator_1.invert(XOR(self.operator_2, output))
        inverse_2 = self.operator_2.invert(XOR(self.operator_1, output))
        return inverse_1 | inverse_2

    def __str__(self):
        return f"(xor {self.operator_1} {self.operator_2})"


class NOT(BooleanOperator):
    def __init__(self, input_1: BooleanOperator):
        self.operator_1 = input_1

    def invert(self, output: BooleanOperator) -> Dict[str, BooleanOperator]:
        return self.operator_1.invert(NOT(output))

    def __str__(self):
        return f"(not {self.operator_1})"


class BooleanVariable(BooleanOperator):
    def __init__(self, name: str):
        self.name = name

    def invert(self, output: BooleanOperator) -> Dict[str, BooleanOperator]:
        return {self.name: output}

    def __str__(self):
        return self.name


class BooleanConstant(BooleanOperator):
    def __init__(self, value: bool):
        self.value = value

    def invert(self, output: BooleanOperator) -> Dict[str, BooleanOperator]:
        return {}

    def __str__(self):
        return "true" if self.value else "false"


class BooleanOutputVariable(OutputVariable):
    def __init__(self, operator: BooleanOperator, name: str):
        self.name = name
        self.operator = operator

    def invert(self) -> List['BooleanOutputVariable']:
        inverse_dict = self.operator.invert(BooleanVariable(self.name))
        return [BooleanOutputVariable(operator, name) for name, operator in inverse_dict.items()]

    def __str__(self):
        return f"(= {self.name} {self.operator})"
