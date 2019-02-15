n=input("Give a value: ")
n=int(n)
p=1
for i in range(2,(n//2)+1):
    if n%i==0:
        p=p*i
p=p*n
print(p)
