%1a.Write a predicate to determine the lowest common multiple of a list formed from integer
%numbers. 
%gcd(X:number, Y:number, G: number)
%gcd(i, i, o) FLOW MODEL
gcd(X,Y,G) :- X=Y, G=X.
gcd(X,Y,G) :- X<Y, Y1 is Y-X, gcd(X,Y1,G).
gcd(X,Y,G) :- X>Y ,gcd(Y,X,G).

%lcm(X:number, Y:number, LCM: number
%lcm(i, i, o) FLOW MODEL
lcm(X,Y,LCM):-gcd(X,Y,GCD), LCM is X*Y//GCD.

%lcml(L:list, E:number)
%lcml(i,o) FLOW MODEL
lcml([N],N).
lcml([H|T],E):-lcml(T,R), lcm(R,H,E).

test_lcml():-lcml([1,2,3,4],12).