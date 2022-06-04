#!/bin/bash

Z3COMMAND="z3 smt.string_solver=z3str3"
CVC5COMMAND="cvc5 --strings-exp"

COMMAND=""
if [ "$1" == "z3" ]
then
  COMMAND="$Z3COMMAND"
else
  COMMAND="$CVC5COMMAND"
fi

LOGIC=$2
ORACLE=$3
FUSION_FUNCTONS=$4
SMT_TIMEOUT=30
mkdir /app/vol
TIMESTAMP=$(date '+%s')
WORKDIR="/app/vol/$TIMESTAMP"
mkdir $WORKDIR
mkdir $WORKDIR/bugs
mkdir $WORKDIR/scratch
mkdir $WORKDIR/logs

echo "command=$COMMAND, logic=$LOGIC, oracle=$ORACLE, fusion_functions=$FUSION_FUNCTONS, smt_timeout=$SMT_TIMEOUT" > $WORKDIR/options-$LOGIC-$ORACLE.txt
echo "==============="
cat $WORKDIR/options-$LOGIC-$ORACLE.txt
echo "===============\n\n"

cp $FUSION_FUNCTONS $WORKDIR

#timeout 1h python3 yinyang/bin/yinyang -t $SMT_TIMEOUT -b $WORKDIR/bugs/$ORACLE -s $WORKDIR/scratch/$ORACLE -l $WORKDIR/logs/$ORACLE -c $WORKDIR/$FUSION_FUNCTONS -o $ORACLE "$COMMAND" /app/semantic-fusion-seeds/$LOGIC/$ORACLE
timeout 1h python3 yinyang/bin/yinyang -t $SMT_TIMEOUT -b $WORKDIR/bugs/$ORACLE -s $WORKDIR/scratch/$ORACLE -l $WORKDIR/logs/$ORACLE -c $FUSION_FUNCTONS -o $ORACLE "$COMMAND" /app/semantic-fusion-seeds/$LOGIC/$ORACLE

/app/coverage.sh $1 $WORKDIR
