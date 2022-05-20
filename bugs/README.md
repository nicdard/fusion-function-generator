# Discovered bugs
## Z3
| Input                  | Configuration            | Logic | Kind      | Issue                                                                       | Date     |
|------------------------|--------------------------|-------|-----------|-----------------------------------------------------------------------------|----------|
| [NRA 1](z3/nra-1.smt2) | [config-1](config-1.txt) | NRA   | Soundness | [#2650](https://github.com/Z3Prover/z3/issues/2650#issuecomment-1113448263) | 30/04/22 |
| [NRA 2](z3/nra-2.smt2) | [config-2](config-2.txt) | NRA   | Soundness | [#2650](https://github.com/Z3Prover/z3/issues/2650#issuecomment-1126688235) | 14/05/22 |
| [QF_NRA 1](z3/qf_nra-1.smt2) | [config-3](config-3.txt) | QF_NRA | Segfault | [#6044](https://github.com/Z3Prover/z3/issues/6044)                   | 20/05/22 |
