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
from src.operators.bitvector_theory import *

from src.visitors.rewrite_visitor import RewriteVisitor
from src.visitors.printer_visitor import PrinterVisitor


def init_named(op_class, name):
    op = op_class()
    op.name = name
    return op


def init_bv(op_class, name, size):
    op = init_named(op_class, name)
    op.size = size
    return op


class TestRewriteVisitor(unittest.TestCase):
    def assert_equal_trees(self, expected: Operator, tree: Operator):
        visitor = PrinterVisitor()
        self.assertEqual(expected.accept(visitor), tree.accept(visitor))

    def assert_not_equal_trees(self, tree_1: Operator, tree_2: Operator):
        visitor = PrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def assert_any_of_trees(self, expected_list: List[Operator], tree: Operator):
        visitor = PrinterVisitor()
        self.assertIn(tree.accept(visitor), [expected.accept(
            visitor) for expected in expected_list])

    def test_boolean_visitor_easy(self):
        tree = BooleanEquality(init_named(BooleanVariable, 'x'), init_named(BooleanVariable, 'y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = BooleanEquality(init_named(BooleanVariable, 'y'), init_named(BooleanVariable, 'x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_integer_visitor_easy(self):
        tree = IntegerEquality(init_named(IntegerVariable, 'x'), init_named(IntegerVariable, 'y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = IntegerEquality(init_named(IntegerVariable, 'y'), init_named(IntegerVariable, 'x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_real_visitor_easy(self):
        tree = RealEquality(init_named(RealVariable, 'x'), init_named(RealVariable, 'y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = RealEquality(init_named(RealVariable, 'y'), init_named(RealVariable, 'x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_string_visitor_easy(self):
        tree = StringEquality(init_named(StringVariable, 'x'), init_named(StringVariable, 'y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = StringEquality(init_named(StringVariable, 'y'), init_named(StringVariable, 'x'))
        self.assert_equal_trees(expected, inverses[0])

    def test_bitvector_visitor_easy(self):
        tree = BitVectorEquality(init_bv(BitVectorVariable, 'x', 8), init_bv(BitVectorVariable, 'y', 8))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(1, len(inverses))
        expected = BitVectorEquality(init_bv(BitVectorVariable, 'y', 8), init_bv(BitVectorVariable, 'x', 8))
        self.assert_equal_trees(expected, inverses[0])

    def test_boolean_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = BooleanEquality(init_named(BooleanVariable, 'x'),
                                 init_named(BooleanVariable, 'y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = BooleanEquality(init_named(BooleanVariable, 'x'), BooleanNot(init_named(BooleanVariable, 'y')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_integer_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = IntegerEquality(init_named(IntegerVariable, 'x'), init_named(IntegerVariable, 'y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = IntegerEquality(init_named(IntegerVariable, 'x'), IntegerAddition(
            init_named(IntegerVariable, 'y'), init_named(IntegerConstant, 'c')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_real_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = RealEquality(init_named(RealVariable, 'x'), init_named(RealVariable, 'y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = RealEquality(init_named(RealVariable, 'x'), RealAddition(
            init_named(RealVariable, 'y'), init_named(RealConstant, 'c')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_string_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = StringEquality(init_named(StringVariable, 'x'), init_named(StringVariable, 'y'))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = StringEquality(init_named(StringVariable, 'x'), StringConcatenation1_1(
            init_named(StringVariable, 'y'), init_named(StringConstant, 'c')))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_bitvector_visitor_inequality(self):
        visitor = RewriteVisitor()

        tree_1 = BitVectorEquality(init_bv(BitVectorVariable, 'x', 8), init_bv(BitVectorVariable, 'y', 8))
        inverses_1 = tree_1.accept(visitor)
        self.assertEqual(1, len(inverses_1))

        tree_2 = BitVectorEquality(init_bv(BitVectorVariable, 'x', 16), BitVectorConcatenation(
            init_bv(BitVectorVariable, 'y', 8), init_bv(BitVectorConstant, 'c', 8)))
        inverses_2 = tree_2.accept(visitor)
        self.assertEqual(1, len(inverses_2))

        self.assert_not_equal_trees(inverses_1[0], inverses_2[0])

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            init_named(BooleanVariable, 'z'),
            BooleanXor(
                BooleanNot(init_named(BooleanVariable, 'x')),
                BooleanXor(
                    init_named(BooleanVariable, 'y'),
                    BooleanNot(
                        init_named(BooleanConstant, 'c0')))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(2, len(inverses))

        expected_x = BooleanEquality(
            init_named(BooleanVariable, 'x'),
            BooleanNot(
                BooleanXor(
                    BooleanXor(
                        init_named(BooleanVariable, 'y'),
                        BooleanNot(
                            init_named(BooleanConstant, 'c0'))),
                    init_named(BooleanVariable, 'z'))))
        self.assert_equal_trees(expected_x, inverses[0])

        expected_y = BooleanEquality(
            init_named(BooleanVariable, 'y'),
            BooleanXor(
                BooleanNot(init_named(BooleanConstant, 'c0')),
                BooleanXor(
                    BooleanNot(
                        init_named(BooleanVariable, 'x')),
                    init_named(BooleanVariable, 'z'))))
        self.assert_equal_trees(expected_y, inverses[1])

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            init_named(IntegerVariable, 'z'),
            IntegerAddition(
                IntegerMultiplication(
                    init_named(IntegerConstant, 'c0'),
                    IntegerSubtraction(
                        init_named(IntegerVariable, 'x'),
                        init_named(IntegerConstant, 'c1'))),
                IntegerMultiplication(
                    init_named(IntegerVariable, 'y'),
                    init_named(IntegerVariable, 'v'))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(3, len(inverses))

        expected_x = IntegerEquality(
            init_named(IntegerVariable, 'x'),
            IntegerAddition(
                IntegerDivision(
                    IntegerSubtraction(
                        init_named(IntegerVariable, 'z'),
                        IntegerMultiplication(
                            init_named(IntegerVariable, 'y'),
                            init_named(IntegerVariable, 'v'))),
                    init_named(IntegerConstant, 'c0')),
                init_named(IntegerConstant, 'c1')))
        self.assert_equal_trees(expected_x, inverses[0])

        expected_y = IntegerEquality(
            init_named(IntegerVariable, 'y'),
            IntegerDivision(
                IntegerSubtraction(
                    init_named(IntegerVariable, 'z'),
                    IntegerMultiplication(
                        init_named(IntegerConstant, 'c0'),
                        IntegerSubtraction(
                            init_named(IntegerVariable, 'x'),
                            init_named(IntegerConstant, 'c1')))),
                init_named(IntegerVariable, 'v')))
        self.assert_equal_trees(expected_y, inverses[1])

        expected_v = IntegerEquality(
            init_named(IntegerVariable, 'v'),
            IntegerDivision(
                IntegerSubtraction(
                    init_named(IntegerVariable, 'z'),
                    IntegerMultiplication(
                        init_named(IntegerConstant, 'c0'),
                        IntegerSubtraction(
                            init_named(IntegerVariable, 'x'),
                            init_named(IntegerConstant, 'c1')))),
                init_named(IntegerVariable, 'y')))
        self.assert_equal_trees(expected_v, inverses[2])

    def test_real_visitor_hard(self):
        tree = RealEquality(
            init_named(RealVariable, 'z'),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealMultiplication(
                            init_named(RealVariable, 'x'),
                            init_named(RealConstant, 'c0')),
                        init_named(RealConstant, 'c1')),
                    init_named(RealVariable, 'y')),
                init_named(RealConstant, 'c2')))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(2, len(inverses))

        expected_x = RealEquality(
            init_named(RealVariable, 'x'),
            RealDivision(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            init_named(RealVariable, 'z'),
                            init_named(RealConstant, 'c2')),
                        init_named(RealVariable, 'y')),
                    init_named(RealConstant, 'c1')),
                init_named(RealConstant, 'c0')))
        self.assert_equal_trees(expected_x, inverses[0])

        expected_y = RealEquality(
            init_named(RealVariable, 'y'),
            RealSubtraction(
                RealAddition(
                    RealMultiplication(
                        init_named(RealVariable, 'x'),
                        init_named(RealConstant, 'c0')),
                    init_named(RealConstant, 'c1')),
                RealDivision(
                    init_named(RealVariable, 'z'),
                    init_named(RealConstant, 'c2'))))
        self.assert_equal_trees(expected_y, inverses[1])

    def test_string_visitor_hard(self):
        tree = StringEquality(
            init_named(StringVariable, 'z'),
            StringConcatenation2_1(
                init_named(StringVariable, 'x'),
                StringConcatenation2_2(
                    StringReplacement(
                        init_named(StringConstant, 'c0'),
                        init_named(StringConstant, 'c1'),
                        init_named(StringConstant, 'c2')),
                    init_named(StringVariable, 'y'))))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(2, len(inverses))

        expected_x = StringEquality(
            init_named(StringVariable, 'x'),
            Substring(
                init_named(StringVariable, 'z'),
                init_named(IntegerConstant, '0'),
                StringIndexof(
                    init_named(StringVariable, 'z'),
                    StringConcatenation1_1(
                        StringReplacement(
                            init_named(StringConstant, 'c0'),
                            init_named(StringConstant, 'c1'),
                            init_named(StringConstant, 'c2')),
                        init_named(StringVariable, 'y')),
                    StringLength(init_named(StringVariable, 'x')))))

        self.assert_equal_trees(expected_x, inverses[0])
        expected_y = StringEquality(
            init_named(StringVariable, 'y'),
            Substring(
                Substring(
                    init_named(StringVariable, 'z'),
                    StringLength(init_named(StringVariable, 'x')),
                    StringLength(
                        StringConcatenation1_1(
                            StringReplacement(
                                init_named(StringConstant, 'c0'),
                                init_named(StringConstant, 'c1'),
                                init_named(StringConstant, 'c2')),
                            init_named(StringVariable, 'y')))),
                StringIndexof(
                    Substring(
                        init_named(StringVariable, 'z'),
                        StringLength(init_named(StringVariable, 'x')),
                        StringLength(
                            StringConcatenation1_1(
                                StringReplacement(
                                    init_named(StringConstant, 'c0'),
                                    init_named(StringConstant, 'c1'),
                                    init_named(StringConstant, 'c2')),
                                init_named(StringVariable, 'y')))),
                    init_named(StringVariable, 'y'),
                    StringLength(
                        StringReplacement(
                            init_named(StringConstant, 'c0'),
                            init_named(StringConstant, 'c1'),
                            init_named(StringConstant, 'c2')))),
                StringLength(init_named(StringVariable, 'y'))))
        self.assert_equal_trees(expected_y, inverses[1])

    def test_bitvector_visitor_hard(self):
        subtree_1 = BitVectorNegation(init_bv(BitVectorVariable, 'x', 16))
        subtree_1.size = 16
        subtree_2 = BitVectorXor(
            BitVectorNot(
                init_bv(BitVectorConstant, 'c0', 12)),
            BitVectorConcatenation(
                init_bv(BitVectorVariable, 'y', 8),
                init_bv(BitVectorConstant, 'c1', 4)
            ))
        subtree_2.size = 12

        tree = BitVectorEquality(
            init_bv(BitVectorVariable, 'z', 28),
            BitVectorConcatenation(subtree_1, subtree_2))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(2, len(inverses))

        expected_x = BitVectorEquality(
            init_bv(BitVectorVariable, 'x', 16),
            BitVectorNegation(
                BitVectorExtraction(
                    init_bv(BitVectorVariable, 'z', 28),
                    IntegerLiteral(12),
                    IntegerLiteral(27))))
        self.assert_equal_trees(expected_x, inverses[0])

        expected_y = BitVectorEquality(
            init_bv(BitVectorVariable, 'y', 8),
            BitVectorExtraction(
                BitVectorXor(
                    BitVectorNot(init_bv(BitVectorConstant, 'c0', 12)),
                    BitVectorExtraction(
                        init_bv(BitVectorVariable, 'z', 28),
                        IntegerLiteral(0),
                        IntegerLiteral(11))),
                IntegerLiteral(4),
                IntegerLiteral(11)))
        self.assert_equal_trees(expected_y, inverses[1])


if __name__ == '__main__':
    unittest.main()
