'''
Created on Oct 16, 2016

@author: Arthur
'''

"""
This is a module docstring

This module provides 2 functions related to the Fibonacci sequence
"""

def fibTerm(n):
    '''
    Return the n-th term of the Fibonacci sequence
    Input: n - the index of the required term (first term, 0 has index 0)
    Output: The n-th term of the sequence
    '''
    a, b, i = 0, 1, 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a
    
def fibSequence(n):  
    '''
    Return the first n terms of the Fibonacci sequence
    Input: n - the number of terms of the sequence
    Output: The sequence of terms
    '''
    result = []
    
    for i in range(0,n+1):
        result.append(fibTerm(i))
    return result

'''
If the module is executed directly, its name is '__main__'
'''
if __name__ == "__main__":
    n = int(input("How many terms?"))
    print(fibSequence(n))
    
    