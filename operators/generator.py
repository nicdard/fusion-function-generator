import os
import pathlib
import sys
from typing import Dict, List, Union
from gen_configuration import theories

WARNING_MESSAGE = "# WARNING: This file has been generated and it shouldn't be edited manually!\n# Look at the README to learn more.\n\n"

def define_generic(output_dir: pathlib.Path):
    """
    Generates abstract classes. 
    """
    path = output_dir.joinpath("generic.py")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write("\n".join([
            WARNING_MESSAGE,
            "from abc import ABC",
            "\n",
            "class Operator(ABC):",
            "    pass",
            "",
        ]))
        # for type in types.keys():
            

def define_visitor_interface(type: str) -> List[str]:
    """
    Generates a visitor interface for a given theory.
    """
    # We could use generics to give the right type information (https://docs.python.org/3/library/typing.html#typing.Generic), 
    # but it seems overkilling.
    class_name = f"{type.capitalize()}Visitor"
    # Extract all names from the dictionary of the operations for a given theory and
    # construct the full operation name for each of them. 
    generate_opname = lambda type : (map(lambda op : type + op, theories[type].keys()))
    content = []
    content.extend([
        "",
        f"class {class_name}(ABC):",
    ])
    for operator in generate_opname(type):
        content.append(f"    @abstractmethod")
        content.append(f"    def visit{operator}(self, operator: {operator}):")
        content.append(f"        pass")
        content.append(f"")
    return content 


def define_ast(base_name: str):
    """
    Generates class hierarchy for a given operator.  
    """
    for type in theories.keys():
        operators = theories[type]
        path = base_name.joinpath(type.lower() + "_theory.py")    
        content = [
            WARNING_MESSAGE,
            "from abc import ABC, abstractmethod",
            "from operators.gen.generic import Operator",
            "\n"
        ]
        content.extend([
           f"class {type}Operator(Operator):",
            "    @abstractmethod",
            "    def __init__(self, *inputs):",
            "        pass",
            "",
            "    @abstractmethod",
           f"    def accept(self, visitor: '{type}Visitor'):",
            "        pass",
            ""
        ])
        for operator in operators.keys():
            params = ", "
            if isinstance(operators[operator], int):
                params += ", ".join([f"input_{i}: {type}Operator" for i in range(1, operators[operator] + 1) ])
            else:
                params += operators[operator]
            content.extend([
                f"class {type}{operator}({type}Operator):",
                f"    def __init__(self{params}):",
            ])
            if isinstance(operators[operator], int):
                content.extend([
                    f"        self.operator_{i} = input_{i}" for i in range(1, operators[operator] + 1)
                ])
            else:
                parameters = map(
                    lambda s: s.split(":")[0],
                    operators[operator].split(",")
                )
                content.extend([
                    f"        self.{pname} = {pname}" for pname in parameters
                ])
            content.append("")
            content.extend([
                f"    def accept(self, visitor: '{type}Visitor'):",
                f"        return visitor.visit{type}{operator}(self)"
                "\n"
            ])
        content.extend(define_visitor_interface(type))
        with open(path, 'w+', encoding='utf-8') as f:
            f.write("\n".join(content))


def define_visitor(output_dir: pathlib.Path, name: str):
    """
    Generates a stub implementation of all visitors of all theories.
    The visitor implementation is generated in the operators folder
    as it will edited manually.
    """
    # We could use generics to give the right type information (https://docs.python.org/3/library/typing.html#typing.Generic), 
    # but it seems overkilling.
    file_name = f"{name.lower()}_visitor.py"
    class_name = f"{name.capitalize()}Visitor"
    path = output_dir.joinpath(file_name)
    # Extract all names from the dictionary of the operations for a given theory and
    # construct the full operation name for each of them. 
    generate_opname = lambda type : (map(lambda op : type + op, theories[type].keys()))
    generate_import_opname = lambda type : ",\n".join(map(lambda op : "    " + op, generate_opname(type)))
    content = [
        f"from operators.gen.{type.lower()}_theory import ( \
            \n{generate_import_opname(type)}, \
            \n    {type.capitalize()}Visitor \
            \n)" \
            for type in theories.keys()
    ]
    extends = ", ".join([ f"{type.capitalize()}Visitor" for type in theories.keys() ])
    # content.append("from operators.gen.visitor import Visitor")
    content.extend([
        "",
        f"class {class_name}({extends}):",
    ])
    for type in theories.keys():
        for operator in generate_opname(type):
            content.append(f"    def visit{operator}(self, operator: {operator}):")
            content.append(f"        pass")
            content.append(f"")
    with open(path, 'w+', encoding='utf-8') as f:
        f.write("\n".join(content))


def main():
    """
    A utility to generate operators definitions together with the Visitor interface.
    """
    script_path = pathlib.Path(__file__).parent.resolve()
    output_dir = script_path.joinpath("gen")

    if len(sys.argv) < 2:
        print("Usage: \
            \n-gen : generates (overwrites) the gen subfolder. \
            \n-stub [NAME]: generates a new visitor stub with the given NAME. Also generates the gen folder.")
        os._exit(64)

    if not (sys.argv[1] == "gen" or
        (sys.argv[1] == "stub" and len(sys.argv) >= 3)):
        os._exit(64)    
    
    # Ensure that the gen folder exists.
    os.makedirs(os.path.dirname(script_path), exist_ok=True)

    define_generic(output_dir)
    define_ast(output_dir)

    print(sys.argv[1])
    if sys.argv[1] == "stub":
        define_visitor(script_path, sys.argv[2])

if __name__ == '__main__':
    main()
