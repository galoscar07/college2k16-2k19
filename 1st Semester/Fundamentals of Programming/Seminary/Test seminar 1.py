# -------------------1-------------

def f1 (l,n):
    l = l + [n]
def g1(l):
    l *= 2
def h1(l,n):
    l.extend([n])
def m1():
    l = [1,2]
    n = 3
    f1(l,n)
    print(l)
    g1(l)
    print(l)
    h1(l,4)
    print(l)
m1()
print("mue")
#-----------------------2---------------------
def f2(l):
    l.clear()
    l.append(10)
def g2(l):
    l = []
    l.append(10)
def h2(k):
    k += 1
def m2():
    lf = [1,2,3]
    lg = [1,2,3]
    n = 0
    f2(lf)
    g2(lg)
    h2(n)
    print(lf,lg,n)
m2()
print("mue")
#-----------------------3---------------------
l = [1,2]
l2 = [3]
def f3(n):
    l2 = l[:]
    l.append(n)
f3(5)
print(l,l2)
print()
