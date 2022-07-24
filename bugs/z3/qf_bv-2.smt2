(declare-const a (_ BitVec 1))
(declare-const _a (_ BitVec 2))
(declare-const b (_ BitVec 4))
(declare-const c (_ BitVec 16))
(declare-const d (_ BitVec 16))
(declare-const e (_ BitVec 16))
(declare-const f (_ BitVec 16))
(declare-const g (_ BitVec 31))
(declare-const h (_ BitVec 32))
(declare-const i (_ BitVec 32))
(declare-const cr (_ BitVec 32))
(assert (= c f))
(assert (= f (bvor f c)))
(assert 
    (bvule 
        (bvsub 
            (bvadd 
                (_ bv4270377 32) 
                ((_ zero_extend 30) _a)
                ((_ zero_extend 30) _a)
                ((_ zero_extend 16) f) 
                ((_ zero_extend 28) b)
                ((_ zero_extend 16) d) 
                i 
                ((_ zero_extend 16) e)
            ) 
            (_ bv4270344 32)
        ) 
        (_ bv423 32)
    )
)
(assert (distinct (_ bv1 2) _a))
(assert 
    (bvule 
        (bvadd 
            i 
            (_ bv4270377 32)
            ((_ zero_extend 16) d) 
            ((_ zero_extend 16) f) 
            ((_ zero_extend 30) _a)
            ((_ zero_extend 30) _a)
        ) 
        (_ bv4271190 32)
    ) 
)
(assert (bvule h (_ bv4271190 32)))
(assert (bvule i (_ bv846 32)))
(assert (distinct h (_ bv0 32)))
(assert (bvule (bvadd i (_ bv9 32)) (_ bv533898 32)))
(assert (bvule (bvsub (bvadd h (bvsub (_ bv1 32) cr)) (_ bv4270344 32)) (_ bv846 32)))
(assert (bvule ((_ zero_extend 31) a) (_ bv2 32)))
(assert (= (bvxor (bvnot (_ bv1 32)) (bvneg ((_ zero_extend 1) g))) ((_ zero_extend 16) f))) 
(assert (bvule (bvadd (_ bv4270382 32) ((_ zero_extend 16) d) ((_ zero_extend 16) c)) (_ bv4271190 32)))
(assert (bvule (bvadd cr (_ bv4270372 32)) (_ bv2135595 32)))
(assert (distinct d (_ bv0 16)))
(assert (distinct f (_ bv0 16)))
(check-sat)

; $ z3
; ASSERTION VIOLATION
; File: ../src/sat/sat_model_converter.cpp
; Line: 136
; sat || undef
; (C)ontinue, (A)bort, (S)top, (T)hrow exception, Invoke (G)DB
