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
from ffg.operators.generic import BooleanOperator, IntegerOperator, RealOperator, StringOperator


class BooleanNot(BooleanOperator):
    def __init__(self, input_1: BooleanOperator):
        self.operator_1 = input_1

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_not(self)


class BooleanXor(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_xor(self)


class BooleanIte(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_ite(self)


class BooleanOr(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_or(self)


class BooleanAnd(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_and(self)


class BooleanImplies(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_implies(self)


class BooleanDistinct(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_distinct(self)


class IntegerDistinct(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_integer_distinct(self)


class RealDistinct(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_real_distinct(self)


class StringDistinct(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_string_distinct(self)


class BitVectorDistinct(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_bit_vector_distinct(self)


class IntegerLess(BooleanOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_integer_less(self)


class IntegerLessOrEqual(BooleanOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_integer_less_or_equal(self)


class IntegerGreater(BooleanOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_integer_greater(self)


class IntegerGreaterOrEqual(BooleanOperator):
    def __init__(self, input_1: IntegerOperator, input_2: IntegerOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_integer_greater_or_equal(self)


class RealLess(BooleanOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_real_less(self)


class RealLessOrEqual(BooleanOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_real_less_or_equal(self)


class RealGreater(BooleanOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_real_greater(self)


class RealGreaterOrEqual(BooleanOperator):
    def __init__(self, input_1: RealOperator, input_2: RealOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_real_greater_or_equal(self)


class StringLess(BooleanOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_string_less(self)


class StringLessEqual(BooleanOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_string_less_equal(self)


class StringPrefixOf(BooleanOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_string_prefix_of(self)


class StringSuffixOf(BooleanOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_string_suffix_of(self)


class StringContains(BooleanOperator):
    def __init__(self, input_1: StringOperator, input_2: StringOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_string_contains(self)


class BooleanVariable(BooleanOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_variable(self)


class BooleanConstant(BooleanOperator):
    def __init__(self):
        pass

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_constant(self)


class BooleanLiteral(BooleanOperator):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_literal(self)


class BooleanEquality(BooleanOperator):
    def __init__(self, input_1: BooleanOperator, input_2: BooleanOperator):
        self.operator_1 = input_1
        self.operator_2 = input_2

    def accept(self, visitor: 'BooleanVisitor'):
        return visitor.visit_boolean_equality(self)


class BooleanVisitor(ABC):
    @abstractmethod
    def visit_boolean_not(self, operator: BooleanNot):
        pass

    @abstractmethod
    def visit_boolean_xor(self, operator: BooleanXor):
        pass

    @abstractmethod
    def visit_boolean_ite(self, operator: BooleanIte):
        pass

    @abstractmethod
    def visit_boolean_or(self, operator: BooleanOr):
        pass

    @abstractmethod
    def visit_boolean_and(self, operator: BooleanAnd):
        pass

    @abstractmethod
    def visit_boolean_implies(self, operator: BooleanImplies):
        pass

    @abstractmethod
    def visit_boolean_distinct(self, operator: BooleanDistinct):
        pass

    @abstractmethod
    def visit_integer_distinct(self, operator: IntegerDistinct):
        pass

    @abstractmethod
    def visit_real_distinct(self, operator: RealDistinct):
        pass

    @abstractmethod
    def visit_string_distinct(self, operator: StringDistinct):
        pass

    @abstractmethod
    def visit_bit_vector_distinct(self, operator: BitVectorDistinct):
        pass

    @abstractmethod
    def visit_integer_less(self, operator: IntegerLess):
        pass

    @abstractmethod
    def visit_integer_less_or_equal(self, operator: IntegerLessOrEqual):
        pass

    @abstractmethod
    def visit_integer_greater(self, operator: IntegerGreater):
        pass

    @abstractmethod
    def visit_integer_greater_or_equal(self, operator: IntegerGreaterOrEqual):
        pass

    @abstractmethod
    def visit_real_less(self, operator: RealLess):
        pass

    @abstractmethod
    def visit_real_less_or_equal(self, operator: RealLessOrEqual):
        pass

    @abstractmethod
    def visit_real_greater(self, operator: RealGreater):
        pass

    @abstractmethod
    def visit_real_greater_or_equal(self, operator: RealGreaterOrEqual):
        pass

    @abstractmethod
    def visit_string_less(self, operator: StringLess):
        pass

    @abstractmethod
    def visit_string_less_equal(self, operator: StringLessEqual):
        pass

    @abstractmethod
    def visit_string_prefix_of(self, operator: StringPrefixOf):
        pass

    @abstractmethod
    def visit_string_suffix_of(self, operator: StringSuffixOf):
        pass

    @abstractmethod
    def visit_string_contains(self, operator: StringContains):
        pass

    @abstractmethod
    def visit_boolean_variable(self, operator: BooleanVariable):
        pass

    @abstractmethod
    def visit_boolean_constant(self, operator: BooleanConstant):
        pass

    @abstractmethod
    def visit_boolean_literal(self, operator: BooleanLiteral):
        pass

    @abstractmethod
    def visit_boolean_equality(self, operator: BooleanEquality):
        pass
