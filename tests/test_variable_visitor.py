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


import unittest

from src.operators.boolean_theory import *
from src.operators.integer_theory import *
from src.operators.real_theory import *
from src.operators.string_theory import *
from src.visitors.variable_visitor import VariableVisitor


class TestVariableVisitor(unittest.TestCase):
    def test_boolean_visitor_easy(self):
        visitor = VariableVisitor()
        tree = BooleanConstant('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = BooleanVariable('x')
        self.assertEqual({'x': 'Bool'}, tree.accept(visitor))
        tree = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        self.assertEqual({'x': 'Bool', 'y': 'Bool'}, tree.accept(visitor))

    def test_integer_visitor_easy(self):
        visitor = VariableVisitor()
        tree = IntegerConstant('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = IntegerVariable('x')
        self.assertEqual({'x': 'Int'}, tree.accept(visitor))
        tree = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        self.assertEqual({'x': 'Int', 'y': 'Int'}, tree.accept(visitor))

    def test_real_visitor_easy(self):
        visitor = VariableVisitor()
        tree = RealConstant('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = RealVariable('x')
        self.assertEqual({'x': 'Real'}, tree.accept(visitor))
        tree = RealEquality(RealVariable('x'), RealVariable('y'))
        self.assertEqual({'x': 'Real', 'y': 'Real'}, tree.accept(visitor))

    def test_string_visitor_easy(self):
        visitor = VariableVisitor()
        tree = StringLiteral('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = StringVariable('x')
        self.assertEqual({'x': 'String'}, tree.accept(visitor))
        tree = StringEquality(StringVariable('x'), StringVariable('y'))
        self.assertEqual({'x': 'String', 'y': 'String'}, tree.accept(visitor))

    def test_boolean_visitor_inequality(self):
        visitor = VariableVisitor()
        tree_1 = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        tree_2 = BooleanEquality(BooleanVariable('y'), BooleanVariable('z'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_integer_visitor_inequality(self):
        visitor = VariableVisitor()
        tree_1 = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        tree_2 = IntegerEquality(IntegerVariable('y'), IntegerVariable('z'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_real_visitor_inequality(self):
        visitor = VariableVisitor()
        tree_1 = RealEquality(RealVariable('x'), RealVariable('y'))
        tree_2 = RealEquality(RealVariable('y'), RealVariable('z'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_string_visitor_inequality(self):
        visitor = VariableVisitor()
        tree_1 = StringEquality(StringVariable('x'), StringVariable('y'))
        tree_2 = StringEquality(StringVariable('y'), StringVariable('z'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable('z'),
            BooleanXor(
                BooleanNot(BooleanVariable('x')), 
                BooleanXor(
                    BooleanVariable('y'), 
                    BooleanNot(BooleanConstant('c0')))))
        variables = tree.accept(VariableVisitor())
        self.assertEqual({'x': 'Bool', 'y': 'Bool', 'z': 'Bool'}, variables)

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            IntegerVariable('z'),
            IntegerAddition(
                IntegerMultiplication(
                    IntegerConstant('c0'),
                    IntegerSubtraction(
                        IntegerVariable('x'),
                        IntegerConstant('c1'))),
                IntegerDivision(
                    IntegerVariable('y'),
                    IntegerVariable('v')))) 
        variables = tree.accept(VariableVisitor())
        self.assertEqual({'v': 'Int', 'x': 'Int', 'y': 'Int', 'z': 'Int'}, variables)

    def test_real_visitor_hard(self):
        tree = RealEquality(
            RealVariable('z'),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            RealVariable('x'),
                            RealConstant('c0')),
                        RealConstant('c1')),
                    RealVariable('y')),
                RealConstant('c2'))) 
        variables = tree.accept(VariableVisitor())
        self.assertEqual({'x': 'Real', 'y': 'Real', 'z': 'Real'}, variables)

    def test_string_visitor_hard(self):
        tree = StringEquality(
            StringVariable('z'),
            StringConcatenation(
                StringReplacement(
                    StringVariable('x'),
                    StringLiteral('c0'),
                    StringLiteral('c1')),
                Substring(
                    StringVariable('y'),
                    StringLength(StringLiteral('c2')),
                    IntegerConstant('c3'))))
        variables = tree.accept(VariableVisitor())
        self.assertEqual({'x': 'String', 'y': 'String', 'z': 'String'}, variables)


if __name__ == '__main__':
    unittest.main()
