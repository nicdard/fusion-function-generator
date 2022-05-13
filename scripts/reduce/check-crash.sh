#!/bin/bash

Z3=$(readlink -f z3-4.8.17-x64-glibc-2.31/bin/z3)
timeout -s 9 15 $Z3 $1
ret=$?

if [[ $ret == 139 ]]; then
    exit 0
else
    exit 1
fi
