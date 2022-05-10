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


from src.operators.boolean_theory import *
from src.operators.generic import Operator
from src.operators.integer_theory import *
from src.operators.real_theory import *
from src.visitors.symbolic_printer_visitor import SymbolicPrinterVisitor
from src.visitors.rewrite_visitor import RewriteVisitor


class TestRewriteVisitor(unittest.TestCase):
    def assert_equal_trees(self, tree: Operator, expected: Operator):
        printer = SymbolicPrinterVisitor()
        self.assertEqual(tree.accept(printer), expected.accept(printer))

    def test_boolean_visitor_easy(self):
        tree = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 1)
        expected = BooleanEquality(BooleanVariable('y'), BooleanVariable('x'))
        self.assert_equal_trees(inverses[0], expected)

    def test_integer_visitor_easy(self):
        tree = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 1)
        expected = IntegerEquality(IntegerVariable('y'), IntegerVariable('x'))
        self.assert_equal_trees(inverses[0], expected)

    def test_real_visitor_easy(self):
        tree = RealEquality(RealVariable('x'), RealVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 1)
        expected = RealEquality(RealVariable('y'), RealVariable('x'))
        self.assert_equal_trees(inverses[0], expected)

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable('z'),
            BooleanXor(
                BooleanNot(BooleanVariable('x')), 
                BooleanXor(
                    BooleanVariable('y'), 
                    BooleanNot(BooleanConstant('c0')))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 2)
        expected_x = BooleanEquality(
            BooleanVariable('x'),
            BooleanNot(BooleanXor(
                BooleanXor(
                    BooleanVariable('y'),
                    BooleanNot(BooleanConstant('c0'))),
                BooleanVariable('z'))))
        self.assert_equal_trees(inverses[0], expected_x)
        expected_y = BooleanEquality(
            BooleanVariable('y'),
            BooleanXor(
                BooleanNot(BooleanConstant('c0')),
                BooleanXor(
                    BooleanNot(BooleanVariable('x')),
                    BooleanVariable('z'))))
        self.assert_equal_trees(inverses[1], expected_y)

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
                IntegerMultiplication(
                    IntegerVariable('y'),
                    IntegerVariable('v'))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 3)
        expected_x = IntegerEquality(
            IntegerVariable('x'),
            IntegerAddition(
                IntegerDivision(
                    IntegerSubtraction(
                        IntegerVariable('z'),
                        IntegerMultiplication(
                            IntegerVariable('y'),
                            IntegerVariable('v'))
                    ),
                    IntegerConstant('c0')),
                IntegerConstant('c1')))
        self.assert_equal_trees(inverses[0], expected_x)
        expected_y = IntegerEquality(
            IntegerVariable('y'),
            IntegerDivision(
                IntegerSubtraction(
                    IntegerVariable('z'),
                    IntegerMultiplication(
                        IntegerConstant('c0'),
                        IntegerSubtraction(
                            IntegerVariable('x'),
                            IntegerConstant('c1')))),
                IntegerVariable('v')))
        self.assert_equal_trees(inverses[1], expected_y)
        expected_v = IntegerEquality(
            IntegerVariable('v'),
            IntegerDivision(
                IntegerSubtraction(
                    IntegerVariable('z'),
                    IntegerMultiplication(
                        IntegerConstant('c0'),
                        IntegerSubtraction(
                            IntegerVariable('x'),
                            IntegerConstant('c1')))),
                IntegerVariable('y')))   
        self.assert_equal_trees(inverses[2], expected_v)

    def test_real_visitor_hard(self):
        tree = RealEquality(
            RealVariable('z'),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealMultiplication(
                            RealVariable('x'),
                            RealConstant('c0')),
                        RealConstant('c1')),
                    RealVariable('y')),
                RealConstant('c2'))) 
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 2)
        expected_x = RealEquality(
            RealVariable('x'),
            RealDivision(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            RealVariable('z'),
                            RealConstant('c2')),
                        RealVariable('y')),
                    RealConstant('c1')),
                RealConstant('c0')))
        self.assert_equal_trees(inverses[0], expected_x)
        expected_y = RealEquality(
            RealVariable('y'),
            RealSubtraction(
                RealAddition(
                    RealMultiplication(
                        RealVariable('x'),
                        RealConstant('c0')),
                    RealConstant('c1')),
                RealDivision(
                    RealVariable('z'),
                    RealConstant('c2'))))
        self.assert_equal_trees(inverses[1],  expected_y)


if __name__ == '__main__':
    unittest.main()
