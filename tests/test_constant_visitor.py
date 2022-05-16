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
from src.visitors.constant_visitor import ConstantVisitor


class TestConstantVisitor(unittest.TestCase):
    def test_boolean_visitor_easy(self):
        visitor = ConstantVisitor()
        tree = BooleanVariable('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = BooleanConstant('c0')
        self.assertEqual({'c0': 'Bool'}, tree.accept(visitor))
        tree = BooleanEquality(BooleanConstant('c0'), BooleanConstant('c1'))
        self.assertEqual({'c0': 'Bool', 'c1': 'Bool'}, tree.accept(visitor))

    def test_integer_visitor_easy(self):
        visitor = ConstantVisitor()
        tree = IntegerVariable('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = IntegerConstant('c0')
        self.assertEqual({'c0': 'Int'}, tree.accept(visitor))
        tree = IntegerEquality(IntegerConstant('c0'), IntegerConstant('c1'))
        self.assertEqual({'c0': 'Int', 'c1': 'Int'}, tree.accept(visitor))

    def test_real_visitor_easy(self):
        visitor = ConstantVisitor()
        tree = RealVariable('c0')
        self.assertEqual({}, tree.accept(visitor))
        tree = RealConstant('c0')
        self.assertEqual({'c0': 'Real'}, tree.accept(visitor))
        tree = RealEquality(RealConstant('c0'), RealConstant('c1'))
        self.assertEqual({'c0': 'Real', 'c1': 'Real'}, tree.accept(visitor))

    def test_string_visitor_easy(self):
        visitor = ConstantVisitor()
        tree = StringVariable('x')
        self.assertEqual({}, tree.accept(visitor))
        tree = StringLiteral('c0')
        self.assertEqual({'c0': 'String'}, tree.accept(visitor))
        tree = StringEquality(StringLiteral('c0'), StringLiteral('c1'))
        self.assertEqual({'c0': 'String', 'c1': 'String'},
                         tree.accept(visitor))

    def test_boolean_visitor_inequality(self):
        visitor = ConstantVisitor()
        tree_1 = BooleanEquality(BooleanConstant('c0'), BooleanConstant('c1'))
        tree_2 = BooleanEquality(BooleanConstant('c1'), BooleanConstant('c2'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_integer_visitor_inequality(self):
        visitor = ConstantVisitor()
        tree_1 = IntegerEquality(IntegerConstant('c0'), IntegerConstant('c1'))
        tree_2 = IntegerEquality(IntegerConstant('c1'), IntegerConstant('c2'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_real_visitor_inequality(self):
        visitor = ConstantVisitor()
        tree_1 = RealEquality(RealConstant('c0'), RealConstant('c1'))
        tree_2 = RealEquality(RealConstant('c1'), RealConstant('c2'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_string_visitor_inequality(self):
        visitor = ConstantVisitor()
        tree_1 = StringEquality(StringLiteral('c0'), StringLiteral('c1'))
        tree_2 = StringEquality(StringLiteral('c1'), StringLiteral('c2'))
        self.assertNotEqual(tree_1.accept(visitor), tree_2.accept(visitor))

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable('z'),
            BooleanXor(
                BooleanNot(BooleanVariable('x')),
                BooleanXor(
                    BooleanVariable('y'),
                    BooleanNot(BooleanConstant('c0')))))
        constants = tree.accept(ConstantVisitor())
        self.assertEqual({'c0': 'Bool'}, constants)

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
        constants = tree.accept(ConstantVisitor())
        self.assertEqual({'c0': 'Int', 'c1': 'Int'}, constants)

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
        constants = tree.accept(ConstantVisitor())
        self.assertEqual({'c0': 'Real', 'c1': 'Real', 'c2': 'Real'}, constants)

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
        constants = tree.accept(ConstantVisitor())
        self.assertEqual({'c0': 'String', 'c1': 'String',
                         'c2': 'String', 'c3': 'Int'}, constants)


if __name__ == '__main__':
    unittest.main()
