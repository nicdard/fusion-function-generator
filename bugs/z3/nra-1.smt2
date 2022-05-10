; not triggered with (set-logic NRA)
(declare-fun a () Real)
(declare-fun b () Real)
(declare-fun c () Real)
(declare-fun d () Real)
(assert
  (forall
    ((e Real))
    (and
      (< c 0)
      (= 0 (- e d (* a e e)))
      (= b (- e d (* a e e)))
      (= b
        (*
          (+ 1 (- (* d 160)) (- 2 (/ (- (- 33 c)) (- 49) 2)))
          (+ 1 (- (* d 160)) (- 2 (/ (- (- 33 c)) (- 49) 2)))
        )
      )
    )
  )
)
(assert (= 0 0))
; also triggered by (= 1 1) and (= 2 2), not by (= 3 3)
(check-sat)
