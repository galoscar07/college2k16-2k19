%multiply(L:list,k:number,R:list)
%multiply(i,i,o) FLOW MODEL
multiply([],_,[]).
multiply([H|T],K,[HR|TR]):-HR is K*H,
multiply(T,K,TR).