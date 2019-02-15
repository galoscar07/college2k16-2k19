from math import sqrt
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=input("Give a value: ")
n=int(n)
stop=0
b=int(n-1)
while stop!=1 and not(isPrime(b)):
    if b<2:
        stop=1
    else:
        b=b-1
if stop==1:
    print("their is not such a value")
else:
    print(b)
