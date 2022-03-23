from operators.generic import _Operator, OutputVariable
from abc import abstractmethod
from typing import Dict, List


class _RealOperator(_Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: '_RealOperator') -> Dict[str, '_RealOperator']:
        return {}


class RealAddition(_RealOperator):
    def __init__(self, input_1: _RealOperator, input_2: _RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(+ {self.operator_1} {self.operator_2})"

    def invert(self, output: _RealOperator) -> Dict[str, _RealOperator]:
        inverse_1 = self.operator_1.invert(RealSubtraction(output, self.operator_2))
        inverse_2 = self.operator_2.invert(RealSubtraction(output, self.operator_1))
        return inverse_1 | inverse_2


class RealSubtraction(_RealOperator):
    def __init__(self, input_1: _RealOperator, input_2: _RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(- {self.operator_1} {self.operator_2})"

    def invert(self, output: _RealOperator) -> Dict[str, _RealOperator]:
        inverse_1 = self.operator_1.invert(RealAddition(output, self.operator_2))
        inverse_2 = self.operator_2.invert(RealSubtraction(self.operator_1, output))
        return inverse_1 | inverse_2


class RealMultiplication(_RealOperator):
    def __init__(self, input_1: _RealOperator, input_2: _RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(* {self.operator_1} {self.operator_2})"

    def invert(self, output: _RealOperator) -> Dict[str, _RealOperator]:
        inverse_1 = self.operator_1.invert(RealDivision(output, self.operator_2))
        inverse_2 = self.operator_2.invert(RealDivision(output, self.operator_1))
        return inverse_1 | inverse_2


class RealDivision(_RealOperator):
    def __init__(self, input_1: _RealOperator, input_2: _RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(div {self.operator_1} {self.operator_2})"

    def invert(self, output: _RealOperator) -> Dict[str, _RealOperator]:
        inverse_1 = self.operator_1.invert(RealMultiplication(output, self.operator_2))
        inverse_2 = self.operator_2.invert(RealDivision(self.operator_1, output))
        return inverse_1 | inverse_2


class RealVariable(_RealOperator):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def invert(self, output: _Operator) -> Dict[str, _RealOperator]:
        return {self.name: output}


class RealConstant(_RealOperator):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def invert(self, output: _Operator) -> Dict[str, _RealOperator]:
        return {}


class RealOutputVariable(OutputVariable):
    def __init__(self, operator: _RealOperator, name: str):
        self.name = name
        self.operator = operator

    def __repr__(self):
        return f"(= {self.name} {self.operator})"

    def invert(self) -> List['RealOutputVariable']:
        inverse_dict = self.operator.invert(RealVariable(self.name))
        return [RealOutputVariable(operator, name) for name, operator in inverse_dict.items()]
