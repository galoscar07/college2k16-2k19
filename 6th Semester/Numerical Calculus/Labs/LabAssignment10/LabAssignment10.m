disp("Hello World");
A = [1 0 0; 1 2 0; 1 2 3];
b = [1; 3; 6];

function x = forward_substitution(A, b)
    x = NaN(size(b));
    n = length(b);
    for i=1:n
        x(i) = 1 / A(i,i) * (b(i) - A(i, 1:(i-1)) * x(1:(i-1)));
    end
endfunction

forward_substitution(A, b)
    
B = [1 2 3; 0 1 2; 0 0 1];
c = [6;3;1];
    
function x = backword_substitution(A, b)
    x = NaN(size(b));
    n = length(b);
    for i=n:-1:1
        x(i) = 1 / A(i,i) * (b(i) - A(i, i+1:n) * x(i+1:n));
    end
endfunction

backword_substitution(B, c)

A = [1 1 1 1; 2 3 1 5; -1 1 -5 3; 3 1 7 -2];
b = [10; 31; -2; 18];

function x = gauss(A, b)
    n = length(b);
    for p = 1:n-1
        [_, q] = max(abs(A(p:n, p)));
        q = q + p - 1;
        A([p, q], : ) = A([q, p],:);
        b([p, q]) = b([q, p]);
        for i = p+1:n
            m = A(i,p) / A(p,p);
            A(i,:) = A(i, :) - m * A(p, :);
            b(i) = b(i) - m * b(p);
        end
    end
    x = backword_substitution(A, b);
endfunction

gauss(A, b)

function x = lusolve(A, b)
    [L, U] = lu(A)
    x = backword_substitution(U, b);
    x = x .* forward_substitution(L, b);
endfunction

lusolve(A, b)
        
