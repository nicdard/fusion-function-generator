# Discovered bugs
## Z3
| Input                        | Logic  | Kind                | Issue                                                                       | Date     |
|------------------------------|--------|---------------------|-----------------------------------------------------------------------------|----------|
| [NRA 1](z3/nra-1.smt2)       | NRA    | Soundness           | [#2650](https://github.com/Z3Prover/z3/issues/2650#issuecomment-1113448263) | 30/04/22 |
| [NRA 2](z3/nra-2.smt2)       | NRA    | Soundness           | [#2650](https://github.com/Z3Prover/z3/issues/2650#issuecomment-1126688235) | 14/05/22 |
| [QF_NRA 1](z3/qf_nra-1.smt2) | QF_NRA | Segfault            | [#6044](https://github.com/Z3Prover/z3/issues/6044)                         | 20/05/22 |
| [QF_S 1](z3/qf_s-1.smt2)     | QF_S   | Memory Leak         | [#6076](https://github.com/Z3Prover/z3/issues/6076)                         | 04/06/22 |
| [QF_BV 1](z3/qf_bv-1.smt2)   | QF_BV  | Assertion Violation | [#6143](https://github.com/Z3Prover/z3/issues/6143)                         | 07/07/22 |
| [QF_S 2](z3/qf_s-2.smt2)     | QF_S   | Soundness           | [#6159](https://github.com/Z3Prover/z3/issues/6159)                         | 14/07/22 |
| [QF_BV 2](z3/qf_bv-2.smt2)   | QF_BV  | Assertion Violation | [#6180](https://github.com/Z3Prover/z3/issues/6180)                         | 21/07/22 |
