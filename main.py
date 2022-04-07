import random

from src.gen import gen_configuration
from src.emitter.yinyang_emitter import emit
from src.gen.tree_generation import generate_tree


def main():
    operator_types = gen_configuration.get_theories()

    for _ in range(10):
        root_type = random.choice(operator_types)
        t = generate_tree(root_type, 25, ['x', 'y'], 'z')
        emit(t)


if __name__ == '__main__':
    main()
