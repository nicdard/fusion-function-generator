import random

from operators import gen_configuration
from operators.dot_visitor import DotVisitor
from operators.printer_visitor import PrinterVisitor
from operators.rewrite_visitor import RewriteVisitor
from operators.tree_generation import generate_tree


def main():
    rewriter = RewriteVisitor()
    printer = PrinterVisitor()
    dot_exporter = DotVisitor()

    theory = random.choice(gen_configuration.get_theories())
    t = generate_tree(theory, 15, 3)
    print(t.accept(printer))
    # print(t.accept(dot_exporter))

    for inverse in t.accept(rewriter):
        print(inverse.accept(printer))


if __name__ == '__main__':
    main()
