from operators.generic import _Operator, OutputVariable
from abc import abstractmethod
from typing import List, Dict


class _BooleanOperator(_Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: '_BooleanOperator') -> Dict[str, '_BooleanOperator']:
        return {}


class XOR(_BooleanOperator):
    def __init__(self, input_1: _BooleanOperator, input_2: _BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(xor {self.operator_1} {self.operator_2})"

    def invert(self, output: _BooleanOperator) -> Dict[str, _BooleanOperator]:
        inverse_1 = self.operator_1.invert(XOR(self.operator_2, output))
        inverse_2 = self.operator_2.invert(XOR(self.operator_1, output))
        return inverse_1 | inverse_2


class NOT(_BooleanOperator):
    def __init__(self, input_1: _BooleanOperator):
        self.operator_1 = input_1

    def __repr__(self):
        return f"(not {self.operator_1})"

    def invert(self, output: _BooleanOperator) -> Dict[str, _BooleanOperator]:
        return self.operator_1.invert(NOT(output))


class BooleanVariable(_BooleanOperator):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def invert(self, output: _BooleanOperator) -> Dict[str, _BooleanOperator]:
        return {self.name: output}


class BooleanConstant(_BooleanOperator):
    def __init__(self, value: bool):
        self.value = value

    def __repr__(self):
        return str(bool).lower()

    def invert(self, output: _BooleanOperator) -> Dict[str, _BooleanOperator]:
        return {}


class BooleanOutputVariable(OutputVariable):
    def __init__(self, operator: _BooleanOperator, name: str):
        self.name = name
        self.operator = operator

    def __repr__(self):
        return f"(= {self.name} {self.operator})"

    def invert(self) -> List['BooleanOutputVariable']:
        inverse_dict = self.operator.invert(BooleanVariable(self.name))
        return [BooleanOutputVariable(operator, name) for name, operator in inverse_dict.items()]
