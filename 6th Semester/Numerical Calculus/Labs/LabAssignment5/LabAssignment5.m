disp("Laboratory Assignment 5");
disp("Problem 1");
disp("In the following table there are some data regarding a moving car. Use Hermite interpolation to estimate position and speed of the car when the time is t = 10. Also in the lab paper there is a table with values.")

function T=dividif(x, f, df)
    n=length(x);
    z = zeros(1, 2*n);
    z(1:2:end)=x;
    z(2:2:end)=x;
    T = NaN(2*n);
    T(1:2:end, 1) = f;
    T(2:2:end, 1) = f;
    T(1:2:end, 2) = df;
    T(2:2:end-2, 2) = diff(f)./diff(x);
    for i=3:2*n
        T(1:2*n-i+1, i)=diff(T(1:2*n-i+2, i-1))./((z(i:2*n)-z(1:2*n-i+1))');
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Vezi ca la examen deobicei vine un subiect din polinomul de interpolare a lui Lagrange/Hermite
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function N=newtonoriginal(x, f, df, X)
    c = dividif(x, f, df)(1, :);
    n = length(x);
    z = zeros(1, 2*n);
    z(1:2:end) = x;
    z(2:2:end) = x;
    N = zeros(size(X));
    for k=1:length(X)
        prods = 1;
        for i = 1:2*n
            N(k)=N(k)+prods*c(i);
            prods=prods*(X(k)-z(i));
        end
    end
end

function [N, dN]=newton(x, f, df, X)
    c = dividif(x, f, df)(1, :);
    n = length(x);
    z = zeros(1, 2*n);
    z(1:2:end) = x;
    z(2:2:end) = x;
    N = zeros(size(X));
    for k=1:length(X)
        dN(k) = c(2);
        prods = 1;
        for i = 3:2*n
            for j=1:i-1
                dN(k) = dN(k) + c(i) * prod(X(k)-z([1:j-1,j+1:i-1]));
            end
            N(k)=N(k)+prods*c(i);
            prods=prods*(X(k)-z(i));
        end
    end
end

% time
x = [0 3 5 8 13]
% distance
f = [0 225 383 623 993]
% speed
df = [75 77 80 74 72]
% the point in which we calculate
X = linspace(0, 13, 1000);

[N, dN] = newton(x, f, df, X);

plot(N, dN)
