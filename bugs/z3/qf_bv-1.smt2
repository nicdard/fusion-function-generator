(declare-const a (_ BitVec 2))
(declare-const b (_ BitVec 8))
(declare-const c (_ BitVec 32))
(declare-const d (_ BitVec 32))
(assert (= (_ bv1 1) ((_ extract 0 0) a)))
(assert (bvslt (_ bv4294967295 32) (bvsub c (_ bv721 32))))
(assert (bvule (bvadd c (_ bv143554326 32)) (_ bv143555047 32)))
(assert (bvult (_ bv143555038 32) (bvadd c (_ bv143554326 32))))
(assert
    (bvule 
        (bvsub 
            (bvadd d (bvshl (bvadd (_ bv1 32) (bvsub (_ bv1 32) (bvadd ((_ zero_extend 24) b) d))) (_ bv1 32)))
            (_ bv3 32)
        )
        (_ bv20903423 32)
    )
) 
(assert (bvult (_ bv1 32) (bvneg (bvadd d d (_ bv3 32) ((_ zero_extend 24) b)))))
(check-sat)

; $ z3
; ASSERTION VIOLATION
; File: ../src/sat/sat_simplifier.cpp
; Line: 1815
; c2.contains(~l)
; (C)ontinue, (A)bort, (S)top, (T)hrow exception, Invoke (G)DB
