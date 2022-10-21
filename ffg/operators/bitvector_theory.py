# MIT License
#
# Copyright (c) 2022 Nicola Dardanis, Lucas Weitzendorf
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# WARNING: This file has been generated and shouldn't be edited manually!
# Look at the README to learn more.

from abc import ABC, abstractmethod
from ffg.operators.generic import BitVectorOperator, IntegerOperator


class BitVectorNot(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_not(self)


class BitVectorNegation(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_negation(self)


class BitVectorXor(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator, input_2: BitVectorOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_xor(self)


class BitVectorConcatenation(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator, input_2: BitVectorOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_concatenation(self)


class BitVectorIte(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator, input_2: BitVectorOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_ite(self)


class BitVectorExtraction(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator, input_2: IntegerOperator, input_3: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2
        self.operator_3 = input_3

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_extraction(self)


class BitVectorVariable(BitVectorOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_variable(self)


class BitVectorConstant(BitVectorOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_constant(self)


class BitVectorLiteral(BitVectorOperator):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_literal(self)


class BitVectorEquality(BitVectorOperator):
    def __init__(self, input_1: BitVectorOperator, input_2: BitVectorOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BitVectorVisitor'):
        return visitor.visit_bit_vector_equality(self)


class BitVectorVisitor(ABC):
    @abstractmethod
    def visit_bit_vector_not(self, operator: BitVectorNot):
        pass

    @abstractmethod
    def visit_bit_vector_negation(self, operator: BitVectorNegation):
        pass

    @abstractmethod
    def visit_bit_vector_xor(self, operator: BitVectorXor):
        pass

    @abstractmethod
    def visit_bit_vector_concatenation(self, operator: BitVectorConcatenation):
        pass

    @abstractmethod
    def visit_bit_vector_ite(self, operator: BitVectorIte):
        pass

    @abstractmethod
    def visit_bit_vector_extraction(self, operator: BitVectorExtraction):
        pass

    @abstractmethod
    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        pass

    @abstractmethod
    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        pass

    @abstractmethod
    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        pass

    @abstractmethod
    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        pass
