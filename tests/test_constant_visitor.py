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

from src.visitors.initialization_visitor import InitializationVisitor
from src.visitors.constant_visitor import ConstantVisitor


class TestConstantVisitor(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        import random
        random.seed(42)

    def assert_equal_value(self, value, tree):
        init_visitor = InitializationVisitor(['a', 'b', 'c', 'd', 'e'], 'z')
        tree.accept(init_visitor)
        const_visitor = ConstantVisitor()
        self.assertEqual(value, tree.accept(const_visitor))

    def assert_not_equal_tree(self, tree_1, tree_2):
        init_visitor = InitializationVisitor(['a', 'b', 'c', 'd', 'e'], 'z')
        tree_1.accept(init_visitor)
        tree_2.accept(init_visitor)
        const_visitor = ConstantVisitor()
        self.assertNotEqual(tree_1.accept(const_visitor), tree_2.accept(const_visitor))

    def test_boolean_visitor_easy(self):
        tree = BooleanVariable()
        self.assert_equal_value({}, tree)
        tree = BooleanConstant()
        self.assert_equal_value({'c0': 'Bool'}, tree)
        tree = BooleanEquality(BooleanConstant(), BooleanConstant())
        self.assert_equal_value({'c0': 'Bool', 'c1': 'Bool'}, tree)

    def test_integer_visitor_easy(self):
        tree = IntegerVariable()
        self.assert_equal_value({}, tree)
        tree = IntegerConstant()
        self.assert_equal_value({'c0': 'Int'}, tree)
        tree = IntegerEquality(IntegerConstant(), IntegerConstant())
        self.assert_equal_value({'c0': 'Int', 'c1': 'Int'}, tree)

    def test_real_visitor_easy(self):
        tree = RealVariable()
        self.assert_equal_value({}, tree)
        tree = RealConstant()
        self.assert_equal_value({'c0': 'Real'}, tree)
        tree = RealEquality(RealConstant(), RealConstant())
        self.assert_equal_value({'c0': 'Real', 'c1': 'Real'}, tree)

    def test_string_visitor_easy(self):
        tree = StringVariable()
        self.assert_equal_value({}, tree)
        tree = StringConstant()
        self.assert_equal_value({'c0': 'String'}, tree)
        tree = StringEquality(StringConstant(), StringConstant())
        self.assert_equal_value({'c0': 'String', 'c1': 'String'}, tree)

    def test_bitvector_visitor_easy(self):
        tree = BitVectorVariable()
        self.assert_equal_value({}, tree)
        tree = BitVectorConstant()
        self.assert_equal_value({'c0': '(_ BitVec 5)'}, tree)
        tree = BitVectorEquality(BitVectorConstant(), BitVectorConstant())
        self.assert_equal_value({'c0': '(_ BitVec 8)', 'c1': '(_ BitVec 8)'}, tree)

    def test_boolean_visitor_inequality(self):
        tree_1 = BooleanConstant()
        tree_2 = BooleanEquality(BooleanConstant(), BooleanConstant())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_integer_visitor_inequality(self):
        tree_1 = IntegerConstant()
        tree_2 = IntegerEquality(IntegerConstant(), IntegerConstant())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_real_visitor_inequality(self):
        tree_1 = RealConstant()
        tree_2 = RealEquality(RealConstant(), RealConstant())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_string_visitor_inequality(self):
        tree_1 = StringConstant()
        tree_2 = StringEquality(StringConstant(), StringConstant())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_bitvector_visitor_inequality(self):
        tree_1 = BitVectorConstant()
        tree_2 = BitVectorEquality(BitVectorConstant(), BitVectorConstant())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable(),
            BooleanXor(
                BooleanNot(BooleanVariable()),
                BooleanXor(
                    BooleanVariable(),
                    BooleanNot(BooleanConstant()))))
        self.assert_equal_value({'c0': 'Bool'}, tree)

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            IntegerVariable(),
            IntegerAddition(
                IntegerMultiplication(
                    IntegerConstant(),
                    IntegerSubtraction(
                        IntegerVariable(),
                        IntegerConstant()
                    )
                ),
                IntegerDivision(
                    IntegerVariable(),
                    IntegerVariable())))
        self.assert_equal_value({'c0': 'Int', 'c1': 'Int'}, tree)

    def test_real_visitor_hard(self):
        tree = RealEquality(
            RealVariable(),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            RealVariable(),
                            RealConstant()
                        ),
                        RealConstant(),
                    ),
                    RealVariable()
                ),
                RealConstant()))
        self.assert_equal_value({'c0': 'Real', 'c1': 'Real', 'c2': 'Real'}, tree)

    def test_string_visitor_hard(self):
        tree = StringEquality(
            StringVariable(),
            StringConcatenation(
                StringReplacement(
                    StringVariable(),
                    StringConstant(),
                    StringConstant()),
                Substring(
                    StringVariable(),
                    StringLength(StringConstant()),
                    StringIndexof(
                        StringVariable(),
                        StringVariable(),
                        IntegerConstant(),
                    ))))
        expected = {'c0': 'String', 'c1': 'String', 'c2': 'String', 'c3': 'Int'}
        self.assert_equal_value(expected, tree)

    def test_bitvector_visitor_hard(self):
        tree = BitVectorEquality(
            BitVectorVariable(),
            BitVectorConcatenation(
                BitVectorExtraction(
                    BitVectorConstant(),
                    IntegerLiteral(0),
                    IntegerLiteral(3)),
                BitVectorXor(
                    BitVectorConstant(),
                    BitVectorConcatenation(
                        BitVectorVariable(),
                        BitVectorConstant()
                    ))))
        expected = {'c0': '(_ BitVec 4)', 'c1': '(_ BitVec 9)', 'c2': '(_ BitVec 1)'}
        self.assert_equal_value(expected, tree)


if __name__ == '__main__':
    unittest.main()
