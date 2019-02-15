#1
def m1():
    a = 1
    n = a
    b = [a] + [0]
    c = [1] + [b]
    c.append(a)
    a = 0
    b[1] = 2
    c[1][0] = 3
    print(a,b,c,n)
m1()
#--------------------------------

#2.
def m2():
    a = lambda x: x+1
    b = lambda x: x+[1]
    c = b([2])
    d = [a,b,c]
    print(a(2),b([2]),c)
    a = [3,5]
    b = [5,6]
    c = [7,8]
    print(d[0](2))
    print(d[2][0])
m2()

#--------------------------------
#3.
def g3(n):
    return n+1
def f3(x,y):
    return x(y)+1
print(f3(g3,1))
b = [f3,g3]
a = lambda x:x+2
print(a(1))
print(g3(a(1)))
g3 = a
print(g3(1))
print(b[1](1))

