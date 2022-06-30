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
from src.operators.bitvector_theory import *

from src.visitors.printer_visitor import PrinterVisitor


def init_named(op_class, name):
    op = op_class()
    op.name = name
    return op


class TestSymbolicPrinterVisitor(unittest.TestCase):
    def test_boolean_visitor_easy(self):
        tree = BooleanEquality(init_named(BooleanConstant, 'c0'), init_named(BooleanConstant, 'c1'))
        self.assertEqual("(= c0 c1)", tree.accept(PrinterVisitor()))

    def test_integer_visitor_easy(self):
        tree = IntegerEquality(init_named(IntegerConstant, 'c0'), init_named(IntegerConstant, 'c1'))
        self.assertEqual("(= c0 c1)", tree.accept(PrinterVisitor()))

    def test_real_visitor_easy(self):
        tree = RealEquality(init_named(RealConstant, 'c0'), init_named(RealConstant, 'c1'))
        self.assertEqual("(= c0 c1)", tree.accept(PrinterVisitor()))

    def test_string_visitor_easy(self):
        tree = StringEquality(init_named(StringConstant, 'c0'), init_named(StringConstant, 'c1'))
        self.assertEqual("(= c0 c1)", tree.accept(PrinterVisitor()))

    def test_bitvector_visitor_easy(self):
        tree = BitVectorEquality(init_named(BitVectorConstant, 'c0'), init_named(BitVectorConstant, 'c1'))
        self.assertEqual("(= c0 c1)", tree.accept(PrinterVisitor()))

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            init_named(BooleanVariable, 'z'),
            BooleanXor(
                BooleanNot(init_named(BooleanVariable, 'x')),
                BooleanXor(
                    init_named(BooleanVariable, 'y'),
                    BooleanNot(init_named(BooleanConstant, 'c0')))))
        symbolic_repr = tree.accept(PrinterVisitor())
        self.assertEqual("(= z (xor (not x) (xor y (not c0))))", symbolic_repr)

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            init_named(IntegerVariable, 'z'),
            IntegerAddition(
                IntegerMultiplication(
                    init_named(IntegerConstant, 'c0'),
                    IntegerSubtraction(
                        init_named(IntegerVariable, 'x'),
                        init_named(IntegerConstant, 'c1')
                    )
                ),
                IntegerDivision(
                    init_named(IntegerVariable, 'y'),
                    init_named(IntegerVariable, 'v'))))
        symbolic_repr = tree.accept(PrinterVisitor())
        self.assertEqual("(= z (+ (* c0 (- x c1)) (div y v)))", symbolic_repr)

    def test_real_visitor_hard(self):
        tree = RealEquality(
            init_named(RealVariable, 'z'),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            init_named(RealVariable, 'x'),
                            init_named(RealConstant, 'c0')),
                        init_named(RealConstant, 'c1')),
                    init_named(RealVariable, 'y')),
                init_named(RealConstant, 'c2')))
        symbolic_repr = tree.accept(PrinterVisitor())
        self.assertEqual("(= z (* (- (+ (/ x c0) c1) y) c2))", symbolic_repr)

    def test_string_visitor_hard(self):
        tree = StringEquality(
            init_named(StringVariable, 'z'),
            StringConcatenation1n3(
                StringReplacement(
                    init_named(StringVariable, 'x'),
                    init_named(StringConstant, 'c0'),
                    init_named(StringConstant, 'c1')),
                Substring(
                    init_named(StringVariable, 'y'),
                    StringLength(init_named(StringConstant, 'c2')),
                    StringIndexof(
                        init_named(StringVariable, 'z'),
                        init_named(StringVariable, 'y'),
                        init_named(IntegerConstant, 'c3'),
                    ))))
        symbolic_repr = tree.accept(PrinterVisitor())
        self.assertEqual(
            "(= z (str.++ (str.replace x c0 c1) (str.substr y (str.len c2) (str.indexof z y c3))))", symbolic_repr)

    def test_bitvector_visitor_hard(self):
        tree = BitVectorEquality(
            init_named(BitVectorVariable, 'x'),
            BitVectorConcatenation(
                BitVectorExtraction(
                    init_named(BitVectorConstant, 'c0'),
                    IntegerLiteral(0),
                    IntegerLiteral(3)),
                BitVectorXor(
                    init_named(BitVectorConstant, 'c1'),
                    BitVectorConcatenation(
                        init_named(BitVectorVariable, 'y'),
                        init_named(BitVectorConstant, 'c2')
                    ))))
        symbolic_repr = tree.accept(PrinterVisitor())
        self.assertEqual("(= x (concat ((_ extract 3 0) c0) (bvxor c1 (concat y c2))))", symbolic_repr)

    def test_boolean_visitor_inequality(self):
        tree_1 = BooleanEquality(init_named(BooleanConstant, 'c0'), init_named(BooleanConstant, 'c1'))
        tree_2 = BooleanEquality(init_named(BooleanVariable, 'x'), init_named(BooleanVariable, 'y'))
        visitor = PrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_integer_visitor_inequality(self):
        tree_1 = IntegerEquality(init_named(IntegerConstant, 'c0'), init_named(IntegerConstant, 'c1'))
        tree_2 = IntegerEquality(init_named(IntegerVariable, 'x'), init_named(IntegerVariable, 'y'))
        visitor = PrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_real_visitor_inequality(self):
        tree_1 = RealEquality(init_named(RealConstant, 'c0'), init_named(RealConstant, 'c1'))
        tree_2 = RealEquality(init_named(RealVariable, 'x'), init_named(RealVariable, 'y'))
        visitor = PrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_string_visitor_inequality(self):
        tree_1 = StringEquality(init_named(StringConstant, 'c0'), init_named(StringConstant, 'c1'))
        tree_2 = StringEquality(init_named(StringVariable, 'x'), init_named(StringVariable, 'y'))
        visitor = PrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_bitvector_visitor_inequality(self):
        tree_1 = BitVectorEquality(init_named(BitVectorConstant, 'c0'), init_named(BitVectorConstant, 'c1'))
        tree_2 = BitVectorEquality(init_named(BitVectorVariable, 'x'), init_named(BitVectorVariable, 'y'))
        visitor = PrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))


if __name__ == '__main__':
    unittest.main()
