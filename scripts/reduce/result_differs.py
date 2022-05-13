#!/usr/bin/env python3

import signal
import subprocess
import sys


def handler(sig, frame):
    print("Aborted")
    sys.exit(1)


signal.signal(signal.SIGTERM, handler)


def run(cmd):
    cmd = cmd + [sys.argv[1]]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.stdout.decode('utf8').strip()


A = run(['./z3-4.8.17-x64-glibc-2.31/bin/z3'])
B = run(['./cvc5-Linux'])

if A not in ['sat', 'unsat']:
    print(f'Unexpected output for A: {A}')
    sys.exit(2)

if B not in ['sat', 'unsat']:
    print(f'Unexpected output for B: {B}')
    sys.exit(2)

print(f'{A} / sat')
if A == B:
    sys.exit(0)
else:
    sys.exit(1)
