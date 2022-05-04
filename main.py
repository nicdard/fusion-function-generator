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
import random
import argparse

from src.gen import gen_configuration
from src.emitter.yinyang_emitter import emit_function, emit_options
from src.gen.tree_generation import generate_tree
from src.visitors.infix_printer_visitor import InfixPrinterVisitor


def parse_args():
    parser = argparse.ArgumentParser(description='Generate fusion functions.')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='print formulas in standard infix notation to stdout')
    parser.add_argument('--size', '-s', type=int, default=25, help='number of operators in each function')
    parser.add_argument('--num_functions', '-n', type=int, default=10, help='number of functions to generate')
    parser.add_argument('--target', '-t', type=str, default='fusion_functions', help='name of the output file')
    return parser.parse_args()


def main(args):
    output_dir = os.path.join(os.path.dirname(__file__), 'out')
    os.makedirs(output_dir, exist_ok=True)
    file_name = args.target.removesuffix('.txt') + '.txt'

    operator_types = gen_configuration.get_theories()

    with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as file:
        emit_options(file, args)
        infix_printer = InfixPrinterVisitor()
        for i in range(args.num_functions):
            root_type = random.choice(operator_types)
            tree = generate_tree(root_type, args.size, ['y', 'x'], 'z')
            if args.verbose:
                print(f"{tree.accept(infix_printer)}\n")
            emit_function(tree, file, is_symbolic=True)


if __name__ == '__main__':
    main(parse_args())
