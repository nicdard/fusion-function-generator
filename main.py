from operators.dot_visitor import DotVisitor
from operators.gen.real_theory import *
from operators.gen.integer_theory import *
from operators.gen.boolean_theory import *
from operators.printer_visitor import PrinterVisitor
from operators.rewrite_visitor import RewriteVisitor
from operators.generation import generate_arity_tree, generate_operator_tree


def main():
    # sub_tree_1 = IntegerAddition(IntegerVariable("a"), IntegerVariable("b"))
    # sub_tree_2 = IntegerMultiplication(IntegerConstant(5), sub_tree_1)
    # sub_tree_3 = IntegerAddition(IntegerVariable("c"), sub_tree_2)
    # root = IntegerEquality(IntegerVariable("z"), sub_tree_3)
    # inverses = RewriteVisitor().visitIntegerEquality(root)
    printer = PrinterVisitor()
    # dot_exporter = DotVisitor()
    # print(printer.visitIntegerEquality(root))
    # print(dot_exporter.visitIntegerEquality(root))

    # for inverse in inverses:
    #    print(printer.visitIntegerEquality(inverse))

    for _ in range(10):
        t = generate_arity_tree(2, 15, (2, 2))
        t = generate_operator_tree(t, 3)

        if isinstance(t, BooleanEquality):
            print(printer.visitBooleanEquality(t))
        elif isinstance(t, IntegerEquality):
            print(printer.visitIntegerEquality(t))
        elif isinstance(t, RealEquality):
            print(printer.visitRealEquality(t))



"""
    bool_sub_tree = BooleanEquality(
        BooleanXOR(BooleanNOT
            (BooleanConstant(True)),
                   BooleanVariable("x")
                   ),
        BooleanNOT(BooleanXOR(
            BooleanConstant(False),
            BooleanVariable("y")
        ))
    )
    printer.visitBooleanEquality(bool_sub_tree)
    dot_exporter.visitBooleanEquality(bool_sub_tree)"""


if __name__ == '__main__':
    main()
