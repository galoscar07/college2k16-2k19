% ---------------------------------------------
% I Check the following operations with vectors
% ---------------------------------------------

% If you want to find information about a function type help name_of_method
a=10:-1:1; % line vector starting point:step:the final point default step 1
a = [1 2 3]; % line vector
b = [4; 5; 6]; % column vector
c=a.*b; % matrix multiplication
d = b'; % the transpose vector of b
e=a.*d; % pointwise multiplication
f=a.^2; % elems of the vector at the power of 2
[1 2 3]*[1 2 3]';
exp(a);
exp(1); % the number e
sqrt(a);
m=max(a); % get the max from the matrix
A=magic(5);
max(A); % max on every column
max(A, 2);
A(3,:); % take the line 3 from the matrix
A([1, 3, 5, 1], :); % take multiples lines it can also take a line 2 times
A([1, 3, 5, 1], 2:end);
a=magic(4); % generate a "magic matrix" having the sum on line and column
            % equal
b=magic(4);
c=[a,b]; % concatenation of 2 matrices put b on the right of a 
c=[a;b]; % concatenation of 3 matrices, put b under a

A=zeros(3); % initialize a matrice full of zeros
A=zeros(1, 10); % initialize a vector with 10 zeros
A=ones(4);
I=eye(3); % identity matrix
v=randi(5,1,10); % make a vector of 10 elements with values from 1 to 5
[m,i]=max(v); % m = max value in v and i the position
[~,i]=max(v); % will return only the index

triu(A); % extract upper triangular part 
tril(A); % extract lower triangular part
diag(diag(A)); % make all the elems except the one on the main diagonal 0

pi; % constant  
format long; % now see pi decimals
pi;
format short;

linspace(0,pi,10) % 10 values from 0 to pi equal distance between them

% ---------------
% II Polynomials
% ---------------

% evaluate the polynomial p(x) = 2x^3-5x^2+8 in x = 2
polyval([2 -5 0 8], 2);

% find the roots of the polynomial p(x) = x^3 - 5x^2 - 17x + 21
% help roots;
roots([1, -5, -17, 21]);

% -----------
% III Graphs
% -----------

% Problem 1
f=@(x) exp(10*x.*(x-1)).*sin(12*pi*x)
fplot(f, [0, 1], '--r', 'LineWidth', 2)

% Problem 2
graphic(1,2); % uses the function in the file graphic.m

% Problem 3
ezplot(@(x,y) (x.^2 + y.^2 -1).^3 - x.^2.*y.^3, [-1.5 , 1.5]);

% Problem 4
%x = linspace(-2, 2, 100);
%y = linspace(-4, 4, 100);
%[X, Y] = meshgrid(x, y);
%mesh(X, Y, exp(-((X-1/2).^2) + (Y-1/2).^2));

% write a recursive function that computes the value of the following expression:
% 1+1/(1+1/(1+1/(1+1))) here n =3
% 1 + 1/(1+1) here n = 1
%contfrac(10000);