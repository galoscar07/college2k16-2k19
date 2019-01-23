%b.For a heterogeneous list, formed from integer numbers and list of numbers, merge all sublists with removing the double values. 

% merge(L1: list, L2: list, L3: list)
% merge(i, i, o) FLOW MODEL
merge([],[],[]):-!.
merge([],L,L):-!.
merge(L,[],L):-!.
merge([H|T],[H1|T1],[H|L]):-H<H1,!,
                            merge(T,[H1|T1],L).
merge([H|T],[H1|T1],[H1|L]):-H>H1,!,
                            merge([H|T],T1,L).
merge([H|T],[H1|T1],[H|L]):-H=H1,!,
                            merge(T,T1,L).
                            
    
%mainMerge(L:List, LR:List)
%mainMerge(i,o) FLOW MODEL
mainMerge([],[]).
mainMerge([H|T],LR):-number(H),
                    mainMerge(T,LR).
mainMerge([H|T],R):-is_list(H),
                    mainMerge(T,R1),
                    merge(H,R1,R).


test():-mainMerge([1,[2,3],4,5,[1,4,6],3,[1,3,7,9,10,11],5,[1,11],8],[1,2,3,4,6,7,9,10,11]),
        mainMerge([1,[2,3],4,5,[1,4,6],3,[1,3,7,9,10,11,12,14],5,[1,11],8],[1,2,3,4,6,7,9,10,11,12,14]),
        mainMerge([1,[1],[1,2],3,4,5,[6,67]],[1,2,6,67]).
   