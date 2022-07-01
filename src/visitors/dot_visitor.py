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

from src.operators.boolean_theory import *
from src.operators.integer_theory import *
from src.operators.real_theory import *
from src.operators.string_theory import *
from src.operators.bitvector_theory import *


class DotVisitor(BooleanVisitor, IntegerVisitor, RealVisitor, StringVisitor, BitVectorVisitor):
    def __init__(self):
        self.id = 0

    def visit_boolean_not(self, operator: BooleanNot):
        return self._visit_operator("not", operator, 1)

    def visit_boolean_xor(self, operator: BooleanXor):
        return self._visit_operator("xor", operator, 2)

    def visit_boolean_constant(self, operator: BooleanConstant):
        return self._visit_constant(operator)

    def visit_boolean_variable(self, operator: BooleanVariable):
        return self._visit_variable(operator)

    def visit_boolean_literal(self, operator: BooleanLiteral):
        name = self._generate_node_name()
        return name, {name: str(operator.value).lower()}, {}

    def visit_boolean_equality(self, operator: BooleanEquality):
        return self._visit_root("=", operator)

    def visit_integer_addition(self, operator: IntegerAddition):
        return self._visit_operator("+", operator, 2)

    def visit_integer_subtraction(self, operator: IntegerSubtraction):
        return self._visit_operator("-", operator, 2)

    def visit_integer_multiplication(self, operator: IntegerMultiplication):
        return self._visit_operator("*", operator, 2)

    def visit_integer_division(self, operator: IntegerDivision):
        return self._visit_operator("div", operator, 2)

    def visit_integer_constant(self, operator: IntegerConstant):
        return self._visit_constant(operator)

    def visit_integer_variable(self, operator: IntegerVariable):
        return self._visit_variable(operator)

    def visit_integer_literal(self, operator: IntegerLiteral):
        name = self._generate_node_name()
        return name, {name: str(operator.value)}, {}

    def visit_integer_equality(self, operator: IntegerEquality):
        return self._visit_root("=", operator)

    def visit_real_addition(self, operator: RealAddition):
        return self._visit_operator("+", operator, 2)

    def visit_real_subtraction(self, operator: RealSubtraction):
        return self._visit_operator("-", operator, 2)

    def visit_real_multiplication(self, operator: RealMultiplication):
        return self._visit_operator("*", operator, 2)

    def visit_real_division(self, operator: RealDivision):
        return self._visit_operator("/", operator, 2)

    def visit_real_constant(self, operator: RealConstant):
        return self._visit_constant(operator)

    def visit_real_variable(self, operator: RealVariable):
        return self._visit_variable(operator)

    def visit_real_literal(self, operator: RealLiteral):
        name = self._generate_node_name()
        return name, {name: str(operator.value)}, {}

    def visit_real_equality(self, operator: RealEquality):
        return self._visit_root("=", operator)

    def _visit_string_concatenation(self, operator: StringOperator):
        return self._visit_operator("str.++", operator, 2)

    def visit_string_concatenation1n1(self, operator: StringConcatenation1n1):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation1n2(self, operator: StringConcatenation1n2):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation1n3(self, operator: StringConcatenation1n3):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2n1(self, operator: StringConcatenation2n1):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2n2(self, operator: StringConcatenation2n2):
        return self._visit_string_concatenation(operator)

    def visit_string_concatenation2n3(self, operator: StringConcatenation2n3):
        return self._visit_string_concatenation(operator)

    def visit_string_length(self, operator: StringLength):
        return self._visit_operator("str.len", operator, 1)

    def visit_string_indexof(self, operator: StringIndexof):
        return self._visit_operator("str.indexof", operator, 3)

    def visit_substring(self, operator: Substring):
        return self._visit_operator("str.substr", operator, 3)

    def visit_string_replacement(self, operator: StringReplacement):
        return self._visit_operator("str.replace", operator, 3)

    def visit_string_variable(self, operator: StringVariable):
        return self._visit_variable(operator)

    def visit_string_constant(self, operator: StringLiteral):
        return self._visit_constant(operator)

    def visit_string_literal(self, operator: StringLiteral):
        name = self._generate_node_name()
        return name, {name: f"\"{operator.value}\""}, {}

    def visit_string_equality(self, operator: StringEquality):
        return self._visit_root("=", operator)

    def visit_bit_vector_not(self, operator: BitVectorNot):
        return self._visit_operator("bvnot", operator, 1)

    def visit_bit_vector_negation(self, operator: BitVectorNegation):
        return self._visit_operator("bvneg", operator, 1)

    def visit_bit_vector_xor(self, operator: BitVectorXor):
        return self._visit_operator("bvxor", operator, 2)

    def visit_bit_vector_concatenation(self, operator: BitVectorConcatenation):
        return self._visit_operator("concat", operator, 2)

    def visit_bit_vector_extraction(self, operator: BitVectorExtraction):
        return self._visit_operator("extract", operator, 3)

    def visit_bit_vector_variable(self, operator: BitVectorVariable):
        return self._visit_variable(operator)

    def visit_bit_vector_constant(self, operator: BitVectorConstant):
        return self._visit_constant(operator)

    def visit_bit_vector_literal(self, operator: BitVectorLiteral):
        name = self._generate_node_name()
        return name, {name: f"#b{''.join([str(bit) for bit in operator.value])}"}, {}

    def visit_bit_vector_equality(self, operator: BitVectorEquality):
        return self._visit_root("=", operator)

    def _visit_root(self, label, operator):
        heading = "digraph {\n"
        ending = "\n}"
        name = self._generate_node_name()
        op_1, children_1, edges_1 = operator.operator_1.accept(self)
        op_2, children_2, edges_2 = operator.operator_2.accept(self)
        nodes = {name: label, **children_1, **children_2}
        edges = {name: [op_1, op_2], **edges_1, **edges_2}
        nodes = [f"    {child} [label=\"{nodes[child]}\"]" for child in nodes.keys()]
        edges = [f"    {key} -> {'{' + ' '.join(edges[key]) + '}'}" for key in edges.keys()]
        content = heading + "\n".join(nodes) + "\n" + "\n".join(edges) + ending
        return content

    def _visit_operator(self, label, operator, arity):
        op_ids, ops, edges = [], dict(), dict()

        for i in range(arity):
            op_id, op, sub_edges = getattr(
                operator, f'operator_{i+1}').accept(self)
            op_ids.append(op_id)
            ops.update(op)
            edges.update(sub_edges)

        name = self._generate_node_name()
        return name, {name: label, **ops}, {name: op_ids, **edges}

    def _visit_constant(self, operator):
        name = self._generate_node_name()
        return name, {name: operator.name}, {}

    def _visit_variable(self, operator):
        name = self._generate_node_name()
        return name, {name: operator.name}, {}

    def _generate_node_name(self):
        self.id += 1
        return f"n{self.id}"
