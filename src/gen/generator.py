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
import pathlib
import sys
import re
from typing import List
from gen_configuration import (
    get_constant,
    get_constant_initializer,
    get_operator_parameters,
    get_operators,
    get_root,
    get_variable,
    get_theories,
    get_theory_name,
    get_module_name,
    get_operator_types,
    get_required_modules
)

WARNING_MESSAGE = "# WARNING: This file has been generated and shouldn't be edited manually!\n" \
                  "# Look at the README to learn more.\n"

camel_case_pattern = re.compile(r'(?<!^)(?=[A-Z])')


def camel_to_snake_case(s: str) -> str:
    """
    Converts from CamelCase to snake_case.
    """
    return camel_case_pattern.sub('_', s).lower()


def read_license():
    """
    Returns the content of the LICENSE file as python comments.
    """
    path = pathlib.Path(__file__).parent.resolve()
    license_path = path.parent.parent.joinpath("LICENSE")
    comments = []
    with open(license_path, "r") as license:
        for line in license.readlines():
            comments.append(f"# {line}")
    comments.append("\n")
    return comments


def define_generic(output_dir: pathlib.Path, license: str):
    """
    Generates abstract classes. 
    """
    path = output_dir.joinpath("generic.py")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+', encoding='utf-8') as f:
        print(f"...emitting base classes to {path.as_uri()}")
        f.write(license + "\n")
        f.write("\n".join([
            WARNING_MESSAGE,
            "from abc import ABC, abstractmethod",
            "\n",
            "class Operator(ABC):",
            "    @abstractmethod",
            "    def accept(self, visitor):",
            "        pass",
            "",
        ]))
        for theory in get_theories():
            f.write("\n".join([
                "\n",
                f"class {theory}(Operator):",
                "    @abstractmethod",
                "    def __init__(self, *inputs):",
                "        pass",
                "",
                "    @abstractmethod",
                "    def accept(self, visitor):",
                "        pass",
                "",
            ]))


def define_visitor_interface(theory: str) -> List[str]:
    """
    Generates a visitor interface for a given theory.
    """
    content = []
    content.extend([
        f"class {get_theory_name(theory)}Visitor(ABC):",
    ])
    for operator in [*get_operators(theory), get_variable(theory), get_constant(theory), get_root(theory)]:
        content.append(f"    @abstractmethod")
        content.append(
            f"    def visit_{camel_to_snake_case(operator)}(self, operator: {operator}):")
        content.append(f"        pass")
        content.append(f"")
    return content


def define_ast(base_name: pathlib.Path, license: str):
    """
    Generates class hierarchy of operators for all theories.  
    """
    for theory in get_theories():
        path = base_name.joinpath(get_module_name(theory) + ".py")
        operator_types = get_operator_types(theory)
        operator_types.sort()
        content = [
            license,
            WARNING_MESSAGE,
            *[f"import {module}" for module in get_required_modules(theory)],
            "from abc import ABC, abstractmethod",
            f"from src.operators.generic import {', '.join(operator_types)}",
            "\n",
        ]

        def accept_fun(op_name):
            return [
                f"    def accept(self, visitor: '{get_theory_name(theory)}Visitor'):",
                f"        return visitor.visit_{camel_to_snake_case(op_name)}(self)",
                ""
            ]

        operators = get_operators(theory)
        for operator in operators:
            params = ", "
            params += ", ".join(
                [f"input_{i + 1}: {ptype}" for i, ptype in enumerate(get_operator_parameters(theory, operator))])
            content.extend([
                f"class {operator}({theory}):",
                f"    def __init__(self{params}):",
            ])
            content.extend([
                f"        self.operator_{i} = input_{i}" for i in
                range(1, len(get_operator_parameters(theory, operator)) + 1)
            ])
            content.extend([
                "",
                *accept_fun(operator),
                "",
            ])
        # Create variable class.
        content.extend([
            f"class {get_variable(theory)}({theory}):",
            f"    def __init__(self, name: str):",
            f"        self.name = name",
            "",
            *accept_fun(get_variable(theory)),
            "",
        ])
        # Create constant class.
        content.extend([
            f"class {get_constant(theory)}({theory}):",
            f"    def __init__(self, name: str):",
            f"        self.name = name",
            f"        self.value = {get_constant_initializer(theory)}",
            "",
            *accept_fun(get_constant(theory)),
            "",
        ])
        # Create root operator class.
        content.extend([
            f"class {get_root(theory)}({theory}):",
            f"    def __init__(self, input_1: {theory}, input_2: {theory}):",
            f"        self.operator_1 = input_1",
            f"        self.operator_2 = input_2",
        ])
        content.extend([
            "",
            *accept_fun(get_root(theory)),
            "",
        ])
        content.extend(define_visitor_interface(theory))
        with open(path, 'w+', encoding='utf-8') as f:
            print(
                f"...emitting operators and visitor interface for {theory} to {path.as_uri()}")
            f.write("\n".join(content))


def define_visitor(output_dir: pathlib.Path, name: str, license: str):
    """
    Generates a stub implementation of all visitors of all theories.
    The visitor implementation is generated in the folder specified by output_dir.
    """
    # We could use generics to give the right type information
    # (https://docs.python.org/3/library/typing.html#typing.Generic),
    # but it seems overkilling.
    file_name = f"{name.lower()}_visitor.py"
    class_name = f"{name.capitalize()}Visitor"
    path = output_dir.joinpath(file_name)

    content = [license]
    extends = []

    for theory in get_theories():
        visitor_name = f"{get_theory_name(theory)}Visitor"
        extends.append(f"{visitor_name}")

        content.append(
            f"from src.operators.{get_module_name(theory)} import (")
        for operator in [*get_operators(theory), get_variable(theory), get_constant(theory), get_root(theory)]:
            content.append(f"    {operator},")
        content.append(f"    {visitor_name}")
        content.append(")")

    extends = ", ".join(extends)

    content.extend([
        "\n",
        f"class {class_name}({extends}):",
    ])
    for theory in get_theories():
        for operator in [*get_operators(theory), get_variable(theory), get_constant(theory), get_root(theory)]:
            content.append(
                f"    def visit_{camel_to_snake_case(operator)}(self, operator: {operator}):")
            content.append(f"        pass")
            content.append(f"")
    with open(path, 'w+', encoding='utf-8') as f:
        f.write("\n".join(content))


def main():
    """
    A utility to generate operator definitions together with the Visitor interface.
    """
    script_path = pathlib.Path(__file__).parent.resolve()
    output_dir = script_path.parent.joinpath("operators")
    license = "".join(read_license())

    if len(sys.argv) < 2:
        print("Usage: \
            \n-operators : generates (overwrites) the operators subdirectory. \
            \n-stub [NAME]: generates a new visitor stub with the given NAME. Also generates the operators folder.")
        sys.exit(64)

    if not (sys.argv[1] == "operators" or
            (sys.argv[1] == "stub" and len(sys.argv) >= 3)):
        print(f"Unknown option: {sys.argv[1]}")
        sys.exit(64)

    # Ensure that the 'operators' folder exists.
    os.makedirs(os.path.dirname(script_path), exist_ok=True)

    print("Generate src/operators directory:")
    define_generic(output_dir, license)
    define_ast(output_dir, license)

    print(sys.argv[1])
    if sys.argv[1] == "stub":
        define_visitor(script_path.parent.joinpath(
            "visitors"), sys.argv[2], license)


if __name__ == '__main__':
    main()
