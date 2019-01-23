%3. a. Merge two sorted lists with removing the double values.
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
test1():-merge([1,2,3,5,7],[2,4,6,8],[1,2,3,4,5,6,7,8]),
        merge([1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]),
        merge([1,2,3,4,5],[6,7,8],[1,2,3,4,5,6,7,8]).
                            
