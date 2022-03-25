from operators.generic import _IntegerOperator, _BooleanOperator
from typing import Dict, List


class IntegerEquality(_BooleanOperator):
    def __init__(self, operator_1: _IntegerOperator, operator_2: _IntegerOperator):
        self.operator_1 = operator_1
        self.operator_2 = operator_2

    def __repr__(self):
        return f"(= {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        return {}

    def rewrite(self) -> List['IntegerEquality']:
        inverse_dict = self.operator_2.invert(self.operator_1)
        return [IntegerEquality(var, operator) for var, operator in inverse_dict.items()]


class IntegerAddition(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(+ {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        inverse_1 = self.operator_1.invert(IntegerSubtraction(output, self.operator_2))
        inverse_2 = self.operator_2.invert(IntegerSubtraction(output, self.operator_1))
        return inverse_1 | inverse_2


class IntegerSubtraction(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(- {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        inverse_1 = self.operator_1.invert(IntegerAddition(output, self.operator_2))
        inverse_2 = self.operator_2.invert(IntegerSubtraction(self.operator_1, output))
        return inverse_1 | inverse_2


class IntegerMultiplication(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(* {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        inverse_1 = self.operator_1.invert(_IntegerDivision(output, self.operator_2))
        inverse_2 = self.operator_2.invert(_IntegerDivision(output, self.operator_1))
        return inverse_1 | inverse_2


class _IntegerDivision(_IntegerOperator):
    def __init__(self, input_1: _IntegerOperator, input_2: _IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def __repr__(self):
        return f"(div {self.operator_1} {self.operator_2})"

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        return {}


class IntegerVariable(_IntegerOperator):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        return {self: output}


class IntegerConstant(_IntegerOperator):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def invert(self, output: _IntegerOperator) -> Dict[_IntegerOperator, _IntegerOperator]:
        return {}
