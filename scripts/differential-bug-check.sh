#!/bin/bash

for filename in bugs/*.smt2; do
	echo "$filename"
	echo "z3:   $(timeout 60 z3 "$filename")"
	echo "cvc5: $(timeout 60 cvc5 "$filename" 2> /dev/null)"
	echo ""
done
