from operators.gen.boolean_theory import (
    BooleanXor,
    BooleanNot,
    BooleanVariable,
    BooleanConstant,
    BooleanEquality,
    BooleanVisitor
)
from operators.gen.integer_theory import (
    IntegerAddition,
    IntegerSubtraction,
    IntegerMultiplication,
    IntegerDivision,
    IntegerVariable,
    IntegerConstant,
    IntegerEquality,
    IntegerVisitor
)
from operators.gen.real_theory import (
    RealAddition,
    RealSubtraction,
    RealMultiplication,
    RealDivision,
    RealVariable,
    RealConstant,
    RealEquality,
    RealVisitor
)


class VariableVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def visit_boolean_xor(self, operator: BooleanXor):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_boolean_not(self, operator: BooleanNot):
        return operator.operator_1.accept(self)

    def visit_boolean_variable(self, operator: BooleanVariable):
        return {operator.name: "Bool"}

    def visit_boolean_constant(self, operator: BooleanConstant):
        return {}

    def visit_boolean_equality(self, operator: BooleanEquality):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_integer_addition(self, operator: IntegerAddition):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_integer_division(self, operator: IntegerDivision):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_integer_variable(self, operator: IntegerVariable):
        return {operator.name: "Int"}

    def visit_integer_constant(self, operator: IntegerConstant):
        return {}

    def visit_integer_equality(self, operator: IntegerEquality):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_real_addition(self, operator: RealAddition):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_real_subtraction(self, operator: RealSubtraction):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_real_multiplication(self, operator: RealMultiplication):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_real_division(self, operator: RealDivision):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 

    def visit_real_variable(self, operator: RealVariable):
        return {operator.name: "Real"}

    def visit_real_constant(self, operator: RealConstant):
        return {}

    def visit_real_equality(self, operator: RealEquality):
        return operator.operator_1.accept(self) | operator.operator_2.accept(self) 
