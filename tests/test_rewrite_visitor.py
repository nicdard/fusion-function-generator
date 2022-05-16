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

from typing import List

from src.operators.generic import Operator
from src.operators.boolean_theory import *
from src.operators.integer_theory import *
from src.operators.real_theory import *
from src.operators.string_theory import *
from src.visitors.rewrite_visitor import RewriteVisitor
from src.visitors.symbolic_printer_visitor import SymbolicPrinterVisitor


class TestRewriteVisitor(unittest.TestCase):
    def assert_equal_trees(self, expected: Operator, tree: Operator):
        visitor = SymbolicPrinterVisitor()
        self.assertEqual(expected.accept(visitor), tree.accept(visitor))

    def assert_not_equal_trees(self, tree_1: Operator, tree_2: Operator):
        visitor = SymbolicPrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def assert_any_of_trees(self, expected_list: List[Operator], tree: Operator):
        visitor = SymbolicPrinterVisitor()
        self.assertIn(tree.accept(visitor), [expected.accept(
            visitor) for expected in expected_list])

    def test_boolean_visitor_easy(self):
        tree = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = BooleanEquality(BooleanVariable('y'), BooleanVariable('x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_integer_visitor_easy(self):
        tree = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = IntegerEquality(IntegerVariable('y'), IntegerVariable('x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_real_visitor_easy(self):
        tree = RealEquality(RealVariable('x'), RealVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = RealEquality(RealVariable('y'), RealVariable('x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_string_visitor_easy(self):
        tree = StringEquality(StringVariable('x'), StringVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = StringEquality(StringVariable('y'), StringVariable('x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_boolean_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = BooleanEquality(BooleanVariable(
            'x'), BooleanNot(BooleanVariable('y')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_integer_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = IntegerEquality(IntegerVariable('x'), IntegerAddition(
            IntegerVariable('y'), IntegerConstant('c')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_real_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = RealEquality(RealVariable('x'), RealVariable('y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = RealEquality(RealVariable('x'), RealAddition(
            RealVariable('y'), RealConstant('c')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_string_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = StringEquality(StringVariable('x'), StringVariable('y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = StringEquality(StringVariable('x'), StringConcatenation(
            StringVariable('y'), StringLiteral('c')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable('z'),
            BooleanXor(
                BooleanNot(BooleanVariable('x')),
                BooleanXor(
                    BooleanVariable('y'),
                    BooleanNot(
                        BooleanConstant('c0')))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(2, len(inverses))

        expected_x = BooleanEquality(
            BooleanVariable('x'),
            BooleanNot(
                BooleanXor(
                    BooleanXor(
                        BooleanVariable('y'),
                        BooleanNot(
                            BooleanConstant('c0'))),
                    BooleanVariable('z'))))
        self.assert_equal_trees(expected_x, inverses[0])

        expected_y = BooleanEquality(
            BooleanVariable('y'),
            BooleanXor(
                BooleanNot(BooleanConstant('c0')),
                BooleanXor(
                    BooleanNot(
                        BooleanVariable('x')),
                    BooleanVariable('z'))))
        self.assert_equal_trees(expected_y, inverses[1])

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            IntegerVariable('z'),
            IntegerAddition(
                IntegerMultiplication(
                    IntegerConstant('c0'),
                    IntegerSubtraction(
                        IntegerVariable('x'),
                        IntegerConstant('c1'))),
                IntegerMultiplication(
                    IntegerVariable('y'),
                    IntegerVariable('v'))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(3, len(inverses))

        expected_x = IntegerEquality(
            IntegerVariable('x'),
            IntegerAddition(
                IntegerDivision(
                    IntegerSubtraction(
                        IntegerVariable('z'),
                        IntegerMultiplication(
                            IntegerVariable('y'),
                            IntegerVariable('v'))),
                    IntegerConstant('c0')),
                IntegerConstant('c1')))
        self.assert_equal_trees(expected_x, inverses[0])

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
        self.assert_equal_trees(expected_y, inverses[1])

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
        self.assert_equal_trees(expected_v, inverses[2])

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
        self.assertEqual(2, len(inverses))

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
        self.assert_equal_trees(expected_x, inverses[0])

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
        self.assert_equal_trees(expected_y, inverses[1])

    def test_string_visitor_hard(self):
        tree = StringEquality(
            StringVariable('z'),
            StringConcatenation(
                StringVariable('x'),
                StringConcatenation(
                    StringReplacement(
                        StringLiteral('c0'),
                        StringLiteral('c1'),
                        StringLiteral('c2')),
                    StringVariable('y'))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(2, len(inverses))

        expected_x = StringEquality(
            StringVariable('x'),
            Substring(
                StringVariable('z'),
                IntegerConstant('0'),
                StringLength(
                    StringVariable('x'))))
        self.assert_equal_trees(expected_x, inverses[0])

        expected_y_1 = StringEquality(
            StringVariable('y'),
            StringReplacement(
                StringReplacement(
                    StringVariable('z'),
                    StringVariable('x'),
                    StringLiteral('""')),
                StringReplacement(
                    StringLiteral('c0'),
                    StringLiteral('c1'),
                    StringLiteral('c2')),
                StringLiteral('""')))
        expected_y_2 = StringEquality(
            StringVariable('y'),
            Substring(
                StringReplacement(
                    StringVariable('z'),
                    StringVariable('x'),
                    StringLiteral('""')),
                StringLength(
                    StringReplacement(
                        StringLiteral('c0'),
                        StringLiteral('c1'),
                        StringLiteral('c2'))),
                StringLength(
                    StringVariable('y'))))
        expected_y_3 = StringEquality(
            StringVariable('y'),
            StringReplacement(
                Substring(
                    StringVariable('z'),
                    StringLength(
                        StringVariable('x')),
                    StringLength(
                        StringConcatenation(
                            StringReplacement(
                                StringLiteral('c0'),
                                StringLiteral('c1'),
                                StringLiteral('c2')),
                            StringVariable('y')))),
                StringReplacement(
                    StringLiteral('c0'),
                    StringLiteral('c1'),
                    StringLiteral('c2')),
                StringLiteral('""')))
        expected_y_4 = StringEquality(
            StringVariable('y'),
            Substring(
                Substring(
                    StringVariable('z'),
                    StringLength(
                        StringVariable('x')),
                    StringLength(
                        StringConcatenation(
                            StringReplacement(
                                StringLiteral('c0'),
                                StringLiteral('c1'),
                                StringLiteral('c2')),
                            StringVariable('y')))),
                StringLength(
                    StringReplacement(
                        StringLiteral('c0'),
                        StringLiteral('c1'),
                        StringLiteral('c2'))),
                StringLength(
                    StringVariable('y'))))
        self.assert_any_of_trees(
            [expected_y_1, expected_y_2, expected_y_3, expected_y_4], inverses[1])


if __name__ == '__main__':
    unittest.main()
