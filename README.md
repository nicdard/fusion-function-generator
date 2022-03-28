# fusion-function-generator

## Adding a new theory

The script [generator.py](operators/generator.py) folder is used to generate all the code under operators/gen.
To re-generate everything, type:

> python3 operators/generator.py gen

This script can be used also to create a stub implementation of a new visitor in the operators folder:

> python3 operators/generator.py stub your-visitor-name-here

To add a new theory it is enough to modify the [gen_configuration.py](operators/gen_configuration.py). 
Add the new theory description by following the guideline and examples already there.

Afterwards you will need to re-generate the gen folder and (if needed) update the visitors.
To update a visitor, make the visitor inherit from the new visitor class associated with the theory you created,
and implement all of its methods.

## References

See the docs folder.

[References.md](docs/References.md) is a list of useful links to documentation or tools.
