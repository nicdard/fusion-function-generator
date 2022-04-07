import os
import pathlib
from operators.gen.generic import Operator
from operators.printer_visitor import PrinterVisitor
from operators.rewrite_visitor import RewriteVisitor
from operators.variable_visitor import VariableVisitor


def emit(operator: Operator, filename: str = "fusion_functions.txt", output_dir: pathlib.Path = None):
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

    if output_dir is None:
        output_dir = pathlib.Path(__file__).parent.parent.parent.resolve().joinpath("fusion_functions")
    
    output_path = output_dir.joinpath(filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'a', encoding='utf-8') as file:
        rewriter = RewriteVisitor()
        inverses = operator.accept(rewriter)
        printer = PrinterVisitor()
        variable_visitor = VariableVisitor()
        variables = operator.accept(variable_visitor)
        # Block begin
        print("#begin", file=file)
        # Variable declarations
        for variable in variables.keys():
            print(f"(declare-const {variable} {variables[variable]})", file=file)
        # Fusion function
        print(f"(assert {operator.accept(printer)})", file=file)
        # Inverses
        for inverse_root in inverses:
            print(f"(assert {inverse_root.accept(printer)})", file=file)
        # Block end
        print("#end\n", file=file)
