from operators import int_theory


def main():
    sub_tree_1 = int_theory.Addition(int_theory.IntegerVariable("a"), int_theory.IntegerVariable("b"))
    sub_tree_2 = int_theory.Multiplication(int_theory.IntegerConstant(5), sub_tree_1)
    sub_tree_3 = int_theory.Addition(int_theory.IntegerVariable("c"), sub_tree_2)
    root = int_theory.IntegerOutputVariable(sub_tree_3, "z")
    print(root)

    for inverse in root.invert():
        print(inverse)


if __name__ == '__main__':
    main()
