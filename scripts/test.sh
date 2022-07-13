# Start all benchmarks.
BENCHMARKS="BV LIA LRA NRA QF_BV QF_BVFP QF_ABV QF_ABVFP QF_LIA QF_LRA QF_NRA QF_SLIA QF_S"
ORACLES="sat unsat"
for size in 10 25 50;
  do
  python3 /app/main.py --target $size.txt --size $size --num_functions 50
  for theory in $BENCHMARKS;
  do  
    for oracle in $ORACLES;
    do
      python3 /app/yinyang/bin/yinyang -t 40 -c /app/out/$size.txt -o $oracle "cvc5 --strings-exp" /app/semantic-fusion-seeds/$theory/$oracle &
      python3 /app/yinyang/bin/yinyang -t 40 -c /app/out/$size.txt -o $oracle "z3 smt.ṡtring_solver=z3str3" /app/semantic-fusion-seeds/$theory/$oracle &
    done
  done
done
