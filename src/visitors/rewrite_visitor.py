from src.operators.boolean_theory import (
    BooleanXor,
    BooleanNot,
    BooleanConstant,
    BooleanVariable,
    BooleanEquality,
    BooleanVisitor
)
from src.operators.integer_theory import (
    IntegerAddition,
    IntegerSubtraction,
    IntegerMultiplication,
    IntegerDivision,
    IntegerConstant,
    IntegerVariable,
    IntegerEquality,
    IntegerVisitor
)
from src.operators.real_theory import (
    RealAddition,
    RealSubtraction,
    RealMultiplication,
    RealDivision,
    RealConstant,
    RealVariable,
    RealEquality,
    RealVisitor             
)


class RewriteVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def __init__(self):
        self.output = {}

    def visit_boolean_xor(self, operator: BooleanXor):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanXor(operator.operator_2, output)
        self.output[operator.operator_2] = BooleanXor(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_boolean_not(self, operator: BooleanNot):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanNot(output)
        return operator.operator_1.accept(self)

    def visit_boolean_constant(self, operator: BooleanConstant):
        return {}

    def visit_boolean_variable(self, operator: BooleanVariable):
        return {operator: self.output[operator]}
        
    def visit_boolean_equality(self, operator: BooleanEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        return [BooleanEquality(var, operator) for var, operator in inverse_dict.items()]

    def visit_integer_addition(self, operator: IntegerAddition):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerSubtraction(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtraction(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerAddition(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtraction(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerDivision(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerDivision(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_integer_division(self, operator: IntegerDivision):
        return {}

    def visit_integer_constant(self, operator: IntegerConstant):
        return {}

    def visit_integer_variable(self, operator: IntegerVariable):
        return {operator: self.output[operator]}

    def visit_integer_equality(self, operator: IntegerEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {} 
        return [IntegerEquality(var, operator) for var, operator in inverse_dict.items()]
    
    def visit_real_addition(self, operator: RealAddition):
        output = self.output[operator]
        self.output[operator.operator_1] = RealSubtraction(output, operator.operator_2)
        self.output[operator.operator_2] = RealSubtraction(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_real_subtraction(self, operator: RealSubtraction):
        output = self.output[operator]
        self.output[operator.operator_1] = RealAddition(output, operator.operator_2)
        self.output[operator.operator_2] = RealSubtraction(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_real_multiplication(self, operator: RealMultiplication):
        output = self.output[operator]
        self.output[operator.operator_1] = RealDivision(output, operator.operator_2)
        self.output[operator.operator_2] = RealDivision(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_real_division(self, operator: RealDivision):
        output = self.output[operator]
        self.output[operator.operator_1] = RealMultiplication(output, operator.operator_2)
        self.output[operator.operator_2] = RealDivision(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visit_real_constant(self, operator: RealConstant):
        return {}

    def visit_real_variable(self, operator: RealVariable):
        return {operator: self.output[operator]}

    def visit_real_equality(self, operator: RealEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {} 
        return [RealEquality(var, operator) for var, operator in inverse_dict.items()]
