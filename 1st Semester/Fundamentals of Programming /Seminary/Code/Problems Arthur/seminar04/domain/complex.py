'''
Created on Oct 19, 2016

@author: Arthur

This module contains the operations required for our complex number data type

!NB 
    Data Type = domain + operations
    The current module MUST NOT contain any I/O, it must communicate with other modules exclusively using function parameters, returns and exceptions
'''
from math import sqrt

def equal(c1, c2):
    """
    Test if two complex number are equal
    Input: Two complex numbers
    Output: True if numbers are equal, false otherwise
    Exceptions: -
    """
    return c1[0] == c2[0] and c1[1] == c2[1]

def isReal(number):
    """
    Test if given number is real
    Input: A complex number
    Output: True if number is real, False otherwise
    Exceptions: -
    """
    return number[1] == 0

def modulus(number):
    """
    Calculates the modulus of a complex number
    Input: A complex number
    Output: The value of the modulus
    Exceptions: -
    """
    return sqrt(number[0] ** 2 + number[1] ** 2)

def sum(c1, c2):
    """
    Calculates the sum of two complex numbers
    Input: A pair of complex numbers
    Output: Sum of given numbers
    Exceptions: -
    """
    return [c1[0] + c2[0], c1[1] + c2[1]]

def testEqual():
    assert equal([0, 0], [0, 0]) == True
    assert equal([1, -2], [1, -2]) == True
    assert equal([1, 0], [0, 1]) == False
    assert equal([0, -1], [-1, 0]) == False

def testIsReal():
    assert isReal([0, 0]) == True
    assert isReal([1, 0]) == True
    assert isReal([-1, 0]) == True
    assert isReal([0, 1]) == False
    assert isReal([0, -1]) == False
    assert isReal([-1, -1]) == False

def testModulus():
    assert modulus([0, 0]) == 0
    assert modulus([1, 0]) == 1
    assert modulus([0, -1]) == 1
    assert modulus([3, 4]) == 5

def testSum():
    assert sum([0, 0], [0, 0]) == [0, 0]
    assert sum([1, 0], [0, 1]) == [1, 1]
    assert sum([0, 1], [0, -1]) == [0, 0]
    assert sum([-1, 0], [1, 0]) == [0, 0]
    assert sum([1, 2], [3, 4]) == [4, 6]
