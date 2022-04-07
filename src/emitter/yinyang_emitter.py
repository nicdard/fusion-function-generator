from src.operators.generic import Operator
from src.visitors.printer_visitor import PrinterVisitor
from src.visitors.rewrite_visitor import RewriteVisitor
from src.visitors.variable_visitor import VariableVisitor


def emit(tree: Operator, file):
    """
    Emits the fusion functions and its inverses to yinyang's configuration file:
        #begin
        <declaration of x>
        <declaration of y>
        <declaration of z>
        [<declaration of c>]
        <assert fusion function>
        <assert inversion function>
        <assert inversion function>
        #end
    For more information on the format please visit:
    https://yinyang.readthedocs.io/en/latest/fusion.html#fusion-functions
    """

    rewriter = RewriteVisitor()
    printer = PrinterVisitor()
    variables = tree.accept(VariableVisitor())

    # Block begin
    print("#begin", file=file)

    # Variable declarations
    for variable, definition in variables.items():
        print(f"(declare-const {variable} {definition})", file=file)

    # Fusion function
    print(f"(assert {tree.accept(printer)})", file=file)

    # Inverses
    for inverse_root in tree.accept(rewriter):
        print(f"(assert {inverse_root.accept(printer)})", file=file)

    # Block end
    print("#end\n", file=file)
