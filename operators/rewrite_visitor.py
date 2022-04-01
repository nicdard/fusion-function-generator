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

class RewriteVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def __init__(self):
        self.output = {}

    def visitBooleanXOR(self, operator: BooleanXOROperator):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanXOROperator(operator.operator_2, output)
        self.output[operator.operator_2] = BooleanXOROperator(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitBooleanNOT(self, operator: BooleanNOTOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = BooleanNOTOperator(output)
        return operator.operator_1.accept(self)

    def visitBooleanConstant(self, operator: BooleanConstantOperator):
        return {}

    def visitBooleanVariable(self, operator: BooleanVariableOperator):
        return {operator: self.output[operator]}
        
    def visitBooleanEquality(self, operator: BooleanEqualityOperator):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        return [BooleanEqualityOperator(var, operator) for var, operator in inverse_dict.items()]

    def visitIntegerAddition(self, operator: IntegerAdditionOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerSubtractionOperator(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtractionOperator(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitIntegerSubtraction(self, operator: IntegerSubtractionOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerAdditionOperator(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerSubtractionOperator(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitIntegerMultiplication(self, operator: IntegerMultiplicationOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = IntegerDivisionOperator(output, operator.operator_2)
        self.output[operator.operator_2] = IntegerDivisionOperator(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitIntegerDivision(self, operator: IntegerDivisionOperator):
        return {}

    def visitIntegerConstant(self, operator: IntegerConstantOperator):
        return {}

    def visitIntegerVariable(self, operator: IntegerVariableOperator):
        return {operator: self.output[operator]}

    def visitIntegerEquality(self, operator: IntegerEqualityOperator):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {} 
        return [IntegerEqualityOperator(var, operator) for var, operator in inverse_dict.items()]
    
    def visitRealAddition(self, operator: RealAdditionOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = RealSubtractionOperator(output, operator.operator_2)
        self.output[operator.operator_2] = RealSubtractionOperator(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitRealSubtraction(self, operator: RealSubtractionOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = RealAdditionOperator(output, operator.operator_2)
        self.output[operator.operator_2] = RealSubtractionOperator(operator.operator_1, output)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitRealMultiplication(self, operator: RealMultiplicationOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = RealDivisionOperator(output, operator.operator_2)
        self.output[operator.operator_2] = RealDivisionOperator(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitRealDivision(self, operator: RealDivisionOperator):
        output = self.output[operator]
        self.output[operator.operator_1] = RealMultiplicationOperator(output, operator.operator_2)
        self.output[operator.operator_2] = RealDivisionOperator(output, operator.operator_1)
        inverse_1 = operator.operator_1.accept(self)
        inverse_2 = operator.operator_2.accept(self)
        return inverse_1 | inverse_2

    def visitRealConstant(self, operator: RealConstantOperator):
        return {}

    def visitRealVariable(self, operator: RealVariableOperator):
        return {operator: self.output[operator]}

    def visitRealEquality(self, operator: RealEqualityOperator):
        self.output[operator.operator_2] = operator.operator_1
        inverse_dict = operator.operator_2.accept(self)
        # Prepare the visitor to be reused
        self.output = {} 
        return [RealEqualityOperator(var, operator) for var, operator in inverse_dict.items()]


