from operators.gen.boolean_theory import (             
    BooleanXOROperator,
    BooleanNOTOperator,
    BooleanConstantOperator,
    BooleanVariableOperator,
    BooleanEqualityOperator,             
    BooleanVisitor             
)
from operators.gen.generic import Operator
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

class DotVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    
    def __init__(self):
        self.id = 0

    def visitBooleanXOR(self, operator: BooleanXOROperator):
        return self.visitBinaryOperator("XOR", operator)

    def visitBooleanNOT(self, operator: BooleanNOTOperator):
        return self.visitUnaryOperator("NOT", operator)

    def visitBooleanConstant(self, operator: BooleanConstantOperator):
        return self.visitConstant(operator)

    def visitBooleanVariable(self, operator: BooleanVariableOperator):
        return self.visitVariable(operator)

    def visitBooleanEquality(self, operator: BooleanEqualityOperator):
        return self.visitRoot("EQ", operator)

    def visitIntegerAddition(self, operator: IntegerAdditionOperator):
        return self.visitBinaryOperator("INT_ADD", operator)

    def visitIntegerSubtraction(self, operator: IntegerSubtractionOperator):
        return self.visitBinaryOperator("INT_SUB", operator)

    def visitIntegerMultiplication(self, operator: IntegerMultiplicationOperator):
        return self.visitBinaryOperator("INT_MUL", operator)

    def visitIntegerDivision(self, operator: IntegerDivisionOperator):
        return self.visitBinaryOperator("INT_DIV", operator)

    def visitIntegerConstant(self, operator: IntegerConstantOperator):
        return self.visitConstant(operator)

    def visitIntegerVariable(self, operator: IntegerVariableOperator):
        return self.visitVariable(operator)

    def visitIntegerEquality(self, operator: IntegerEqualityOperator):
        return self.visitRoot("INT_EQ", operator)

    def visitRealAddition(self, operator: RealAdditionOperator):
        return self.visitBinaryOperator("REAL_ADD", operator)

    def visitRealSubtraction(self, operator: RealSubtractionOperator):
        return self.visitBinaryOperator("REAL_SUB", operator)

    def visitRealMultiplication(self, operator: RealMultiplicationOperator):
        return self.visitBinaryOperator("REAL_MUL", operator)

    def visitRealDivision(self, operator: RealDivisionOperator):
        return self.visitBinaryOperator("REAL_DIV", operator)

    def visitRealConstant(self, operator: RealConstantOperator):
        return self.visitConstant(operator)

    def visitRealVariable(self, operator: RealVariableOperator):
        return self.visitVariable(operator)

    def visitRealEquality(self, operator: RealEqualityOperator):
        return self.visitRoot("REAL_EQ", operator)

    def visitRoot(self, label: str, operator: Operator):
        heading = "digraph {\n"
        ending = "\n}"
        id = self.generateNodeName()
        (op_1, children_1, edges_1) = operator.operator_1.accept(self)
        (op_2, children_2, edges_2) = operator.operator_2.accept(self)
        nodes = {id: label} | children_1 | children_2
        edges = { id: [op_1, op_2] } | edges_1 | edges_2
        nodes = [ f"    {child} [label={nodes[child]}]" for child in nodes.keys() ]
        edges = [ (f"    {key} -> {'{' + ' '.join(edges[key]) + '}'}" ) for key in edges.keys() ]
        content = heading + "\n".join(nodes) + "\n" + "\n".join(edges) + ending
        return content

    def visitBinaryOperator(self, label: str, operator: Operator):
        (op_id_1, op_1, edges_1) = operator.operator_1.accept(self)
        (op_id_2, op_2, edges_2) = operator.operator_2.accept(self)
        id = self.generateNodeName()
        return (
            id,
            { id: label } | op_1 | op_2,
            { id: [op_id_1, op_id_2] } | edges_1 | edges_2,
        )

    def visitUnaryOperator(self, label: str, operator: Operator):
        (op_id_1, op_1, edges_1) = operator.operator_1.accept(self)
        id = self.generateNodeName()
        return (
            id, 
            { id: label } | op_1,
            { id: [op_id_1] } | edges_1
        )
    
    def visitConstant(self, operator: Operator):
        id = self.generateNodeName()
        return (id, { id: operator.value }, {})
    
    def visitVariable(self, operator: Operator):
        id = self.generateNodeName()
        return (id, { id: operator.name }, {})
    
    def generateNodeName(self):
        self.id += 1
        return f"n{self.id}"