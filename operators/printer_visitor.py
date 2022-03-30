from operators.gen.boolean_theory import (             
    BooleanXOROperator,
    BooleanNOTOperator,
    BooleanConstantOperator,
    BooleanVariableOperator,
    BooleanEqualityOperator,
    BooleanVisitor
)
from operators.gen.integer_theory import (             
    IntegerAdditionOperator,
    IntegerSubtractionOperator,
    IntegerMultiplicationOperator,
    IntegerDivisionOperator,
    IntegerConstantOperator,
    IntegerVariableOperator,
    IntegerEqualityOperator,
    IntegerVisitor
)
from operators.gen.real_theory import (             
    RealAdditionOperator,
    RealSubtractionOperator,
    RealMultiplicationOperator,
    RealDivisionOperator,
    RealConstantOperator,
    RealVariableOperator,
    RealEqualityOperator,             
    RealVisitor             
)

class PrinterVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def visitBooleanXOR(self, operator: BooleanXOROperator):
        return f"(xor {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitBooleanNOT(self, operator: BooleanNOTOperator):
        return f"(not {operator.operator_1.accept(self)})"

    def visitBooleanConstant(self, operator: BooleanConstantOperator):
        return str(operator.value)

    def visitBooleanVariable(self, operator: BooleanVariableOperator):
        return operator.name

    def visitBooleanEquality(self, operator: BooleanEqualityOperator):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerAddition(self, operator: IntegerAdditionOperator):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerSubtraction(self, operator: IntegerSubtractionOperator):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerMultiplication(self, operator: IntegerMultiplicationOperator):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerDivision(self, operator: IntegerDivisionOperator):
        return f"(div {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitIntegerConstant(self, operator: IntegerConstantOperator):
        return str(operator.value)

    def visitIntegerVariable(self, operator: IntegerVariableOperator):
        return operator.name

    def visitIntegerEquality(self, operator: IntegerEqualityOperator):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"
    
    def visitRealAddition(self, operator: RealAdditionOperator):
        return f"(+ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealSubtraction(self, operator: RealSubtractionOperator):
        return f"(- {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealMultiplication(self, operator: RealMultiplicationOperator):
        return f"(* {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealDivision(self, operator: RealDivisionOperator):
        return f"(/ {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"

    def visitRealConstant(self, operator: RealConstantOperator):
        return str(operator.value)

    def visitRealVariable(self, operator: RealVariableOperator):
        return operator.name

    def visitRealEquality(self, operator: RealEqualityOperator):
        return f"(= {operator.operator_1.accept(self)} {operator.operator_2.accept(self)})"
