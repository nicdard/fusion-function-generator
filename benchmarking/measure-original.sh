#!/bin/bash

cd yinyang
git checkout master
cd ..

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
SMT_TIMEOUT=30
mkdir /app/vol
WORKDIR="/app/vol/$ID"
mkdir $WORKDIR
mkdir $WORKDIR/bugs
mkdir $WORKDIR/scratch
mkdir $WORKDIR/logs

echo "id=$ID command=$COMMAND, logic=$LOGIC, oracle=$ORACLE, smt_timeout=$SMT_TIMEOUT" > $WORKDIR/options-$LOGIC-$ORACLE.txt
$COMMAND --version >> $WORKDIR/options-$LOGIC-$ORACLE.txt
echo "==============="
cat $WORKDIR/options-$LOGIC-$ORACLE.txt
echo "==============="

cp $FUSION_FUNCTONS $WORKDIR

#timeout 1h python3 yinyang/bin/yinyang -t $SMT_TIMEOUT -b $WORKDIR/bugs/$ORACLE -s $WORKDIR/scratch/$ORACLE -l $WORKDIR/logs/$ORACLE -c $WORKDIR/$FUSION_FUNCTONS -o $ORACLE "$COMMAND" /app/semantic-fusion-seeds/$LOGIC/$ORACLE
timeout 1h python3 yinyang/bin/yinyang -t $SMT_TIMEOUT -b $WORKDIR/bugs/$ORACLE -s $WORKDIR/scratch/$ORACLE -l $WORKDIR/logs/$ORACLE -o $ORACLE "$COMMAND" /app/semantic-fusion-seeds/$LOGIC/$ORACLE

/app/coverage.sh $2 $WORKDIR
