from math import sqrt
def isPrime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=input("da valoare")
b=int(n)
a=2
l=[0,0]
while a<=b:
    if isPrime(a):
        if isPrime(b-a):
            l[0]=a
            l[1]=b-a
    a+=1
if l[0]==0 and l[1]==0:
    print("no se puede")
else:
    print(l[0]," ",l[1])

    
