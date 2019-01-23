n=input("Give a value: ")
n=int(n)
b=0
while n!=0:
    b=(b*10)+(n%10)
    n=n//10
print(b)
