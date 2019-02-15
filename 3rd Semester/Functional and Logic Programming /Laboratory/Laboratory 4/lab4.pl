%Function to check if three points are collinear
% collinear(L1: list, L2: List, L3: List, E: Number)
% collinear(i,i,i,o) FLOW MODEL
%(Xc - Xa)/ (Xb - Xa) = (Yc - Ya)/ (Yb - Ya)
collinear([H1|T1],[H2|T2],[H3|T3],E):- (H3-H1)/(H2-H1)=:=(T3-T1)/(T2-T1),
                                        E is 1.
collinear([H1|T1],[H2|T2],[H3|T3],E):- (H3-H1)/(H2-H1)=\=(T3-T1)/(T2-T1),
                                        E is 0.
%minsert insereaza un element intr-o lista
minsert([], E, [E]).
minsert([H|T],E,[E,H|T]).
minsert([H|T],R,[H|Tr]):-minsert(T,E,Tr).

%permutarile elementelor unei liste
perm([], []).
perm([H|T],R):-perm(T,RT),
                minsert(RT,H,R).

%Combinations of k lists of a list
%combinations(L: list, K: Element, LR: List)
%combinations(i,i,o) FLOW MODEL
combinations([],0,[]).
combinations([H|T],N,[H|T1]):-N>0,
                              N1 is N-1,
                              combinations(T,N1,T1).
combinations([_|T],N,LR):-combinations(T,N,LR).

%Aranjamente de K elemente dintr-o lista L
arr(L,K,R):-comb(L,K,R1),
            perm(R1,R).

%oneSolution(L:List, E:Number, LR:List)
%oneSolution(i,i,o) FLOW MODEL
oneSol(L,E,RL):-arr(L,E,[H1,H2,H3|_]),
                collinear(H1,H2,H3,E).

%allSolutions(L:List, E:Number, RL:List)
%allSolutions(i,i,o) FLOW MODEL
allSolutions(L,E,R):-findall(RL, oneSolution(L,E,RL), R).
