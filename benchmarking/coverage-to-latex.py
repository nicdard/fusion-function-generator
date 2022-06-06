#!/usr/bin/env python

import json
from pathlib import Path
from string import Template

import re

inputs = [
  "vanilla-1h.json",
  "ffg-1h.json",
  "ffg-1h-2.json",
  "ffg-2h-2.json",
  "vanilla-2h.json",
  "ffg-2h.json",
  "ffg-1h-5.txt.json",
  "ffg-2h-5.txt.json",
]

by_logic = {}
logics = set()
clis = set()
benchmarks = set()
oracles = set()
for i in inputs:
    path = Path('./' + i)
    # Read the configuration first.
    summary = json.loads(path.read_text())
    for o in summary:
        LOGIC = o["logic"]
        logics.add(LOGIC)
        if LOGIC not in by_logic:
          by_logic[LOGIC] = {}
        CLI = o["solver_cli"].split(" ")[0].upper()
        clis.add(CLI)
        if CLI not in by_logic[LOGIC]:
          by_logic[LOGIC][CLI] = {}
        FUSION_FUNCTION = o["fusion_functions"] + " - " + o["solver_timeout"]
        benchmarks.add(FUSION_FUNCTION)
        if FUSION_FUNCTION not in by_logic[LOGIC][CLI]:
          by_logic[LOGIC][CLI][FUSION_FUNCTION] = {}
        ORACLE = o["oracle"]
        oracles.add(ORACLE)
        if ORACLE not in by_logic[LOGIC][CLI][FUSION_FUNCTION]:
          by_logic[LOGIC][CLI][FUSION_FUNCTION][ORACLE] = {
            "l": [ ], "f": [], "b": []
          }
        by_logic[LOGIC][CLI][FUSION_FUNCTION][ORACLE]["l"] = { "perc": o["coverage"]["line_percent"], "max": False }
        by_logic[LOGIC][CLI][FUSION_FUNCTION][ORACLE]["f"] = { "perc": o["coverage"]["function_percent"], "max": False }
        by_logic[LOGIC][CLI][FUSION_FUNCTION][ORACLE]["b"] = { "perc": o["coverage"]["branch_percent"], "max": False }

with open('./latex.output.txt', 'w') as file:

  solvers = sorted(clis)
  benchmarks = sorted(benchmarks)
  oracles = sorted(oracles)
  
  solver_headlines = [ f"  \\textbf{{{solver}}} & \\textit{{{benchmarks[0].replace('/app/fusion_functions/', 'FFG-').replace('.txt', '').replace('vanilla-yinyang', 'Vanilla')}}} \\\\" for solver in solvers ]
  benchmark_headlines = [ f"              & \\textit{{{benchmark.replace('/app/fusion_functions/', 'FFG-').replace('.txt', '').replace('vanilla-yinyang', 'Vanilla')}}} \\\\" for benchmark in benchmarks[1:] ]
  headlines = []
  for solver in solver_headlines:
    headlines.append(solver)
    headlines = headlines + benchmark_headlines

  logics = sorted(logics)
  groups = [logics[n:n + 2] for n in range(0, len(logics), 2)]

  for group in groups:
    # Each group has an headline
    table = [
      "%-------------------",
      "\\begin{tabular}{l r}",
      "  \\\\",  
      "  \\\\",  
      "  \\\\",
      *headlines,
      "\\end{tabular}",
    ]
    
    content = []
    for logic in group:
      data = []
      for solver in solvers:
        for oracle in oracles:
          print(oracle)
          l = 0
          f = 0
          b = 0
          for benchmark in benchmarks:
            bench = by_logic[logic][solver][benchmark][oracle]
            if bench['l']['perc'] > l:
              l = bench['l']['perc']
            if bench['f']['perc'] > f:
              f = bench['f']['perc']
            if bench['b']['perc'] > b:
              b = bench['b']['perc']
            print(f"{logic} {solver} {benchmark} {oracle}")
          for benchmark in benchmarks:
            print(bench['l']['perc'], bench['l']['max'])
            bench = by_logic[logic][solver][benchmark][oracle]
            if bench['l']['perc'] == l:
              bench['l']['max'] = True
            if bench['f']['perc'] == f:
              bench['f']['max'] = True
            if bench['b']['perc'] == b:
              bench['b']['max'] = True
          
        for benchmark in benchmarks:
          bench = by_logic[logic][solver][benchmark]
          data_line = []
          for oracle in oracles:
            print(f"{logic} {solver} {benchmark} {oracle}")
            b = bench[oracle]

            def cell(d):
              return f" \ccell[gray]{{0.9}}{{\\textit{{{d['perc']}}}}}" if d['max'] else f"\\textit{{{d['perc']}}}"
            
            data_line.append(f"{cell(b['l'])} & {cell(b['f'])} & {cell(b['b'])}")
          data.append("      " + (" & ".join(data_line)) + " \\\\") 

      logic_name = logic.replace('_', '\_')
      content = content + [
        "\\begin{tabular}{c c c c c c}", 
        f"  \\multicolumn{{6}}{{c}}{{\\textbf{{{logic_name}}}}} \\\\",
        "   \\cline{2-5}",
        f"  \\multicolumn{{3}}{{c}}{{SAT}} & \\multicolumn{{3}}{{c}}{{UNSAT}} \\\\",
        "   \\hline",
        "  \\textit{l} & \\textit{f} & \\textit{b} & \\textit{l} & \\textit{f} & \\textit{b} \\\\",
        *data,
        "\\end{tabular}",
      ]
    table = '\n'.join(table + content)
    print(table, file=file)
    print('\\\\', file=file)
