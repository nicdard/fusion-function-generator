# fusion-function-generator

Automatic generation of [Fusion Functions](https://yinyang.readthedocs.io/en/latest/fusion.html#fusion-functions) 
used by 
[yinyang](https://yinyang.readthedocs.io/en/latest/index.html) fuzzer for [Semantic Fusion](https://yinyang.readthedocs.io/en/latest/fusion.html).

## Adding a new theory

The script [generator.py](src/gen/generator.py) folder is used to generate all the code under [src/operators](src/operators).
To re-generate everything, type:

> python3 gen/generator.py operators

This script can be used also to create a stub implementation of a new visitor in [src/visitors](src/visitors):

> python3 gen/generator.py stub your-visitor-name-here

To add a new theory, it is enough to modify the [gen_configuration.py](src/gen/gen_configuration.py). 
Add the new theory description by following the guideline and examples already there.

Afterwards, you will need to re-generate the gen folder and (if needed) update the visitors.
To update a visitor, make the visitor inherit from the new visitor class associated with the theory you created,
and implement all of its methods.

## References

See [docs](docs).

[References.md](docs/References.md) is a list of useful links to documentation or tools.
