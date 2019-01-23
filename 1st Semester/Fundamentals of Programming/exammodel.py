"""
subject 1 answer b

def f(l):
    print("A")
    if l == []:
        raise ValueError()
    print("B")
def start():
    l = []
    try:
        print("A")
        f(l)
        print("D")
    except ValueError:
        print("C")
start()
"""

"""
subject 2   answer [1, 2, 6] -1


class A:
    def f(self, l,nr):
        l.append(nr)
class B:
    def g(self, l, nr):
        nr=nr-1
        l = l+[-2]
a = A()
b = B()
l = [1,2]
c = -1
a.f(l,6)
b.g(l,c)
print(l,c)
"""

"""
subject 3 answer 1 3 7 2
"""
a = lambda x: [x+1]
b = a(1)
c = lambda x: x + b
d = c([1])
a=1
b=3
print (a, b, c(4), d[1])
l =[]
if type(l) is not list:
    raise ValueError
