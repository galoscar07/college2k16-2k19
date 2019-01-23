(defun addTwice(l p pc)
(cond
((null l) nil)
((equal 0(- p pc))(cons (car l) (cons (car l) (cdr l))))
(t(cons (car l)(addTwice (cdr l) p (+ 1 pc))))
)
)

(defun addTwiceMain (l p)
(addTwice l p 1)
)

(addTwiceMain (list 10 20 30 40 50) 3)