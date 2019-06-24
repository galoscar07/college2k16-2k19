disp("Hello World");

% Problem from previous lab: Find LU decomposition of the following matrix using
%Doolittle method.
% maybe exam so put it in the paper
% it computes the L and U where L contains only emels under "diagonala 
%principala" and on dp has only value 1 and U have only over dp not any elem on 
%the dp

A = [6 2 1 -1; 2 4 1 0; 1 1 4 -1; -1 0 -1 3];
[L, U] = lu(A);

function [L, U] = my_lu(A)
    [n, ~] = size(A);
    I = eye(n);
    L = I;
    for k=1:n-1
        t = zeros(n,1);
        t(k+1:n) = A(k+1:n, k) ./ A(k, k);
        es = zeros(1, n);
        es(k) = 1;
        A = (I - t * es) * A;
        L= L * (I+t*es);
    end
    U = A;
endfunction

[L,U] = my_lu(A);

A = diag(-ones(5,1),-1) +  diag(-ones(5,1),1) + 3 * eye(6)


disp("Problem 1 Lab 11");
function x_new=gs(A, b, er)
    n = length(b);
    x_old = b;
    x_new = b;
    for i=1:n
        x_new(i) = 1/A(i,i) * (b(i)-A(i,1:i-1) * x_new(1:i-1) - A(i,i+1:n) * x_old(i+1:n));
    end
    while norm(x_new - x_old) >= er
        x_old = x_new
        for i=1:n
           x_new(i) = 1/A(i,i) * (b(i)-A(i,1:i-1) * x_new(1:i-1) - A(i,i+1:n) * x_old(i+1:n));
        end
    end
end
A = diag(-ones(5,1),-1) +  diag(-ones(5,1),1) + 3 * eye(6);
B = [2;1;1;1;1;2];
err = 10^-5;
gs(A, B, err)


%1) Jacobi: M=diag(diag(A)), N=M-A, T=M\N, c=M\b
function x_new=gs1(A, b, er)
    n = length(b);
    x_old = b;
    x_new = b;
    M = diag(diag(A));
    N = M - A;
    T = M \ N;
    C = M \ b;
    x_new = T * x_old + C;
    while norm(x_new - x_old) >= er
        x_old = x_new;
        x_new = T * x_old + C;
    end
end
gs1(A, B, err)


%2) G.S.: M=tril(A), -||-
function x_new=gs2(A, b, er)
    n = length(b);
    x_old = b;
    x_new = b;
    M = tril(A);
    N = M - A;
    T = M \ N;
    C = M \ b;
    x_new = T * x_old + C;
    while norm(x_new - x_old) >= er * (1-norm(T)) / norm(T)
        x_old = x_new;
        x_new = T * x_old + C;
    end
end
gs2(A, B, err)


%3) S.O.R.: M=diag(diag(A)) + omega * tril(A,-1), omega -> (0,2)
function x_new=gs3(A, b, er)
    n = length(b);
    x_old = b;
    x_new = b;
    omega = 1.2;
    M=diag(diag(A)) + omega * tril(A,-1);
    N = M - A;
    T = M \ N;
    C = M \ b;
    x_new = T * x_old + C;
    while norm(x_new - x_old) >= er
        x_old = x_new;
        x_new = T * x_old + C;
    end
end
gs3(A, B, err);

disp("Problem 2")
A = [3 1 1; -2 4 0; -1 2 6];
B = [12; 2; -5];
err = 10^5;

gs3(A, B, err)


