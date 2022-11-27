# fusion-function-generator (ffg)

![CI](https://github.com/nicdard/fusion-function-generator/actions/workflows/ci.yml/badge.svg)

Automatic generation of [Fusion Functions](https://yinyang.readthedocs.io/en/latest/fusion.html#fusion-functions) 
used by 
[yinyang](https://yinyang.readthedocs.io/en/latest/index.html) fuzzer for [Semantic Fusion](https://yinyang.readthedocs.io/en/latest/fusion.html).

## Lib structure

The package is divided into 4 folders:
* gen
* operators
* visitors
* emitter

The folder `gen` contains the code which is used to generate the whole
`operators` folder, the [configuration file](ffg/gen/gen_configuration.py) exposing some api to control which operators to use during the generation of the tree as well as some constants for the options to the generation algorithm.
the file `tree_generation` instead contains the main tree generation algorithm.

`operators` contains the basic definition of the operators classes.

`visitors` folder contains useful api to print, export to DOT format and rewrite the trees to their inverses.

Finally, `emitter` includes the code needed to export fusion functions to the format understood by YinYang. It also contains an emitter that outputs fusion functions and its inverses to DOT file.

## Cookbook

Use only a subset of the theories in the generation:
```python
ffg.gen.gen_configuration.set_available_theories(['bool', 'real'])
```

Get the available theories:
```python
ffg.gen.gen_configuration.get_theories()
```

Generate a fusion function of two variables (as a tree):
```python
tree, _ = ffg.gen.tree_generation.generate_tree(root_type, size, ['x', 'y'], 'z')
```

Emit the fusion function to YinYang format as a string:
```python
output = io.StringIO()
emit_function(tree, output, wrap=False)
ff = output.getvalue()
```


