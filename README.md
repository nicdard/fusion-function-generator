# fusion-function-generator

Automatic generation of [Fusion Functions](https://yinyang.readthedocs.io/en/latest/fusion.html#fusion-functions) 
used by 
[yinyang](https://yinyang.readthedocs.io/en/latest/index.html) fuzzer for [Semantic Fusion](https://yinyang.readthedocs.io/en/latest/fusion.html).

## Running

`main.py` is the main entry point to run the tool as a standalone program. Simply type the following command in the shell:

> python3 main.py

This will run with default parameters. For a complete list of the options please type:

> python3 main.py -h

You can customize the number fusion functions that are generated and the number of operators that appear in each formula.
By default, the functions are saved in `out/fusion_functions.txt`.

## Setup and use yinyang

Here you can find a complete overview of [yinyang usage](https://yinyang.readthedocs.io/en/latest/fusion.html#usage).

Follow the following instruction to set up a basic testing environment.

1. Download latest version of at least one SMT Solver compatible with SMT-LIB format ([Z3](https://github.com/Z3Prover/z3/releases), [CVC5](https://github.com/cvc5/cvc5/releases), ...)
2. Clone the pre-categorized [seeds repository](https://github.com/testsmt/semantic-fusion-seeds)
3. Either install or clone [yinyang](https://yinyang.readthedocs.io/en/latest/installation.html)
4. Run this generator to obtain the **fusion_functions.txt** file
5. Run yinyang using the generated functions and the pre-categorized seeds

Example command (for sat oracle, quantifier free linear integer algebra):

```bash
python3.10 [path-to-yinyang-folder]/bin/yinyang "z3" \
  -o sat \
  [path-to-semantic-fusion-seeds-folder]/QF_LIA/sat/ \
  -s [path-to-tmp-folder] \
  -b [path-to-bugs-folder] \ # This folder will contain the bugs that are found during yinyang execution 
  -l [path-to-log-folder] \
  -c [path-to-fusion-function-generator]/out/fusion_functions.txt 
```


## Adding a new theory

The [generator.py](src/gen/generator.py) script is used to generate all the code under [src/operators](src/operators).
To re-generate everything, type:

> python3 src/gen/generator.py operators

This script can be used also to create a stub implementation of a new visitor in [src/visitors](src/visitors):

> python3 src/gen/generator.py stub your-visitor-name-here

To add a new theory, it is enough to modify the [gen_configuration.py](src/gen/gen_configuration.py). 
Add the new theory description by following the guideline and examples already there.

Afterwards, you will need to re-generate the gen folder and (if needed) update the visitors.
To update a visitor, make the visitor inherit from the new visitor class associated with the theory you created,
and implement all of its methods.

## References

See [docs](docs).

[References.md](docs/References.md) is a list of useful links to documentation or tools.
