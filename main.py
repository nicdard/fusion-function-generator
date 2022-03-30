from operators.gen.integer_theory import *
from operators.gen.boolean_theory import *
from operators.printer_visitor import PrinterVisitor
from operators.rewrite_visitor import RewriteVisitor
from tree.generation import generate_arbitrary_ordered_tree, validate


def main():
    sub_tree_1 = IntegerAdditionOperator(IntegerVariableOperator("a"), IntegerVariableOperator("b"))
    sub_tree_2 = IntegerMultiplicationOperator(IntegerConstantOperator(5), sub_tree_1)
    sub_tree_3 = IntegerAdditionOperator(IntegerVariableOperator("c"), sub_tree_2)
    root = IntegerEqualityOperator(IntegerVariableOperator("z"), sub_tree_3)
    inverses = RewriteVisitor().visitIntegerEquality(root)
    printer = PrinterVisitor()
    print(printer.visitIntegerEquality(root))

    for inverse in inverses:
        print(printer.visitIntegerEquality(inverse))

    for _ in range(10):
        t = generate_arbitrary_ordered_tree(2, 15, (2, 2))
        print(t)


if __name__ == '__main__':
    main()
