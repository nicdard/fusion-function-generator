from src.operators.generic import Operator
from src.visitors.constant_visitor import ConstantVisitor
from src.visitors.printer_visitor import PrinterVisitor
from src.visitors.rewrite_visitor import RewriteVisitor
from src.visitors.symbolic_printer_visitor import SymbolicPrinterVisitor
from src.visitors.variable_visitor import VariableVisitor


def emit_options(file, args):
    """
    Emits the options used to generate the functions as comments to the yinyang configuration files.
    """
    print("; Generated with: https://github.com/nicdard/fusion-function-generator", file=file)
    print(f"; {args.num_functions} functions (number of #begin ... #end blocks)", file=file)
    print(f"; {args.size} operators per function", file=file)
    print("", file=file)


def emit_function(tree: Operator, file, is_symbolic: bool = True):
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

    is_symbolic: when traversing constants, emits either the names (true) or the values (false).
    """

    rewriter = RewriteVisitor()
    printer = SymbolicPrinterVisitor() if is_symbolic else PrinterVisitor()
    variables = tree.accept(VariableVisitor())
    constants = tree.accept(ConstantVisitor()) if is_symbolic else {}

    # Block begin
    print("#begin", file=file)

    # Variable declarations
    for variable, type in sorted(variables.items()):
        print(f"(declare-const {variable} {type})", file=file)

    # Constant declarations
    for constant, type in reversed(constants.items()):
        print(f"(declare-const {constant} {type})", file=file)

    # Fusion function
    print(f"(assert {tree.accept(printer)})", file=file)

    # Inverses
    for inverse_root in tree.accept(rewriter):
        print(f"(assert {inverse_root.accept(printer)})", file=file)

    # Block end
    print("#end\n", file=file)
