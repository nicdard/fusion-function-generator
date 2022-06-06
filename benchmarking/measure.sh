#!/bin/bash

Z3COMMAND="z3 smt.string_solver=z3str3"
CVC5COMMAND="cvc5 --strings-exp"

COMMAND=""
if [ "$2" == "z3" ]
then
  COMMAND="$Z3COMMAND"
else
  COMMAND="$CVC5COMMAND"
fi

ID=$1
LOGIC=$3
ORACLE=$4
FUSION_FUNCTIONS=$5
SMT_TIMEOUT=30
mkdir /app/vol
WORKDIR="/app/vol/$ID"
mkdir $WORKDIR
mkdir $WORKDIR/bugs
mkdir $WORKDIR/scratch
mkdir $WORKDIR/logs

echo "id=$ID command=$COMMAND, logic=$LOGIC, oracle=$ORACLE, fusion_functions=$FUSION_FUNCTIONS, smt_timeout=$SMT_TIMEOUT" > $WORKDIR/options-$LOGIC-$ORACLE.txt
$COMMAND --version >> $WORKDIR/options-$LOGIC-$ORACLE.txt
echo "==============="
cat $WORKDIR/options-$LOGIC-$ORACLE.txt
echo "==============="

# Dump to json file.
echo "{" > $WORKDIR/options.json
echo "  \"id\":\"$ID\"," >> $WORKDIR/options.json
echo "  \"logic\":\"$LOGIC\"," >> $WORKDIR/options.json
echo "  \"oracle\":\"$ORACLE\"," >> $WORKDIR/options.json
echo "  \"fusion_functions\":\"$FUSION_FUNCTIONS\"," >> $WORKDIR/options.json
echo "  \"solver_cli\":\"$COMMAND\"," >> $WORKDIR/options.json
echo "  \"solver_timeout\":\"$SMT_TIMEOUT\"" >> $WORKDIR/options.json
echo "}" >> $WORKDIR/options.json

cp $FUSION_FUNCTONS $WORKDIR/

timeout 1h python3 yinyang/bin/yinyang -t $SMT_TIMEOUT -b $WORKDIR/bugs/$ORACLE -s $WORKDIR/scratch/$ORACLE -l $WORKDIR/logs/$ORACLE -c $FUSION_FUNCTIONS -o $ORACLE "$COMMAND" /app/semantic-fusion-seeds/$LOGIC/$ORACLE

/app/coverage.sh $2 $WORKDIR
