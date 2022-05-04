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


from typing import List
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
from src.visitors.symbolic_printer_visitor import SymbolicPrinterVisitor
from src.visitors.rewrite_visitor import RewriteVisitor


class TestRewriteVisitor(unittest.TestCase):
    def test_boolean_visitor_easy(self):
        tree = BooleanEquality(BooleanVariable('x'), BooleanVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 1)
        self.assertEqual(inverses[0], BooleanEquality(BooleanVariable('y'), BooleanVariable('x')))

    def test_integer_visitor_easy(self):
        tree = IntegerEquality(IntegerVariable('x'), IntegerVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 1)
        self.assertEqual(inverses[0], IntegerEquality(IntegerVariable('y'), IntegerVariable('x')))

    def test_real_visitor_easy(self):
        tree = RealEquality(RealVariable('x'), RealVariable('y'))
        inverses = tree.accept(RewriteVisitor())
        self.assertEqual(len(inverses), 1)
        self.assertEqual(inverses[0], RealEquality(RealVariable('y'), RealVariable('x')))

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
        self.assertEqual(inverses[0], 
            BooleanEquality(
                BooleanVariable('x'),
                BooleanNot(BooleanXor(
                    BooleanXor(
                        BooleanVariable('y'),
                        BooleanNot(BooleanConstant('c0'))),
                    BooleanVariable('z'))))
        )
        self.assertEqual(inverses[1], 
            BooleanEquality(
                BooleanVariable('y'),
                BooleanXor(
                    BooleanNot(BooleanConstant('c0')),
                    BooleanXor(
                        BooleanNot(BooleanVariable('x')),
                        BooleanVariable('z'))))
        )

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
        self.assertEqual(inverses[0], 
            IntegerEquality(
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
        )
        self.assertEqual(inverses[1], 
            IntegerEquality(
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
        )
        self.assertEqual(inverses[2], 
            IntegerEquality(
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
        )

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
        self.assertEqual(inverses[0], 
            RealEquality(
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
        )
        self.assertEqual(inverses[1], 
            RealEquality(
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
        )


if __name__ == '__main__':
    unittest.main()
