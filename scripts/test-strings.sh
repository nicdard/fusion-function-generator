#!/bin/bash

# Start all benchmarks.
BENCHMARKS="QF_SLIA QF_S"
ORACLES="sat unsat"
for size in 20 35;
  do
  python3 /app/main.py --target $size.txt --theories string --size $size --num_functions 30
  for theory in $BENCHMARKS;
  do  
    for oracle in $ORACLES;
    do
      python3 /app/yinyang/bin/yinyang -t 40 -c /app/out/$size.txt -o $oracle "cvc5 --strings-exp" /app/semantic-fusion-seeds/$theory/$oracle &
      python3 /app/yinyang/bin/yinyang -t 40 -c /app/out/$size.txt -o $oracle "z3 smt.string_solver=seq" /app/semantic-fusion-seeds/$theory/$oracle &
    done
  done
done

