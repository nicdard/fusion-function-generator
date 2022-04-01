# WARNING: This file has been generated and it shouldn't be edited manually!
# Look at the README to learn more.


from abc import ABC, abstractmethod


class Operator(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
