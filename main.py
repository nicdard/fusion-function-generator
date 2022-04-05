from operators import gen_configuration
from operators.emitter.yinyang_emitter import emit
from operators.tree_generation import generate_tree


def main():
    operator_types = gen_configuration.get_theories()
    print(operator_types)

    root_type = operator_types[2]
    t = generate_tree(root_type, 25, 2)
    emit(t)

    # with open('tree.dot', 'w') as file:
    #     print(t.accept(dot_exporter), file=file)
    # 
    # for i, inverse in enumerate(t.accept(rewriter)):
    #     with open(f'inv_tree_{i+1}.dot', 'w') as file:
    #         print(inverse.accept(dot_exporter), file=file)


if __name__ == '__main__':
    main()
