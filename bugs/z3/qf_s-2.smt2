(declare-fun s () String)
(declare-fun r () String)
(assert 
  (and 
    (= 
      "\u{2f}" (str.substr s 0 (str.len "lo"))) 
      (str.in_re r (re.++ (re.* re.allchar) (re.++ (str.to_re "\u{2f}\") (re.* re.allchar)))
    ) 
    (= 
      (str.substr r 0 (str.len (str.++ r ""))) (str.++ (str.++ (str.substr s 0 (str.len "lo")) s) 
      (str.substr s 0 1))
    )
  )
)
(check-sat)


; $ z3
; sat, expected unsat
