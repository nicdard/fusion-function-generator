#!/bin/bash

# Reducing with ddsmt when the solver wait for user input.
FILE=$1


# install ddsmt.
pip3 install ddsmt
python3 -m ddsmt --version
# make sure resut_differ.py is executable.
chmod +x result_differs.py
python3 -m ddsmt -v $FILE $FILE.reduced result_differs_with_timeout.py
