'''

@author: radu

Problem 1
a) Compute the sum of the first n natural numbers.
b) Check if a given integer number n is prime.
c) Compute the greatest common divisor between two integers a and b.
d) Compute the first prime number greater than a given integer n.
e) Print the first k prime numbers greater than a given integer n.  

'''

# a) Compute the sum of the first n natural numbers.

def sum_n(n):
    """Return the sum of the first n natural numbers.
    
    Given a natural number n,compute the sum of the first n natural numbers.
    
    Arguments:
        n - natural number.
    Returns:
        The sum of the first n natural numbers.
    """
    s = 0
    for i in range(n):
        s += i
    return s

# =============================================================================

# b) Check if a given integer number n is prime.

from math import sqrt

def is_prime(n):
    """Check if n is prime.
    
    Check if a given integer number n is prime.
    
    Arguments:
        n - integer.
    Returns:
        True if n is prime or False otherwise.
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# =============================================================================

# c) Compute the greatest common divisor between two integers a and b.

def gcd(a, b):
    """Return the greatest common divisor between a and b.
    
    Compute the greatest common divisor between two integers a and b.
    
    Arguments:
        a, b - integers; a, b can not be both equal to 0.
    Returns:
        The greatest common divisor between a and b.        
    """
    while b != 0:
        a, b = b, a % b
    return a if a > 0 else -a

# =============================================================================

# d) Compute the first prime number greater than a given integer n.

def first_prime(n):
    """Return the first prime greater than n.
    
    Compute the first prime number greater than a given integer n.
    
    Arguments:
        n - integer.
    Returns:
        The first prime number greater than n.
    """
    while True:
        n = n + 1
        if is_prime(n):
            return n
        
# =============================================================================

# e) Print the first k prime numbers greater than a given integer n.

def first_k_primes(n, k):
    """Print the first k primes greater than n.
    
    Print the first k prime numbers greater than a given integer n.
    
    Arguments:
        n - integer
        k - natural, k>0.
    Returns: 
        None.        
    """
    for _ in range(k):
        n = first_prime(n)
        print(n)
        

if __name__ == '__main__':
    # Problem 1a)
#     try:
#         n = int(input("n="))
#         print("the sum of first n natural numbers is ", sum_n(n))
#     except ValueError:
#         print("invalid input")

    # Problem 1b)
#     try:
#         n = int(input("n="))
#         print("is_prime(n): ", is_prime(n))
#     except ValueError:
#         print("invalid input")

    # Problem 1c)
#     try:
#         a = int(input("a="))
#         b = int(input("b="))
#         print("gcd(a, b) = ", gcd(a, b))
#     except ValueError:
#         print("invalid input")

    # Problem 1d)
#     try:
#         n = int(input("n="))
#         print("first_prime(n) = ", first_prime(n))
#     except ValueError:
#         print("invalid input")
#     

    # Problem 1e)
    try:
        n = int(input("n="))
        k = int(input("k="))
        print("first_k_primes(n): ")
        first_k_primes(n, k)
    except ValueError:
        print("invalid input")
    pass
