n=input("Give a value: ")
b=int(n)
l=[0,0,0,0,0,0,0,0,0,0]
while b!=0:
    l[b%10]=l[b%10]+1
    b=b//10
for i in range(9,-1,-1):
    for g in range(1,l[i]+1):
        b=b*10+i
print(b)
