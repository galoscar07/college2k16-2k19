disp("Hello World");
disp("Problem 1");
l1 = @(x) x;
l2 = @(x) 3 / 2 .* x .^ 2 - 1 / 2;
l3 = @(x) 5 / 2 .* x .^ 3 - 3 / 2 .* x;
l4 = @(x) 35 / 8 .* x .^ 4 - 15 /4 .* x .^ 2 + 3 / 8;

x = 0:0.01:1;

% First graphic plot
subplot(2, 2, 1);
plot(x, l1(x))
title("l1(x)")
legend("l1(x)")

% Second graphic plot
subplot(2, 2, 2);
plot(x, l2(x))
title("l2(x)")
legend("l2(x)")

% Third graphic plot
subplot(2, 2, 3);
plot(x, l3(x))
title("l3(x)")
legend("l3(x)")

% Forth graphic plot
subplot(2, 2, 4);
plot(x, l4(x))
title("l4(x)")
legend("l4(x)")

disp("Problem 2");

T = @(n, t) cos(n * acos(t));
t = -1:0.01:1;

hold on

title('Chebyshev polynomials')
plot(t, T(1, t), 'DisplayName', 'T1')
plot(t, T(2, t), 'DisplayName', 'T2')
plot(t, T(3, t), 'DisplayName', 'T3')
legend('T1', 'T2', 'T3')

leg = []

function rec = P(n)
  if (n == 0)
    rec = @(x) 1;
  elseif(n == 1)
    rec = @(x) x;
  else
    rec = @(x) 2 .* x .* P(n - 1)(x) - P(n - 2)(x);
  end
end

for i = 1:6
  plot(t, P(i)(t));
  leg = [leg; sprintf('T%d', i)];
end

legend(leg)


disp("Problem 3");

%function taylor(N)
%    clf;
%    hold on;
%   T = @(x) ones(size(x))
%    for n=1:N
%        T = @(x) T(x) + (x.^n) / factorial(n);
%        fplot(T, [-1, 3]);
%    end
%end    
%fplot(@exp, [-1, 3], '-r');

x=1:0.25:2.5;
f=@(x) sqrt(5*x.^2+1);

function T = findif(x, f)
    n = length(x);
    T = [f(x)', NaN * ones(n, n-1)];
    for i=2:n
        T(1:n-i+1,i) = diff(T(1:n-i+2, i-1));
    end
end

findif(x, f)