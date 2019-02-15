(defun remo(li el)
    (cond
        ((null li) nil)
        ((atom li) li)
        (T (mapcar #'(lambda(x) (remo x el)) (remove el li)))
    )
)