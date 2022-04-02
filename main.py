from operators.dot_visitor import DotVisitor
from operators.printer_visitor import PrinterVisitor
from operators.rewrite_visitor import RewriteVisitor
from operators.generation import generate_arity_tree, generate_operator_tree


def main():
    rewriter = RewriteVisitor()
    printer = PrinterVisitor()
    dot_exporter = DotVisitor()

    t = generate_arity_tree(2, 15, (2, 2))
    t = generate_operator_tree(t, 3)
    print(t.accept(printer))
    print(t.accept(dot_exporter))

    for inverse in t.accept(rewriter):
        print(inverse.accept(printer))


if __name__ == '__main__':
    main()
