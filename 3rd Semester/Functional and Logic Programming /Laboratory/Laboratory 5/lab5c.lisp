(defun counting (l e)
(cond
    ((null l) nil)
    ((atom (car l))(counting())
    (t(cons (car l)(substitute(cdr l))))
)
)
