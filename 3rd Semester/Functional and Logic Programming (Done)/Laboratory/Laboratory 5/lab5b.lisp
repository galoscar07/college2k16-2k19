(defun assoc(l s)
(cond
((null l) nil)
((null s) nil)
(t(cons (cons(car(l) car(s))) assoc(cdr(l) cdr(s))))
)
)

(assoc (list 1 2 3) (list 4 5 6))