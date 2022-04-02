from operators.gen.boolean_theory import (
    BooleanXOR,
    BooleanNOT,
    BooleanConstant,
    BooleanVariable,
    BooleanEquality,
    BooleanVisitor
)
from operators.gen.integer_theory import (
    IntegerAddition,
    IntegerSubtraction,
    IntegerMultiplication,
    IntegerDivision,
    IntegerConstant,
    IntegerVariable,
    IntegerEquality,
    IntegerVisitor
)
from operators.gen.real_theory import (
    RealAddition,
    RealSubtraction,
    RealMultiplication,
    RealDivision,
    RealConstant,
    RealVariable,
    RealEquality,
    RealVisitor             
)

class PrinterVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def visitBooleanXOR(self, operator: BooleanXOR):
        return f"(xor {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitBooleanNOT(self, operator: BooleanNOT):
        return f"(not {operator.operator_1.accept(self)})"

    def visitBooleanConstant(self, operator: BooleanConstant):
        return str(operator.value)

    def visitBooleanVariable(self, operator: BooleanVariable):
        return operator.name

    def visitBooleanEquality(self, operator: BooleanEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerAddition(self, operator: IntegerAddition):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerSubtraction(self, operator: IntegerSubtraction):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerMultiplication(self, operator: IntegerMultiplication):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerDivision(self, operator: IntegerDivision):
        return f"(div {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerConstant(self, operator: IntegerConstant):
        return str(operator.value)

    def visitIntegerVariable(self, operator: IntegerVariable):
        return operator.name

    def visitIntegerEquality(self, operator: IntegerEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"
    
    def visitRealAddition(self, operator: RealAddition):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealSubtraction(self, operator: RealSubtraction):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealMultiplication(self, operator: RealMultiplication):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealDivision(self, operator: RealDivision):
        return f"(/ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealConstant(self, operator: RealConstant):
        return str(operator.value)

    def visitRealVariable(self, operator: RealVariable):
        return operator.name

    def visitRealEquality(self, operator: RealEquality):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"
