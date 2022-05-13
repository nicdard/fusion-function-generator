#!/bin/bash

# Reducing with ddsmt
FILE=$1

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

if [ -f "check-crash.sh" ]
then
  chmod +x check-crash.sh
else
  exit 1
fi

# install ddsmt.
pip3 install ddsmt
python3 -m ddsmt --version
python3 -m ddsmt -v $FILE $FILE.reduced check-crash.sh &
