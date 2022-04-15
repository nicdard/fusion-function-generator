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


class InfixPrinterVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def visit_boolean_xor(self, operator: BooleanXor):
        return f"({operator.operator_1.accept(self)} xor {operator.operator_2.accept(self)})"

    def visit_boolean_not(self, operator: BooleanNot):
        return f"(not {operator.operator_1.accept(self)})"

    def visit_boolean_constant(self, operator: BooleanConstant):
        return str(operator.name)

    def visit_boolean_variable(self, operator: BooleanVariable):
        return operator.name

    def visit_boolean_equality(self, operator: BooleanEquality):
        return f"({operator.operator_1.accept(self)} = {operator.operator_2.accept(self)})"

    def visit_integer_addition(self, operator: IntegerAddition):
        return f"({operator.operator_1.accept(self)} + {operator.operator_2.accept(self)})"

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return f"({operator.operator_1.accept(self)} - {operator.operator_2.accept(self)})"

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return f"({operator.operator_1.accept(self)} * {operator.operator_2.accept(self)})"

    def visit_integer_division(self, operator: IntegerDivision):
        return f"({operator.operator_1.accept(self)} div {operator.operator_2.accept(self)})"

    def visit_integer_constant(self, operator: IntegerConstant):
        return str(operator.name)

    def visit_integer_variable(self, operator: IntegerVariable):
        return operator.name

    def visit_integer_equality(self, operator: IntegerEquality):
        return f"({operator.operator_1.accept(self)} = {operator.operator_2.accept(self)})"
    
    def visit_real_addition(self, operator: RealAddition):
        return f"({operator.operator_1.accept(self)} + {operator.operator_2.accept(self)})"

    def visit_real_subtraction(self, operator: RealSubtraction):
        return f"({operator.operator_1.accept(self)} - {operator.operator_2.accept(self)})"

    def visit_real_multiplication(self, operator: RealMultiplication):
        return f"({operator.operator_1.accept(self)} * {operator.operator_2.accept(self)})"

    def visit_real_division(self, operator: RealDivision):
        return f"({operator.operator_1.accept(self)} / {operator.operator_2.accept(self)})"

    def visit_real_constant(self, operator: RealConstant):
        return str(operator.name)

    def visit_real_variable(self, operator: RealVariable):
        return operator.name

    def visit_real_equality(self, operator: RealEquality):
        return f"({operator.operator_1.accept(self)} = {operator.operator_2.accept(self)})"
