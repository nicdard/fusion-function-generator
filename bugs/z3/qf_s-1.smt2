(declare-fun a () String)
(declare-fun b () String)
(declare-fun c () String)
(declare-fun d () String)
(declare-fun e () String)
(declare-fun f () String)
(assert
  (and
    (and
      (= b "\u{54}\u{68}\u{65}\u{20}\u{6d}\u{64}\u{35}\u{20}\u{63}\u{68}\u{65}\u{63}\u{6b}\u{73}\u{75}\u{6d}\u{20}\u{6f}\u{66}\u{20}\u{74}\u{68}\u{65}\u{20}\u{66}\u{69}\u{6c}\u{65}\u{20}\u{69}\u{73}\u{20}")
      (= d "\u{3c}\u{62}2f}\u{3e}")
      (= c (str.++ b a))
      (= e (str.++ c d))
      (str.in_re e
        (re.++
          (re.* re.allchar)
          (re.++
            (str.to_re "\u{5c}\u{3c}\u{53}\u{43}\u{52}\u{49}\u{50}\u{54}")
            (re.* re.allchar)))))
    (and
      (and
        (not
          (=
            (str.in_re f
              (re.++
                (re.* re.allchar)
                re.allchar
                (re.* re.allchar)
                (str.to_re (str.++ "A" (str.++ "A" "B")))
                (re.* re.allchar)
                (str.to_re "C")
                (re.* re.allchar)))
            (str.in_re f
              (re.++
                (re.* re.allchar)
                (str.to_re (str.++ "A" "A"))
                re.allchar
                (str.to_re (str.++ "B" "C"))
                (re.* re.allchar)))))
        (not
          (=
            (str.in_re f
              (re.++
                (re.* re.allchar)
                re.allchar
                re.allchar
                re.allchar
                (str.to_re (str.++ "A" (str.++ "A" (str.++ "B" "C"))))
                (re.* re.allchar)))
            (str.in_re f
              (re.++
                (re.* re.allchar)
                re.allchar
                (re.* re.allchar)
                (str.to_re (str.++ "A" (str.++ "A" "B")))
                (re.* re.allchar)
                (str.to_re "C")
                (re.* re.allchar)))))))))
(check-sat)

; When executed with z3 smt.string_solver=z3str3 
; 
; sat
; ast_manager LEAKED: 24
; Leaked: Char[84]
; id: 122
; Leaked: Char[73]
; id: 298
; Leaked: Char[92]
; id: 231
; Leaked: Char[82]
; id: 297
; Leaked: true
; id: 1
; Leaked: Char[66]
; id: 276
; Leaked: Char[67]
; id: 278
; Leaked: Char[65]
; id: 134
; Leaked: Char[83]
; id: 188
; Leaked: Char[60]
; id: 277
; Leaked: Char[80]
; id: 299
