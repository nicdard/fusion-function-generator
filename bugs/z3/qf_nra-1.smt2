; Commit: 40fe472e9555ee5a67b64f70c71577c9a2941bd7
; OS: Ubuntu 20.04

(declare-fun s () Real)
(declare-fun c () Real)
(assert 
  (and 
    (< 0 s) 
    (< (- 0.0 (- 0.0 (- 0.0 (+ c (* 24 (- 1 (* 30 57 43 (+ 7 12 1 0)))))))) 0) 
    (< (* 1.0 (+ 0.0 (- 1)) (- 0.0 (+ c (* 24 (- 0 (* 30 57 43 (+ 7 12 1 0))))))) 0.0) 
    (= 
      0.0 
      (+ 1.0 
        (* 
          (- 1) (- 0.0 (+ c (* 24 (- 0 (* 30 57 43 (+ 7 12 1 0)))))) 
          (- 0.0 (+ c (* 24 (- 10 (* 30 57 43 (+ 7 12 1 (- 2))))))) 
          (- 0.0 (+ c (* 24 (- 10 (* 30 57 43 (+ 7 12 1 (- 2))))))) 
          (- 0.0 (+ c (* 24 (- 10 (* 30 57 43 (+ 7 12 1 (- 2)))))))
        ) 
        (* 
          s s 117187 
          (- s (+ c (* 24 (- 10 (* 30 57 43 (+ 7 12 1 (- 2))))))) 
          (- s (+ c (* 24 (- 10 (* 30 57 43 (+ 7 12 1 (- 2))))))) 
          (- s (+ c (* 24 (- 10 (* 30 (+ (- 5) (* 57 43 (+ 7 12 1 (- 2))))))))) 
          (- s (+ c (* 24 (- 10 (* 30 (+ (- 5) (* 57 43 (+ 7 12 1 (- 2)))))))))
        )
      )
    )
  )
)
(check-sat)


; AddressSanitizer:DEADLYSIGNAL
; =================================================================
; ==29110==ERROR: AddressSanitizer: SEGV on unknown address 0x6270003201e8 (pc 0x555bd10628b3 bp 0x6270003201e8 sp 0x7fffeb825700 T0)
; ==29110==The signal is caused by a READ memory access.
;     #0 0x555bd10628b2 in algebraic_numbers::manager::imp::set(algebraic_numbers::anum&, algebraic_numbers::anum const&) (/usr/bin/z3+0x4ba38b2)
;     #1 0x555bd0716081 in nlsat::interval_set_manager::peek_in_complement(nlsat::interval_set const*, bool, algebraic_numbers::anum&, bool) (/usr/bin/z3+0x4257081)
;     #2 0x555bd06d1897 in nlsat::solver::imp::search() (/usr/bin/z3+0x4212897)
;     #3 0x555bd06d49f4 in nlsat::solver::imp::search_check() (/usr/bin/z3+0x42159f4)
;     #4 0x555bd06c2216 in nlsat::solver::imp::check() (/usr/bin/z3+0x4203216)
;     #5 0x555bceac6342 in nlsat_tactic::imp::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x2607342)
;     #6 0x555bceac7bcc in nlsat_tactic::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x2608bcc)
;     #7 0x555bcfa0a010 in cleanup_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354b010)
;     #8 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #9 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #10 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #11 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #12 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #13 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #14 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #15 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #16 0x555bcfa0b052 in try_for_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c052)
;     #17 0x555bcfa166a4 in or_else_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x35576a4)
;     #18 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #19 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #20 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #21 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #22 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #23 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #24 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #25 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #26 0x555bcfa0b663 in cond_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x354c663)
;     #27 0x555bcfa15291 in and_then_tactical::operator()(ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x3556291)
;     #28 0x555bcf9cf60c in exec(tactic&, ref<goal> const&, sref_buffer<goal, 16u>&) (/usr/bin/z3+0x351060c)
;     #29 0x555bcf9d1164 in check_sat(tactic&, ref<goal>&, ref<model>&, labels_vec&, obj_ref<app, ast_manager>&, obj_ref<dependency_manager<ast_manager::expr_dependency_config>::dependency, ast_manager>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) (/usr/bin/z3+0x3512164)
;     #30 0x555bcf8e2cfa in (anonymous namespace)::tactic2solver::check_sat_core2(unsigned int, expr* const*) (/usr/bin/z3+0x3423cfa)
;     #31 0x555bcf879a9c in solver_na2as::check_sat_core(unsigned int, expr* const*) (/usr/bin/z3+0x33baa9c)
;     #32 0x555bcf889436 in combined_solver::check_sat_core(unsigned int, expr* const*) (/usr/bin/z3+0x33ca436)
;     #33 0x555bcf8db26d in solver::check_sat(unsigned int, expr* const*) (/usr/bin/z3+0x341c26d)
;     #34 0x555bcf7d5f7c in cmd_context::check_sat(unsigned int, expr* const*) (/usr/bin/z3+0x3316f7c)
;     #35 0x555bcf778eb4 in smt2::parser::operator()() (/usr/bin/z3+0x32b9eb4)
;     #36 0x555bcf724cd8 in parse_smt2_commands(cmd_context&, std::istream&, bool, params_ref const&, char const*) (/usr/bin/z3+0x3265cd8)
;     #37 0x555bccb6cce2 in read_smtlib2_commands(char const*) (/usr/bin/z3+0x6adce2)
;     #38 0x555bccb414c8 in main (/usr/bin/z3+0x6824c8)
;     #39 0x7fbf8d4ca0b2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x240b2)
;     #40 0x555bccb5cc1d in _start (/usr/bin/z3+0x69dc1d)
; 
; AddressSanitizer can not provide additional info.
; SUMMARY: AddressSanitizer: SEGV (/usr/bin/z3+0x4ba38b2) in algebraic_numbers::manager::imp::set(algebraic_numbers::anum&, algebraic_numbers::anum const&)
; ==29110==ABORTING
; 