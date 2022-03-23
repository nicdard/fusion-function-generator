from operators.generic import Operator, OutputVariable
from abc import abstractmethod
from typing import Dict, List


class IntegerOperator(Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: 'IntegerOperator') -> Dict[str, 'IntegerOperator']:
        return {}


class Addition(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def invert(self, output: IntegerOperator) -> Dict[str, IntegerOperator]:
        inverse_1 = self.operator_1.invert(Subtraction(output, self.operator_2))
        inverse_2 = self.operator_2.invert(Subtraction(output, self.operator_1))
        return inverse_1 | inverse_2

    def __str__(self):
        return f"(+ {self.operator_1} {self.operator_2})"


class Subtraction(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def invert(self, output: IntegerOperator) -> Dict[str, IntegerOperator]:
        inverse_1 = self.operator_1.invert(Addition(output, self.operator_2))
        inverse_2 = self.operator_2.invert(Subtraction(self.operator_1, output))
        return inverse_1 | inverse_2

    def __str__(self):
        return f"(- {self.operator_1} {self.operator_2})"


class Multiplication(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def invert(self, output: IntegerOperator) -> Dict[str, IntegerOperator]:
        inverse_1 = self.operator_1.invert(Division(output, self.operator_2))
        inverse_2 = self.operator_2.invert(Division(output, self.operator_1))
        return inverse_1 | inverse_2

    def __str__(self):
        return f"(* {self.operator_1} {self.operator_2})"


class Division(IntegerOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def invert(self, output: IntegerOperator) -> Dict[str, IntegerOperator]:
        inverse_1 = self.operator_1.invert(Multiplication(output, self.operator_2))
        inverse_2 = self.operator_2.invert(Division(self.operator_1, output))
        return inverse_1 | inverse_2

    def __str__(self):
        return f"(div {self.operator_1} {self.operator_2})"


class IntegerVariable(IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def invert(self, output: Operator) -> Dict[str, IntegerOperator]:
        return {self.name: output}

    def __str__(self):
        return self.name


class IntegerConstant(IntegerOperator):
    def __init__(self, value: int):
        self.value = value

    def invert(self, output: Operator) -> Dict[str, IntegerOperator]:
        return {}

    def __str__(self):
        return str(self.value)


class IntegerOutputVariable(OutputVariable):
    def __init__(self, operator: IntegerOperator, name: str):
        self.name = name
        self.operator = operator

    def invert(self) -> List['IntegerOutputVariable']:
        inverse_dict = self.operator.invert(IntegerVariable(self.name))
        return [IntegerOutputVariable(operator, name) for name, operator in inverse_dict.items()]

    def __str__(self):
        return f"(= {self.name} {self.operator})"
