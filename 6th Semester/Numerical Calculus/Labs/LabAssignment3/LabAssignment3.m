disp("Lab Assignment 3");

x = 0:0.5:4;
f = x.^8;

function T = divif(x, f)
    n = length(x);
    T = [f', NaN * ones(n, n-1)]
    for i = 2 : n
        T(1:n-i+1, i) = diff(T(1:n-i+2, i-1))./(x(i:n)-x(1:n-i+1))';
    end
end
divif(x, f);

disp("Problem 1");
disp("The table below contains the population of the USA from 1930 to 1980 (in thousands of inhabitants) [The data is given in the lab paper] Approximate the population in 1955 and 1995.");

x = 1930:10:1980;
y = [123203 131669 150697 179323 203212 226505];
X = 1955;

function L = lagrange(x, y, X)
    m = length(x);
    for i = 1:m
        A(i) = 1 / prod(x(i)-[x(1:i-1), x(i+1:m)]);
    end
    for k = 1:length(X)
        S1 = sum((A .* y) ./ (X(k) - x));
        S2 = sum(A ./ (X(k)-x));
        L(k) = S1 / S2;
    end
end
hold on

lagrange(x, y, X)
plot(x, y, 'or')
L=@(X)lagrange(x,y,X)
fplot(L,[1930, 1995])

disp("Problem 2");
disp("Approximate sqrl(115) with Lagrange interpolation, using the known values for three given nodes.");

x = [121 144 169];
y = [11 12 13];
X = 115;

function L = lagrange(x, y, X)
    m = length(x);
    for i = 1:m
        A(i) = 1 / prod(x(i)-[x(1:i-1), x(i+1:m)]);
    end
    for k = 1:length(X)
        S1 = sum((A .* y) ./ (X(k) - x));
        S2 = sum(A ./ (X(k)-x));
        L(k) = S1 / S2;
    end
end

lagrange(x, y, X)

disp("Problem 3");

clear;

function Runge(n, f)
    fplot(f, [-5, 5], '-b')
    x = linspace(-5, 5, n);
    L = @(X)lagrange(x, f(x), X);
    fplot(L, [-5, 5], '-r');
end

f = @(x) 1./(1+x.^2)
hold on
Runge(8, f)

function Runge(n, f)
    fplot(f, [-5, 5], '-b')
    x = 5 * cos((2*[1:n]-1)/(2*n)+pi);
    L = @(X)lagrange(x, f(x), X);
    fplot(L, [-5, 5], '-r');
end

f = @(x) 1./(1+x.^2)
hold on
Runge(8, f)