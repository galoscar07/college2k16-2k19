%Sa se interclaseze fara pastrarea dublurilor doua liste sortate
%Teste:
%[1 2 3 5 7] [2 4 6 8] -> [1 2 3 4 5 6 7 8]
%[1 2 3 4 5] [1 2 3 4 5] ->[1 2 3 4 5]
%[1 2 3 4 5] [6 7 8] ->[1 2 3 4 5 6 7 8]
%[1 2 3 4] [2 3 4 5 6] ->[1 2 3 4 5 6]

%merge(L1: List, L2: List, R: List)
%merge(i,i,o) FLOW MODEL
merge([],L,L):-!.
merge(L,[],L):-!.
merge([H|T],[H1|T1],[H|L]):-H<H1,!,
                            merge(T,[H1|T1],L).
merge([H|T],[H1|T1],[H1|L]):-H>H1,!,
                            merge([H|T],T1,L).
merge([H|T],[H1|T1],[H|L]):-H=H1,!,
                            merge(T,T1,L).
                            
%tests
test1():-merge([1,2,3,5,7],[2,4,6,8],[1,2,3,4,5,6,7,8]).
test2():-merge([1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]).
test3():-merge([1,2,3,4,5],[6,7,8],[1,2,3,4,5,6,7,8]).
test4():-merge([1,2,3,4],[2,3,4,5,6],[1,2,3,4,5,6]).