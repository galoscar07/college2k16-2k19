'''
Created on Oct 19, 2016

@author: Arthur

This is the functions module of the application. It contains those functions that actually implement the required features.

!NB
    The current module MUST NOT contain any I/O, it must communicate with other modules exclusively using function parameters, returns and exceptions
'''
from seminar04.domain.complex import isReal, modulus

def addNumber(numberList, number):
    """
    Add complex number to list
    Input: numberList - The list to add to 
           number - The number to add
    Output: -
    Exceptions: -
    """
    numberList.append(number)
    
def removeNumberAtPos(numberList, pos):
    """
    Remove complex number from list given its position
    Input: numberList - The list 
         pos - The position from which number is removed
    Output: -
    Exceptions: ValueError if position invalid!
    """
    if pos < 0 or pos >= len(numberList):
        raise ValueError("Invalid position!")
    numberList.pop(pos)

def removeNumber(numberList, number):
    """
    Remove all appearances of the complex number from list
    Input: numberList - The list 
           number - The number to remove
    Output: The filtered list
    Exceptions: -
    """
    while number in numberList :
        numberList.remove(number)

def filterByReal(numberList):
    """
    Filter all real numbers
    Input: A list of complex numbers to filter
    Output: The list of real numbers from input list
    Exceptions: -
    """
    res = []
    for number in numberList:
        if isReal(number):
            res.append(number)
    return res

def filterByModulus(numberList, value):
    """
    Filter all numbers with modulus>value
    Input: numberList - a list of complex numbers
           value - modulus value to filter
    Output: The list of filtered numbers
    Exceptions: -
    """
    res = []
    for number in numberList:
        if modulus(number) >= value:
            res.append(number)
    return res

def complexToStr(number):
    """
    Convert complex number to string
    Input: The complex number
    Output Its string representation
    Exceptions: -
    """
    result = ""
    if number[0] == 0 and number[1] == 0: 
        return "0"
    if number[0] != 0:
        result += str(number[0])
    if number[0] != 0 and number[1] > 0:
        result += "+"
    if number[1] != 0:
        if number[1] == 1:
            result += "i"
        elif number[1] == -1:
            result += "-i"
        else:
            result += str(number[1]) + "i"
    return result

def listToStr(numberList):
    """
    Convert list of numbers to string
    Input: A list of complex numbers
    Output: The string representation
    Exceptions: -
    """
    if len(numberList) == 0:
        return "list is empty"
    string = ""
    for c in numberList:
        string += complexToStr(c)
        string += " "
    return string 

def testComplexToStr():
    assert complexToStr([0, 0]) == "0"
    assert complexToStr([1, 0]) == "1"
    assert complexToStr([-1, 0]) == "-1"
    assert complexToStr([1, 1]) == "1+i"
    assert complexToStr([1, -1]) == "1-i"
    assert complexToStr([2, 2]) == "2+2i"
    assert complexToStr([-1, -3]) == "-1-3i"
    assert complexToStr([-10, -99]) == "-10-99i"

def testAddNumber():
    l = []
    addNumber(l, [1, 2])
    assert len(l) == 1 and l[0][0] == 1 and l[0][1] == 2
    addNumber(l, [3, 4])
    assert len(l) == 2 and l[1][0] == 3 and l[1][1] == 4
    
def testRemoveNumber():
    l = [[0, 0], [1, 2], [1, 2], [1, 2], [3, 4], [5, 6]]
    removeNumberAtPos(l, 0)
    removeNumberAtPos(l, 4)
    assert len(l) == 4
    assert l[0][0] == 1 and l[0][1] == 2
    assert l[3][0] == 3 and l[3][1] == 4
    removeNumber(l, [1, 2])
    assert len(l) == 1
    removeNumber(l, [3, 4])
    assert len(l) == 0

def testFilterByReal():
    l = [[0, 0], [1, 2], [-1, 2], [1, -1], [0, 4], [-5, 0]]
    res = filterByReal(l)
    assert len(res) == 2 and res[0][1] == 0 and res[1][1] == 0

def testFilterByModulus():
    l = [[0, 0], [1, 2], [-1, 2], [1, -1], [0, 4], [-5, 0]]
    res = filterByModulus(l, 4)
    assert len(res) == 2
