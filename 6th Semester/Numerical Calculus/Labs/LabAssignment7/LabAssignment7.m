disp("Hello World");
disp("Problem 1");
disp("1. a) Approximate the integral");
disp("b) Plot the graph of the function f and the graph of the trapezium with vertices (0; 0); (0; f (0)); (1; f (1)) and (1; 0):")

f= @(x) 2./(1+x.^2)

function A=trap(f, a, b)
    A=((f(a)+f(b))/2) * (b-a)
    fplot(f, [a, b])
    hold on
    plot([a, a, b, b], [0, f(a), f(b), 0])
    axis([a - 0.1, b + 0.1, 0 , 3])
end

trap(f, 0, 1)

pause(1);

function B=reptrap(f, a, b, u)
    x = linspace(a, b, u+1); % == a: (b-a)/u : b
    B = ((b-a)/2*u) * (f(a)+f(b)+ 2*sum(f(x(2:u))))
    fplot(f, [a, b])
    hold on
    plot([a, a, b, b], [0, f(a), f(b), 0])
    axis([a - 0.1, b + 0.1, 0 , 3])
end

reptrap(f, 0, 1, 90000)
    
pause(1);


disp("Problem 2");
disp("2. Approximate the following double integral using trapezium formula for double integrals, given in (1). (Result: 0:4295545)");

clf; clear;

f= @(x) 2./(1+x.^2)


function A = repsimps(f, a, b, n)
    x = linspace(a, b, n+1); % == a: (b-a)/u : b
    A = (b-a)/(6*n) * [f(a) + f(b) + 4 * sum(f( (x(1:n)+x(2:n+1))/2 )) + 2 * sum(f(x(2:n)))];
    fplot(f, [a, b])
    hold on
    plot([a, a, b, b], [0, f(a), f(b), 0])
    axis([a - 0.1, b + 0.1, 0 , 3])
end
    
repsimps(f, 0, 1, 45000);

pause(1);

I = dblquad (@(x, y) ln(x+2*y), 1, 1.5, 1.4, 2)
