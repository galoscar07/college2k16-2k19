disp("Hello World");
x = [0, pi/2, pi, 3*pi/2, 2*pi];
y = [0, 1, 0, -1, 0];
spline(x, [1 , y, 1])
spline(x, [1 , y, 1], pi/4)

hold on

fplot(@(z) spline(x, [1 , y, 1], z), [0, 2*pi])
plot(x, y, '*r')

fplot(@(z) sin(z), [0, 2*pi] , '-g')