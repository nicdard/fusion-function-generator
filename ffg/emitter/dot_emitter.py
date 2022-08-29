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


import os
from typing import List

from ffg.operators.generic import Operator
from ffg.visitors.dot_visitor import DotVisitor
from ffg.visitors.rewrite_visitor import RewriteVisitor


def emit(trees: List[Operator], output_dir):
    """
    Emits multiple fusion functions and its inverses to the dot format.
    Each function is placed in a separate subdirectory inside ./out.
    """
    dot_printer = DotVisitor()
    rewriter = RewriteVisitor()
    for i, tree in enumerate(trees):
        directory = os.path.join(output_dir, f"dot_{i}")
        os.makedirs(directory, exist_ok=True)

        with open(os.path.join(directory, "z.dot"), 'w', encoding='utf-8') as file:
            digraph = tree.accept(dot_printer)
            print(digraph, file=file)

        for inv_i, inverse in enumerate(tree.accept(rewriter)):
            with open(os.path.join(directory, f"inv_{inv_i}.dot"), 'w', encoding='utf-8') as file:
                digraph = inverse.accept(dot_printer)
                print(digraph, file=file)
