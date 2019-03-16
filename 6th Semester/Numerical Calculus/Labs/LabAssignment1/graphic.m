function graphic(a, b)
t = linspace(0, 10*pi, 1000);
x = (a+b)*cos(t)-b*cos((a/b + 1)*t);
y = (a+b)*sin(t)-b*sin((a/b + 1)*t);
plot(x,y)