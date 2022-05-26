#!/bin/bash

help()
{
  # Display Help
  echo "Compute the coverage information with gcovr."
  echo
  echo "Syntax: ./coverage.sh [z3|cvc5]"
  echo "options:"
  echo "z3    Compute coverage information for z3."
  echo "cvc5  Compute coverage information for cvc5."
  echo
}

if [ ! -z $1 ]; then
  echo "Compute coverage information for $1"
  gcovr --root /app/$1/src --object-directory /app/$1/build/ -o /app/coverage_$1.txt
  echo "The coverage report can be found here: ${pwd} coverage_$1.txt"
else
  help
  exit 1
fi

