TIMESTAMP=$(date '+%s')
id=$((0))

# Build the docker image.
docker build . -t ffg:$TIMESTAMP

# Start all benchmarks.
BENCHMARKS="LIA LRA NRA QF_LIA QF_LRA QF_NRA QF_SLIA QF_S"
for theory in $BENCHMARKS;
do
  for size in 10 20 50;
  do
    # Run cvc5 for sat and unsat seeds.
    id=$(($id + 1))
    docker run --mount source=ffg-$TIMESTAMP,destination=/app/vol --name ffg-$theory-sat-cvc5-$size ffg:$TIMESTAMP bash ./measure.sh $id cvc5 $theory sat /app/fusion_functions/$size.txt &
    id=$(($id + 1))
    docker run --mount source=ffg-$TIMESTAMP,destination=/app/vol --name ffg-$theory-unsat-cvc5-$size ffg:$TIMESTAMP bash ./measure.sh $id cvc5 $theory unsat /app/fusion_functions/$size.txt &
    # Run z3 for sat and unsat seeds..
    id=$(($id + 1))
    docker run --mount source=ffg-$TIMESTAMP,destination=/app/vol --name ffg-$theory-sat-z3-$size ffg:$TIMESTAMP bash ./measure.sh $id z3 $theory sat /app/fusion_functions/$size.txt &
    id=$(($id + 1))
    docker run --mount source=ffg-$TIMESTAMP,destination=/app/vol --name ffg-$theory-unsat-z3-$size ffg:$TIMESTAMP bash ./measure.sh $id z3 $theory unsat /app/fusion_functions/$size.txt &
  done
done

