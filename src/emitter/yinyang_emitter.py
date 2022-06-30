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
from src.operators.generic import Operator
from src.visitors.constant_visitor import ConstantVisitor
from src.visitors.printer_visitor import PrinterVisitor
from src.visitors.rewrite_visitor import RewriteVisitor
from src.visitors.variable_visitor import VariableVisitor


def emit(trees: List[Operator], file_path, args):
    """
    Emits multiple fusion functions and its inverses to yinyan's configuration file.

    is_symbolic: when traversing constants, emits either the names (true) or the values (false).
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        emit_options(file, args)
        for tree in trees:
            emit_function(tree, file)


def emit_options(file, args):
    """
    Emits the options used to generate the functions as comments to the yinyang configuration files.
    """
    print("; Generated with: https://github.com/nicdard/fusion-function-generator", file=file)
    print(
        f"; {args.num_functions} functions (number of #begin ... #end blocks)", file=file)
    print(f"; {args.size} operators per function", file=file)
    print("", file=file)


def emit_function(tree: Operator, file):
    """
    Emits a fusion function and its inverses to yinyang's configuration file:
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
    printer = PrinterVisitor()
    variables = tree.accept(VariableVisitor())
    constants = tree.accept(ConstantVisitor())

    # Block begin
    print("#begin", file=file)

    # Variable declarations
    for variable, type in sorted(variables.items()):
        print(f"(declare-const {variable} {type})", file=file)

    # Constant declarations
    for constant, type in constants.items():
        print(f"(declare-const {constant} {type})", file=file)

    # Fusion function
    print(f"(assert {tree.accept(printer)})", file=file)

    # Inverses
    for inverse_root in tree.accept(rewriter):
        print(f"(assert {inverse_root.accept(printer)})", file=file)

    # Block end
    print("#end\n", file=file)
