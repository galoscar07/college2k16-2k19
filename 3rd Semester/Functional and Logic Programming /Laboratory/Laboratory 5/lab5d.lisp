(defun lungime(l)
	(cond
		(( null l ) 0 )
		(( atom (car l)) ((+(lungime(cdr l)) 1))
		(t( + (lungime (car l))(lungime(cdr l))))
	)
    (format t "~% Number is ~d" lungime(l))
)