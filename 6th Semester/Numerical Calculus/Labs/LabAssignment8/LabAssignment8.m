disp("Problem 1");
disp("a)");

%function B=reptrap(f, a, b, n)
  %  x = linspace(a + (b-a)./(2*n), b - (b-a)./(2*n), n);
 %   B = ((b-a)./n * sum(f(x)));
%end

%f= @(x) exp(-x.^2)
%reptrap(f, 1, 1.5, 90000)
%a=1;b=1.5;
%quad(f, a, b)


function Q = romberg(f, a, b, n)
    Q = NaN(n+1, 1);
    Q(1) = (f(a) + f(b)) * (b-1) ./ 2;
    h = b - a;
    for k = 1:n
        j = 1:2^(k-1);
        Q(k+1) = Q(k) / 2 + (h / 2^k) .* sum(f(a + (2 .* j - 1) * (h / 2^k)));
    end
end

f = @(x) 2./(1+x .^2);
%romberg(f, 0, 1, 3)

function R = myfunction(f, a, b, n)
    R = NaN(n+1)
    R(:,1) = romberg(f, a, b, n)
    for j=2:n+1
        for i=j:n+1
            R(i, j) = (4^(-(j-1)) * R(i-1, j-1) - R(i, j-1)) ./ (4^(-(j-1)) - 1)
        end
    end
end

myfunction(f, 0, 1, 4)
