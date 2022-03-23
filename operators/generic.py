from abc import ABC, abstractmethod
from typing import Dict, List


class Operator(ABC):
    @abstractmethod
    def invert(self, output: 'Operator') -> Dict[str, 'Operator']:
        return {}


class OutputVariable:
    @abstractmethod
    def invert(self) -> List['OutputVariable']:
        return []
