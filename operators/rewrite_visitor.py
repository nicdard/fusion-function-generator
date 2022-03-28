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

class RewriteVisitor(BooleanVisitor, IntegerVisitor):
    def __init__(self):
        self.output = {}

    def visitBooleanXOR(self, operator: BooleanXOR):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanXOR(operator.operator_2, output)
        self.output[operator.operator_2] = BooleanXOR(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitBooleanNOT(self, operator: BooleanNOT):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanNOT(output)
        return operator.operator_1.accept(self)

    def visitBooleanConstant(self, operator: BooleanConstant):
        return {}

    def visitBooleanVariable(self, operator: BooleanVariable):
        return {operator: self.output[operator]}
        
    def visitBooleanEquality(self, operator: BooleanEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        return [BooleanEquality(var, operator) for var, operator in inverse_dict.items()]

    def visitIntegerAddition(self, operator: IntegerAddition):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerSubtraction(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtraction(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitIntegerSubtraction(self, operator: IntegerSubtraction):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerAddition(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtraction(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitIntegerMultiplication(self, operator: IntegerMultiplication):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerDivision(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerDivision(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitIntegerDivision(self, operator: IntegerDivision):
        return {}

    def visitIntegerConstant(self, operator: IntegerConstant):
        return {}

    def visitIntegerVariable(self, operator: IntegerVariable):
        return {operator: self.output[operator]}

    def visitIntegerEquality(self, operator: IntegerEquality):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {} 
        return [IntegerEquality(var, operator) for var, operator in inverse_dict.items()]


