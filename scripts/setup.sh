#!/bin/bash

# The file name of the fusion functions is given
FUSION_FUNCTONS=fusion_functions_$1.txt
# Timeout for the SMT solver
TIMEOUT=$2
# The command line option to z3 is given as second argument for the script.
OPTIONS=$3

echo =====================
echo "Download Seeds"
if [ -d "./semantic-fusion-seeds-master" ]
then
	echo "...seeds folder exists, skip."
else
	wget -O semantic-fusion-seeds.zip https://github.com/testsmt/semantic-fusion-seeds/archive/refs/heads/master.zip
	unzip semantic-fusion-seeds.zip
	rm semantic-fusion-seeds.zip 
	# Fix missclassification bug
	mv semantic-fusion-seeds-master/LIA/unsat/NUM899-1.smt2 semantic-fusion-seeds-master/LIA/sat/NUM899-1.smt2
	mv semantic-fusion-seeds-master/LIA/sat/NUM889-1.smt2  semantic-fusion-seeds-master/LIA/unsat/NUM889-1.smt2
fi

echo
echo =====================
echo "Download Yinyang"
if [ -d "./yinyang-0.3.0" ]
then
	echo "...yinyang folder exists, skip."
else
	wget -O yinyang-0.3.0.zip https://github.com/nicdard/yinyang/archive/refs/heads/feat/allow-multiple-constants.zip
	unzip yinyang-0.3.0.zip -d yinyang-0.3.0
	pip3 install antlr4-python3-runtime==4.9.2

	# Verify yinyang works
	python3 yinyang-0.3.0/yinyang-feat-allow-multiple-constants/bin/yinyang --version
	rm yinyang-0.3.0.zip
fi

echo
echo ======================
echo "Download z3 latest"
if [ -d "./z3-4.8.17-x64-glibc-2.31" ]
then
	echo "...z3-4.8.17-x64-glibc-2.31 folder exists, skip."
else
	wget https://github.com/Z3Prover/z3/releases/download/z3-4.8.17/z3-4.8.17-x64-glibc-2.31.zip
	unzip z3-4.8.17-x64-glibc-2.31.zip
	rm z3-4.8.17-x64-glibc-2.31.zip
fi
Z3=$(readlink -f z3-4.8.17-x64-glibc-2.31/bin/z3)
# Verify z3 works
$Z3 -h

echo
echo ======================
echo "Download CVC5 latest"
if [ -f "./cvc5-Linux" ]
then
	echo "...cvc5-Linux exists, skip."
else
	wget https://github.com/cvc5/cvc5/releases/download/cvc5-1.0.0/cvc5-Linux
	chmod +x cvc5-Linux
	# Verify cvc5 works
	./cvc5-Linux -h
fi

pwd
sleep 5s

echo ======================
echo "Setup test folder..."
TIMESTAMP=$(date '+%s')
mkdir $TIMESTAMP
touch $TIMESTAMP/cmd.txt
ls

THEORIES="LIA LRA NRA QF_LIA QF_LRA QF_NRA"

echo "	...using theories: "
echo $THEORIES

for theory in $THEORIES
do
	sleep 2s
	echo "Starting test for theory $theory"
	DIR=$TIMESTAMP/$theory
	mkdir $DIR
	BUGS=$TIMESTAMP/$theory/bugs
	mkdir $BUGS
	mkdir $BUGS/sat
	mkdir $BUGS/unsat
	SCRATCH=$TIMESTAMP/$theory/scratch
	mkdir $SCRATCH
	LOG=$TIMESTAMP/$theory/log
	mkdir $LOG

	SAT_CMD="python3 yinyang-0.3.0/yinyang-feat-allow-multiple-constants/bin/yinyang -t $TIMEOUT -b $BUGS/sat -s $SCRATCH -l $LOG -c $FUSION_FUNCTONS -o sat "$Z3 $OPTIONS" semantic-fusion-seeds-master/$theory/sat &"
	$SAT_CMD
	SAT_PID=$!
	
	UNSAT_CMD="python3 yinyang-0.3.0/yinyang-feat-allow-multiple-constants/bin/yinyang -t $TIMEOUT -b $BUGS/unsat -s $SCRATCH -l $LOG -c $FUSION_FUNCTONS -o unsat "$Z3 $OPTIONS" semantic-fusion-seeds-master/$theory/unsat &"
	$UNSAT_CMD
	UNSAT_PID=$!
	
	echo $SAT_CMD >> $TIMESTAMP/cmd.txt
	echo $SAT_PID >> $TIMESTAMP/cmd.txt
	echo $SAT_PID >> $TIMESTAMP/processes.txt
	
	echo $UNSAT_CMD >> $TIMESTAMP/cmd.txt
	echo $UNSAT_PID >> $TIMESTAMP/cmd.txt
	echo $UNSAT_PID >> $TIMESTAMP/processes.txt

done
