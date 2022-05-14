#!/bin/bash

# Reducing with ddsmt
FILE=$1

echo
echo ======================
echo "Download z3-4.8.17-x64-glibc-2.31"
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

# install ddsmt.
pip3 install ddsmt
python3 -m ddsmt --version
# make sure resut_differ.py is executable.
chmod +x result_differs.py
python3 -m ddsmt -v $FILE $FILE.reduced result_differs.py
