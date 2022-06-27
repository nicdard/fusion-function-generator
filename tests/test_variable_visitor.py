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
from src.visitors.variable_visitor import VariableVisitor


class TestVariableVisitor(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        import random
        random.seed(42)

    def assert_equal_value(self, value, tree):
        init_visitor = InitializationVisitor(['a', 'b', 'c', 'd', 'e'], 'z')
        tree.accept(init_visitor)
        const_visitor = VariableVisitor()
        self.assertEqual(value, tree.accept(const_visitor))

    def assert_not_equal_tree(self, tree_1, tree_2):
        init_visitor = InitializationVisitor(['a', 'b', 'c', 'd', 'e'], 'z')
        tree_1.accept(init_visitor)
        tree_2.accept(init_visitor)
        const_visitor = VariableVisitor()
        self.assertNotEqual(tree_1.accept(const_visitor), tree_2.accept(const_visitor))
    
    def test_boolean_visitor_easy(self):
        tree = BooleanConstant()
        self.assert_equal_value({}, tree)
        tree = BooleanVariable()
        self.assert_equal_value({'a': 'Bool'}, tree)
        tree = BooleanEquality(BooleanVariable(), BooleanVariable())
        self.assert_equal_value({'a': 'Bool', 'z': 'Bool'}, tree)

    def test_integer_visitor_easy(self):
        tree = IntegerConstant()
        self.assert_equal_value({}, tree)
        tree = IntegerVariable()
        self.assert_equal_value({'a': 'Int'}, tree)
        tree = IntegerEquality(IntegerVariable(), IntegerVariable())
        self.assert_equal_value({'a': 'Int', 'z': 'Int'}, tree)

    def test_real_visitor_easy(self):
        tree = RealConstant()
        self.assert_equal_value({}, tree)
        tree = RealVariable()
        self.assert_equal_value({'a': 'Real'}, tree)
        tree = RealEquality(RealVariable(), RealVariable())
        self.assert_equal_value({'a': 'Real', 'z': 'Real'}, tree)

    def test_string_visitor_easy(self):
        tree = StringConstant()
        self.assert_equal_value({}, tree)
        tree = StringVariable()
        self.assert_equal_value({'a': 'String'}, tree)
        tree = StringEquality(StringVariable(), StringVariable())
        self.assert_equal_value({'a': 'String', 'z': 'String'}, tree)

    def test_bitvector_visitor_easy(self):
        tree = BitVectorConstant()
        self.assert_equal_value({}, tree)
        tree = BitVectorVariable()
        self.assert_equal_value({'a': '(_ BitVec 16)'}, tree)
        tree = BitVectorEquality(BitVectorVariable(), BitVectorVariable())
        self.assert_equal_value({'a': '(_ BitVec 32)', 'z': '(_ BitVec 32)'}, tree)

    def test_boolean_visitor_inequality(self):
        tree_1 = BooleanVariable()
        tree_2 = BooleanEquality(BooleanVariable(), BooleanVariable())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_integer_visitor_inequality(self):
        tree_1 = IntegerVariable()
        tree_2 = IntegerEquality(IntegerVariable(), IntegerVariable())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_real_visitor_inequality(self):
        tree_1 = RealVariable()
        tree_2 = RealEquality(RealVariable(), RealVariable())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_string_visitor_inequality(self):
        tree_1 = StringVariable()
        tree_2 = StringEquality(StringVariable(), StringVariable())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_bitvector_visitor_inequality(self):
        tree_1 = BitVectorVariable()
        tree_2 = BitVectorEquality(BitVectorVariable(), BitVectorVariable())
        self.assert_not_equal_tree(tree_1, tree_2)

    def test_boolean_visitor_hard(self):
        tree = BooleanEquality(
            BooleanVariable(),
            BooleanXor(
                BooleanNot(BooleanVariable()),
                BooleanXor(
                    BooleanVariable(),
                    BooleanNot(BooleanConstant()))))
        expected = {'a': 'Bool', 'b': 'Bool', 'z': 'Bool'}
        self.assert_equal_value(expected, tree)

    def test_integer_visitor_hard(self):
        tree = IntegerEquality(
            IntegerVariable(),
            IntegerAddition(
                IntegerMultiplication(
                    IntegerConstant(),
                    IntegerSubtraction(
                        IntegerVariable(),
                        IntegerConstant())),
                IntegerDivision(
                    IntegerVariable(),
                    IntegerVariable())))
        expected = {'a': 'Int', 'b': 'Int', 'c': 'Int', 'z': 'Int'}
        self.assert_equal_value(expected, tree)

    def test_real_visitor_hard(self):
        tree = RealEquality(
            RealVariable(),
            RealMultiplication(
                RealSubtraction(
                    RealAddition(
                        RealDivision(
                            RealVariable(),
                            RealConstant()),
                        RealConstant()),
                    RealVariable()),
                RealConstant()))
        expected = {'a': 'Real', 'b': 'Real', 'z': 'Real'}
        self.assert_equal_value(expected, tree)

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
                    StringLength(StringVariable()),
                    StringIndexof(
                        StringVariable(),
                        StringVariable(),
                        IntegerConstant(),
                    ))))
        expected = {'a': 'String', 'b': 'String', 'c': 'String',
                    'd': 'String', 'e': 'String', 'z': 'String'}
        self.assert_equal_value(expected, tree)

    def test_bitvector_visitor_hard(self):
        tree = BitVectorEquality(
            BitVectorVariable(),
            BitVectorConcatenation(
                BitVectorExtraction(
                    BitVectorVariable(),
                    IntegerLiteral(0),
                    IntegerLiteral(3)),
                BitVectorXor(
                    BitVectorVariable(),
                    BitVectorConcatenation(
                        BitVectorVariable(),
                        BitVectorConstant()
                    ))))
        expected = {'a': '(_ BitVec 64)', 'b': '(_ BitVec 20)',
                    'c': '(_ BitVec 8)', 'z': '(_ BitVec 33)'}
        self.assert_equal_value(expected, tree)


if __name__ == '__main__':
    unittest.main()
