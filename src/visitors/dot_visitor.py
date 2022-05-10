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
    BooleanConstant,
    BooleanVariable,
    BooleanEquality,
    BooleanVisitor             
)
from src.operators.generic import Operator
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


class DotVisitor(BooleanVisitor, IntegerVisitor, RealVisitor):
    def __init__(self):
        self.id = 0

    def visit_boolean_xor(self, operator: BooleanXor):
        return self.visit_binary_operator("XOR", operator)

    def visit_boolean_not(self, operator: BooleanNot):
        return self.visit_unary_operator("NOT", operator)

    def visit_boolean_constant(self, operator: BooleanConstant):
        return self.visit_constant(operator)

    def visit_boolean_variable(self, operator: BooleanVariable):
        return self.visit_variable(operator)

    def visit_boolean_equality(self, operator: BooleanEquality):
        return self.visitRoot("EQ", operator)

    def visit_integer_addition(self, operator: IntegerAddition):
        return self.visit_binary_operator("INT_ADD", operator)

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return self.visit_binary_operator("INT_SUB", operator)

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return self.visit_binary_operator("INT_MUL", operator)

    def visit_integer_division(self, operator: IntegerDivision):
        return self.visit_binary_operator("INT_DIV", operator)

    def visit_integer_constant(self, operator: IntegerConstant):
        return self.visit_constant(operator)

    def visit_integer_variable(self, operator: IntegerVariable):
        return self.visit_variable(operator)

    def visit_integer_equality(self, operator: IntegerEquality):
        return self.visitRoot("INT_EQ", operator)

    def visit_real_addition(self, operator: RealAddition):
        return self.visit_binary_operator("REAL_ADD", operator)

    def visit_real_subtraction(self, operator: RealSubtraction):
        return self.visit_binary_operator("REAL_SUB", operator)

    def visit_real_multiplication(self, operator: RealMultiplication):
        return self.visit_binary_operator("REAL_MUL", operator)

    def visit_real_division(self, operator: RealDivision):
        return self.visit_binary_operator("REAL_DIV", operator)

    def visit_real_constant(self, operator: RealConstant):
        return self.visit_constant(operator)

    def visit_real_variable(self, operator: RealVariable):
        return self.visit_variable(operator)

    def visit_real_equality(self, operator: RealEquality):
        return self.visitRoot("REAL_EQ", operator)

    def visitRoot(self, label: str, operator: Operator):
        heading = "digraph {\n"
        ending = "\n}"
        id = self.generate_node_name()
        (op_1, children_1, edges_1) = operator.operator_1.accept(self)
        (op_2, children_2, edges_2) = operator.operator_2.accept(self)
        nodes = {id: label} | children_1 | children_2
        edges = { id: [op_1, op_2] } | edges_1 | edges_2
        nodes = [ f"    {child} [label={nodes[child]}]" for child in nodes.keys() ]
        edges = [ (f"    {key} -> {'{' + ' '.join(edges[key]) + '}'}" ) for key in edges.keys() ]
        content = heading + "\n".join(nodes) + "\n" + "\n".join(edges) + ending
        return content

    def visit_binary_operator(self, label: str, operator: Operator):
        (op_id_1, op_1, edges_1) = operator.operator_1.accept(self)
        (op_id_2, op_2, edges_2) = operator.operator_2.accept(self)
        id = self.generate_node_name()
        return (
            id,
            { id: label } | op_1 | op_2,
            { id: [op_id_1, op_id_2] } | edges_1 | edges_2,
        )

    def visit_unary_operator(self, label: str, operator: Operator):
        (op_id_1, op_1, edges_1) = operator.operator_1.accept(self)
        id = self.generate_node_name()
        return (
            id, 
            { id: label } | op_1,
            { id: [op_id_1] } | edges_1
        )
    
    def visit_constant(self, operator: Operator):
        id = self.generate_node_name()
        return (id, { id: operator.value }, {})
    
    def visit_variable(self, operator: Operator):
        id = self.generate_node_name()
        return (id, { id: operator.name }, {})
    
    def generate_node_name(self):
        self.id += 1
        return f"n{self.id}"