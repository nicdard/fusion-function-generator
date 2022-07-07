; set-logic NRA doesn't affect the output
(set-logic NRA)
(declare-fun a () Real) 
(declare-fun b () Real) 
(declare-fun c () Real) 
(declare-fun d () Real) 
(assert 
    (forall 
        ((e Real)) 
        (and 
            (= a 1) 
            (< c d)
            (or 
                (> e a)
                (= 1 (* b e))
            )
            (= 0 (/ (* (+ d 1) (+ a d)) a))         
        ) 
    ) 
)
(assert (= 0 (/ b c 0)))
(check-sat)

; $ z3
; sat, expected unsat
