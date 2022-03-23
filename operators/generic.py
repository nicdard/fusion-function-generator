from abc import ABC, abstractmethod
from typing import Dict, List


class _Operator(ABC):
    @abstractmethod
    def invert(self, output: '_Operator') -> Dict[str, '_Operator']:
        return {}


class OutputVariable:
    @abstractmethod
    def invert(self) -> List['OutputVariable']:
        return []
