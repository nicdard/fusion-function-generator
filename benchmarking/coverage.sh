#!/bin/bash

help()
{
  # Display Help
  echo "Compute the coverage information with gcovr."
  echo
  echo "Syntax: ./coverage.sh [z3|cvc5] <output-folder>"
  echo "options:"
  echo "z3    Compute coverage information for z3."
  echo "cvc5  Compute coverage information for cvc5."
  echo
}

if [ ! -z $1 ]; then
  echo "Compute coverage information for $1"
  gcovr --json-summary-pretty --json-summary --root /app/$1/ffg --object-directory /app/$1/build/ -o $2/coverage.json
  echo "The coverage report can be found here: $2/coverage.json"
else
  help
  exit 1
fi

