#!/bin/bash

FILE=$1


function runZ3() {
  echo "Download $1$2"
  if [ -d "./$1$2" ]
  then
    echo "...$1-x64-glibc-2.31 folder exists, skip."
  else
    wget https://github.com/Z3Prover/z3/releases/download/$1/$1$2.zip -q
    unzip $1$2.zip >/dev/null
    rm $1$2.zip >/dev/null
  fi
  Z3=$(readlink -f $1$2/bin/z3)
  $Z3 $FILE
  # Comment the following cleanup line to speed up multiple calls to this script.
  rm -r $1$2
}

versions="z3-4.8.17 z3-4.8.16 z3-4.8.15 z3-4.8.14 z3-4.8.13 z3-4.8.12 z3-4.8.11"
suffix="-x64-glibc-2.31"
for version in $versions
do
  runZ3 $version $suffix
done

version="z3-4.8.10"
suffix="-x64-ubuntu-18.04"
runZ3 $version $suffix

old_versions="z3-4.8.9 z3-4.8.8 z3-4.8.7 z3-4.8.6"
suffix="-x64-ubuntu-16.04"
for version in $old_versions
do
  runZ3 $version $suffix
done
