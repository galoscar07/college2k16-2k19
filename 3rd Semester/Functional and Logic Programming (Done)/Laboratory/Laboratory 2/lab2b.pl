% 1b. Write a predicate to add a value v after 1-st, 2-nd, 4-th, 8-th, … element in a list.
% add(L:list, E:Number, P:Number, C:number, H:List)
% add(i,i,i,i,o) FLOW MODEL

add([],_,_,_,[]).
add([H|T],E,P,C,[H,E|TR]):-P=:=C, 
                         C1 is C+1,
                         P1 is P*2,
                         add(T,E,P1,C1,TR).
add([H|T],E,P,C,[H|TR]):-P=\=C,
                         C1 is C+1,
                         add(T,E,P,C1,TR).
                         
teste_add():-add([1,2,3,4],10,1,1,[1,10,2,10,3,4,10]),
            add([1],5,1,1,[1,5]),
            add([1,2,3,4,5],5,1,1,[1,5,2,5,3,4,5,5]).