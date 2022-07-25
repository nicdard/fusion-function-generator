#!/bin/bash

source $1 

TIMEOUT=15
# BAD="./$1"
# GOOD=$2
FILE=$2

echo $GOOD

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "invalid args"
    rm -f $$bad.out $$good.out
    exit 10
fi

echo "A" | timeout -s 9 $TIMEOUT $GOOD $FILE >& $$good.out
ret=$?
if grep -q "Parse Error" $$good.out; then
    echo 2
    rm -f $$bad.out $$good.out
    exit 2
fi
if  grep -q "(error" $$good.out; then
    echo 3
    rm -f $$bad.out $$good.out
    exit 3
fi
if [[ $ret == 124 ]]; then
    echo 4
    rm -f $$bad.out $$good.out
    exit 4
fi

echo "A" | timeout -s 9 $TIMEOUT $BAD $FILE >& $$bad.out
ret=$?

if grep -q "invalid model" $$bad.out; then
    echo bug_invalid
    rm -f $$bad.out $$good.out
    exit 0
fi


if grep -q "Parse Error" $$bad.out; then
    echo 5
    rm -f $$bad.out $$good.out
    exit 5
fi
if grep -q "(error" $$bad.out; then
    echo 6
    rm -f $$bad.out $$good.out
    exit 6
fi

if [[ $ret == 139 ]]; then
    echo bug_crash
    rm -f $$bad.out $$good.out
    exit 0
fi

if grep -q "unknown" $$bad.out; then
    echo 7
    rm -f $$bad.out $$good.out
    exit 7
fi

if [[ $ret == 124 ]]; then
    echo 8
    rm -f $$bad.out $$good.out
    exit 8
fi

if  grep -q "ASSERTION VIOLATION" $$bad.out; then
    echo bug_assertion
    rm -f $$bad.out $$good.out
    exit 0
fi

if  grep -q "LEAKED" $$bad.out; then
    echo bug_leaked
    rm -f $$bad.out $$good.out
    exit 0
fi

if egrep "^sat$" $$bad.out ; then
    if egrep "^unsat$" $$good.out ; then
        echo unsat2sat
        rm -f $$bad.out $$good.out
        exit 0
    fi
fi

if egrep "^unsat$" $$bad.out ; then
    if egrep "^sat$" $$good.out ; then
        echo sat2unsat
        rm -f $$bad.out $$good.out
        exit 0
    fi
fi

echo 1
rm -f $$bad.out $$good.out
exit 1