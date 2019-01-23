from math import sqrt
def isPrime(n):
    '''
    Return true if the number is prime or false otherwise
    Arguments: n-is the number that we need to decide if is prime
    Return: True if n is prime, or false otherwise
    '''
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def nextPrime(n):
    '''
    The fuction nextPrime will return the the following prime number after n
    Arguments: n- is the number, and we need to find the next prime number after n
    Return: a prime number which is bigger than n
    '''
    while True:
        n+=1
        if isPrime(n):
            return n
n=input("Give a value: ")
n=int(n)
print("The first prime number after ",n,"is ",nextPrime(n))
