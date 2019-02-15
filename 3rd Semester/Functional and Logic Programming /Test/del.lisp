;Dandu-se o lista liniara, sa se stearga toate secventele de valori numerice consecutive. De exemplu: 
;(1 2 c 4 6 7 8 i 10 j) --> (c 4 i 10 j)
;Teste:
;(1 2 C 4 6 7 8 I 10 J) -> (C 4 I 10 J)
;(1 2 3 5 7 8 9 10) -> (5)
;(A B 4 C S 5 6 B) -> (A B 4 C S B)
;(1 A 2 B 3 4 C D 5 6 7 E) -> (1 A 2 B C D E)
; echivalentul cu (< A B), doar ca are cazuri speciale pt a = NIL sau b=NIL
(DEFUN lt(A B)
  (COND
    ((NULL B) NIL)
    ((NULL A) NIL)
    ((< A B) T)
    (T NIL)
  )
)
; in E retin ultimul element scos din lista
(DEFUN elim(L E)
  (COND
    ((NULL L) NIL)
    (( lt E (CAR L) ) ( elim (CDR L) (CAR L) ) ) ; E < L[i] => E = L[i] si apelez elim(L[i+1..],E)
    (( lt (CAR L) (CAR (CDR L)) ) ( elim (CDR (CDR L)) (CAR(CDR L)))); L[i] < L[i+1] =>  E = L[i+1] si apelez elim(L[i+2..],E)
    (T ( CONS (CAR L) (elim (CDR L) (CAR L)) ) ); default => adaug L[i] in lista finala si apelez elim(L[i+1],E)
  )
)

(DEFUN elim_main(L)
  (elim L (CAR L) ) ; initializez E cu (CAR L)
)

( elim_main '(1 2 3 4 3 2 5 7 8 5) ) ; => (3 5)