# fusion-function-generator

![CI](https://github.com/nicdard/fusion-function-generator/actions/workflows/ci.yml/badge.svg)

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

## Setup and using yinyang

Here you can find a complete overview of [yinyang usage](https://yinyang.readthedocs.io/en/latest/fusion.html#usage).

Follow these instructions to set up a basic testing environment.

1. Download the latest version of at least one SMT solver compatible with SMT-LIB format ([Z3](https://github.com/Z3Prover/z3/releases), [CVC5](https://github.com/cvc5/cvc5/releases), ...)
2. Initialize the yinyang and fusion seed submodules
3. Run this generator to obtain the **fusion_functions.txt** file
4. Run yinyang using the generated functions and the pre-categorized seeds

Example command (for sat oracle, quantifier free linear integer algebra, Z3):

```bash
python3 yinyang/bin/yinyang "z3" \
  -o sat semantic_fusion_seeds/QF_LIA/sat/ \
  -s [path-to-tmp-folder] \
  -b [path-to-bugs-folder] \ # This folder will contain the bugs that are found during yinyang execution 
  -l [path-to-log-folder] \
  -c out/fusion_functions.txt 
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


## Testing

The repository provides unit tests using [unittest](https://docs.python.org/3/library/unittest.html) testing framework.
To run them, simply type:

> python3 -m unittest discover -v

## Benchmarking

A Docker image `ffg` with the latest version of cvc5 and z3 instrumented with gcov is available by building the provided Dockerfile:

> docker build ./benchmarking -t ffg

To run it, simply type:

> docker run -it --name ffg ffg

This will create a container named `ffg` in interactive mode. Note that the shell is `bash`.

To keep data between multiple runs of the container type:

> docker run -it --mount source=ffg-vol,destination=/app/ --name ffg ffg

Note that this will also persist changes in the gcov files used to count the coverage information.
Just mount the volume in a different directory if you want to have fresh build of z3 and cvc5.

To open a new bash shell on a container (named `ffg`) running a benchmark:

> docker exec -it ffg /bin/bash

To get a list of mounted volumes to a running container, type:

> docker inspect -f '{{ .Mounts }}' \<container-id\>

## References

See [docs](docs).

[References.md](docs/References.md) is a list of useful links to documentation or tools.
