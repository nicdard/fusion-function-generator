import os
import random
import argparse

from src.gen import gen_configuration
from src.emitter.yinyang_emitter import emit
from src.gen.tree_generation import generate_tree


def parse_args():
    parser = argparse.ArgumentParser(description='Generate fusion functions.')
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
        for _ in range(args.num_functions):
            root_type = random.choice(operator_types)
            tree = generate_tree(root_type, args.size, ['y', 'x'], 'z')
            emit(tree, file)


if __name__ == '__main__':
    main(parse_args())
