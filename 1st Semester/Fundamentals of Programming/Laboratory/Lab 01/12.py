def digitsNumber(n):
    '''
    The fuction will return the digits of n into a list
    '''
    l=[0,0,0,0,0,0,0,0,0,0]
    if n==0:
        l[0]=1
    else:
        while n!=0:
            l[n%10]=1
            n=n//10
    return l
def ifEquals(l1,l2):
    for i in range(0,10):
        if l1[i]!=l2[i]:
            return False
    return True
n1=input("First Value: ")
n2=input("Secound Value: ")
n1=int(n1)
n2=int(n2)
l1=digitsNumber(n1)
l2=digitsNumber(n2)
if ifEquals(l1,l2):
    print("the numbers have the P property")
else:
    print("the numbers doesn't have the P property")
