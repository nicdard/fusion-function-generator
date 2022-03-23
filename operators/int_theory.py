from operators.generic import _Operator, OutputVariable
from abc import abstractmethod
from typing import Dict, List


class _IntegerOperator(_Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: '_IntegerOperator') -> Dict[str, '_IntegerOperator']:
        return {}


class IntegerAddition(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(+ {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[str, _IntegerOperator]:
        inverse_1 = self.operator_1.invert(IntegerSubtraction(output, self.operator_2))
        inverse_2 = self.operator_2.invert(IntegerSubtraction(output, self.operator_1))
        return inverse_1 | inverse_2


class IntegerSubtraction(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(- {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[str, _IntegerOperator]:
        inverse_1 = self.operator_1.invert(IntegerAddition(output, self.operator_2))
        inverse_2 = self.operator_2.invert(IntegerSubtraction(self.operator_1, output))
        return inverse_1 | inverse_2


class IntegerMultiplication(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(* {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[str, _IntegerOperator]:
        inverse_1 = self.operator_1.invert(_IntegerDivision(output, self.operator_2))
        inverse_2 = self.operator_2.invert(_IntegerDivision(output, self.operator_1))
        return inverse_1 | inverse_2


class _IntegerDivision(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(div {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[str, _IntegerOperator]:
        return {}


class IntegerVariable(_IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def invert(self, output: _Operator) -> Dict[str, _IntegerOperator]:
        return {self.name: output}


class IntegerConstant(_IntegerOperator):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def invert(self, output: _Operator) -> Dict[str, _IntegerOperator]:
        return {}


class IntegerOutputVariable(OutputVariable):
    def __init__(self, operator: _IntegerOperator, name: str):
        self.name = name
        self.operator = operator

    def __repr__(self):
        return f"(= {self.name} {self.operator})"

    def invert(self) -> List['IntegerOutputVariable']:
        inverse_dict = self.operator.invert(IntegerVariable(self.name))
        return [IntegerOutputVariable(operator, name) for name, operator in inverse_dict.items()]
