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


from src.operators.boolean_theory import (
    BooleanXor,
    BooleanNot,
    BooleanVariable,
    BooleanConstant,
    BooleanEquality,
    BooleanVisitor
)
from src.operators.integer_theory import (
    IntegerAddition,
    IntegerSubtraction,
    IntegerMultiplication,
    IntegerDivision,
    IntegerVariable,
    IntegerConstant,
    IntegerEquality,
    IntegerVisitor
)
from src.operators.real_theory import (
    RealAddition,
    RealSubtraction,
    RealMultiplication,
    RealDivision,
    RealVariable,
    RealConstant,
    RealEquality,
    RealVisitor
)
from src.visitors.variable_visitor import VariableVisitor


class ConstantVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def visit_boolean_xor(self, operator: BooleanXor):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_boolean_not(self, operator: BooleanNot):
        return operator.operator_1.accept(self)

    def visit_boolean_variable(self, operator: BooleanVariable):
        return {}

    def visit_boolean_constant(self, operator: BooleanConstant):
        return {operator.name: "Bool"}
    
    def visit_boolean_equality(self, operator: BooleanEquality):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_integer_addition(self, operator: IntegerAddition):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_integer_division(self, operator: IntegerDivision):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_integer_variable(self, operator: IntegerVariable):
        return {}

    def visit_integer_constant(self, operator: IntegerConstant):
        return {operator.name: "Int"}

    def visit_integer_equality(self, operator: IntegerEquality):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_real_addition(self, operator: RealAddition):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_real_subtraction(self, operator: RealSubtraction):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_real_multiplication(self, operator: RealMultiplication):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_real_division(self, operator: RealDivision):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

    def visit_real_variable(self, operator: RealVariable):
        return {}

    def visit_real_constant(self, operator: RealConstant):
        return {operator.name: "Real"}

    def visit_real_equality(self, operator: RealEquality):
        return {**operator.operator_1.accept(self), **operator.operator_2.accept(self)} 

