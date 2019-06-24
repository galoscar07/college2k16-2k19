disp("Hello World");
%A = [400 201; 800 4]
%cond(A)
%B = [200;-200]
%x = A \ B

A = [10 7 8 7; 7 5 6 5; 8 6 10 9; 7 5 9 10]
B = [32 23 33 31]
cond(A)
X = A / B
BB = [31.9 22.9 33.1 31.1]
XX = A / BB
input_error = norm(B - BB) / norm(B)
output_error = norm(X - XX) / norm(X)

output_error / input_error