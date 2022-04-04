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

    operator_types = gen_configuration.get_theories()
    print(operator_types)

    root_type = random.choice(operator_types)
    t = generate_tree(root_type, 25, 3)
    print(t.accept(printer))

    with open('tree.dot', 'w') as file:
        print(t.accept(dot_exporter), file=file)

    for i, inverse in enumerate(t.accept(rewriter)):
        print(inverse.accept(printer))

        with open(f'inv_tree_{i+1}.dot', 'w') as file:
            print(inverse.accept(dot_exporter), file=file)


if __name__ == '__main__':
    main()
