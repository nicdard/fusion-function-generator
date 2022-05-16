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
from src.visitors.symbolic_printer_visitor import SymbolicPrinterVisitor


class TestSymbolicPrinterVisitor(unittest.TestCase):
    def test_boolean_visitor_easy(self):
        tree = BooleanEquality(BooleanConstant('c0'), BooleanConstant('c1'))
        self.assertEqual("(= c0 c1)", tree.accept(SymbolicPrinterVisitor()))

    def test_integer_visitor_easy(self):
        tree = IntegerEquality(IntegerConstant('c0'), IntegerConstant('c1'))
        self.assertEqual("(= c0 c1)", tree.accept(SymbolicPrinterVisitor()))

    def test_real_visitor_easy(self):
        tree = RealEquality(RealConstant('c0'), RealConstant('c1'))
        self.assertEqual("(= c0 c1)", tree.accept(SymbolicPrinterVisitor()))

    def test_string_visitor_easy(self):
        tree = StringEquality(StringLiteral('c0'), StringLiteral('c1'))
        self.assertEqual("(= c0 c1)", tree.accept(SymbolicPrinterVisitor()))

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable('z'),
            BooleanXor(
                BooleanNot(BooleanVariable('x')), 
                BooleanXor(
                    BooleanVariable('y'), 
                    BooleanNot(BooleanConstant('c0')))))
        symbolic_repr = tree.accept(SymbolicPrinterVisitor())
        self.assertEqual("(= z (xor (not x) (xor y (not c0))))", symbolic_repr)

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
        symbolic_repr = tree.accept(SymbolicPrinterVisitor())
        self.assertEqual("(= z (+ (* c0 (- x c1)) (div y v)))", symbolic_repr)

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
        symbolic_repr = tree.accept(SymbolicPrinterVisitor())
        self.assertEqual("(= z (* (- (+ (/ x c0) c1) y) c2))", symbolic_repr)

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
        symbolic_repr = tree.accept(SymbolicPrinterVisitor())
        self.assertEqual("(= z (str.++ (str.replace x c0 c1) (str.substr y (str.len c2) c3)))", symbolic_repr)

    def test_boolean_visitor_inequality(self):
        tree_1 = BooleanEquality(BooleanConstant('c0'), BooleanConstant('c1'))
        tree_2 = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        visitor = SymbolicPrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_integer_visitor_inequality(self):
        tree_1 = IntegerEquality(IntegerConstant('c0'), IntegerConstant('c1'))
        tree_2 = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        visitor = SymbolicPrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_real_visitor_inequality(self):
        tree_1 = RealEquality(RealConstant('c0'), RealConstant('c1'))
        tree_2 = RealEquality(RealVariable('x'), RealVariable('y'))
        visitor = SymbolicPrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_string_visitor_inequality(self):
        tree_1 = StringEquality(StringLiteral('c0'), StringLiteral('c1'))
        tree_2 = StringEquality(StringVariable('x'), StringVariable('y'))
        visitor = SymbolicPrinterVisitor()
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))


if __name__ == '__main__':
    unittest.main()
