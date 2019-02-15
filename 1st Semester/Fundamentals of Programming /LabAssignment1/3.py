n=input("Give a value: ")
b=int(n)
l=[0,0,0,0,0,0,0,0,0,0]
while b!=0:
    l[b%10]=l[b%10]+1
    b=b//10
if l[0]!=0:
    i=1
    while l[i]==0:
        i+=1
    b=b*10+i
    l[i]=l[i]-1
    for j in range(1,l[0]+1):
        b=b*10
    for j in range(i,10):
        for g in range(1,l[j]+1):
            b=b*10+j
else:
    for i in range(1,10):
        for j in range(1,l[i]+1):
            b=b*10+i
print(b)
