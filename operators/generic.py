from abc import ABC, abstractmethod
from typing import Dict


class _Operator(ABC):
    @abstractmethod
    def invert(self, output: '_Operator') -> Dict['_Operator', '_Operator']:
        return {}


class _BooleanOperator(_Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: '_BooleanOperator') -> Dict['_BooleanOperator', '_BooleanOperator']:
        return {}


class _IntegerOperator(_Operator):
    @abstractmethod
    def __init__(self, *inputs):
        pass

    @abstractmethod
    def invert(self, output: '_IntegerOperator') -> Dict['_IntegerOperator', '_IntegerOperator']:
        return {}
