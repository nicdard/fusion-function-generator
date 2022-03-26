from operators.int_theory import *


def main():
    sub_tree_1 = IntegerAddition(IntegerVariable("a"), IntegerVariable("b"))
    sub_tree_2 = IntegerMultiplication(IntegerConstant(5), sub_tree_1)
    sub_tree_3 = IntegerAddition(IntegerVariable("c"), sub_tree_2)
    root = IntegerEquality(IntegerVariable("z"), sub_tree_3)
    print(root)

    for inverse in root.rewrite():
        print(inverse)


if __name__ == '__main__':
    main()
