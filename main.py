from operators.gen.integer_theory import *
from operators.gen.boolean_theory import *
from operators.printer_visitor import PrinterVisitor
from operators.rewrite_visitor import RewriteVisitor


def main():
    sub_tree_1 = IntegerAddition(IntegerVariable("a"), IntegerVariable("b"))
    sub_tree_2 = IntegerMultiplication(IntegerConstant(5), sub_tree_1)
    sub_tree_3 = IntegerAddition(IntegerVariable("c"), sub_tree_2)
    root = IntegerEquality(IntegerVariable("z"), sub_tree_3)
    inverses = RewriteVisitor().visitIntegerEquality(root)
    printer = PrinterVisitor()
    print(printer.visitIntegerEquality(root))

    for inverse in inverses:
        print(printer.visitIntegerEquality(inverse))


if __name__ == '__main__':
    main()
