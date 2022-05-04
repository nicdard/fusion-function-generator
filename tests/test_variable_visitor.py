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
import sys


sys.path.append("../../")


from src.operators.boolean_theory import (
    BooleanConstant,
    BooleanEquality,
    BooleanNot,
    BooleanVariable,
    BooleanXor,
)
from src.operators.integer_theory import ( 
    IntegerAddition,
    IntegerConstant,
    IntegerDivision,
    IntegerEquality,
    IntegerMultiplication,
    IntegerSubtraction,
    IntegerVariable,
)
from src.operators.real_theory import (
    RealAddition,
    RealConstant,
    RealDivision,
    RealEquality,
    RealMultiplication,
    RealSubtraction, 
    RealVariable,
)
from src.visitors.variable_visitor import VariableVisitor


class TestVariableVisitor(unittest.TestCase):
    def test_boolean_visitor_easy(self):
        tree = BooleanVariable('x')
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Bool'})
        tree = BooleanConstant('c0')
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {})
        tree = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Bool', 'y': 'Bool'})

    def test_integer_visitor_easy(self):
        tree = IntegerVariable('x')
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Int'})
        tree = IntegerConstant('c0')
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {})
        tree = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Int', 'y': 'Int'})

    def test_real_visitor_easy(self):
        tree = RealVariable('x')
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Real'})
        tree = RealConstant('c0')
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {})
        tree = RealEquality(RealVariable('x'), RealVariable('y'))
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Real', 'y': 'Real'})

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable('z'),
            BooleanXor(
                BooleanNot(BooleanVariable('x')), 
                BooleanXor(
                    BooleanVariable('y'), 
                    BooleanNot(BooleanConstant('c0')))))
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Bool', 'y': 'Bool', 'z': 'Bool'})

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            IntegerVariable('z'),
            IntegerAddition(
                IntegerMultiplication(
                    IntegerConstant('c0'),
                    IntegerSubtraction(
                        IntegerVariable('x'),
                        IntegerConstant('c1')
                    )
                ),
                IntegerDivision(
                    IntegerVariable('y'),
                    IntegerVariable('v')))) 
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'v': 'Int', 'x': 'Int', 'y': 'Int', 'z': 'Int'})

    def test_real_visitor_hard(self):
        tree = RealEquality(
            RealVariable('z'),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            RealVariable('x'),
                            RealConstant('c0')
                        ),
                        RealConstant('c1'),
                    ),
                    RealVariable('y')
                ),
                RealConstant('c2'))) 
        variables = tree.accept(VariableVisitor())
        self.assertEqual(variables, {'x': 'Real', 'y': 'Real', 'z': 'Real'})


if __name__ == '__main__':
    unittest.main()
