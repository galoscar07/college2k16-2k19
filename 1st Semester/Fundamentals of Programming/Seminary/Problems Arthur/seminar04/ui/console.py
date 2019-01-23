'''
Created on Oct 19, 2016

@author: Arthur

This is the UI module of the application. Notice that it is the only module where I/O operations take place.

!NB
    You are not required to provide specification / tests for UI modules!
'''
from copy import deepcopy
from seminar04.functions.functions import listToStr, addNumber, removeNumberAtPos, removeNumber, filterByModulus, filterByReal

def _printMenu():
    menuString = '\nAvailable commands:\n'
    menuString += '\t 1 - Add number\n'
    menuString += '\t 2 - Remove number at position\n'
    menuString += '\t 3 - Remove all number appearances\n'
    menuString += '\t 4 - Display numbers with modulus>value\n'
    menuString += '\t 5 - Display real numbers\n'
    menuString += '\t 6 - Undo\n'
    menuString += '\t 0 - Exit\n'
    print(menuString)

def start():
    _mainMenu()

def _mainMenu():
    numbersList = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
    undoList = deepcopy(numbersList)
    
    stop = False
    while stop == False:
        try:
            print("The list is: ", listToStr(numbersList))
            _printMenu()
            command = input("Enter command: ")
            if command == '1':
                _addSubmenu(numbersList, undoList)
            elif command == '2':
                _removeAtPositionSubmenu(numbersList, undoList)
            elif command == '3':
                _removeAllSubmenu(numbersList, undoList)
            elif command == '4':
                _filterByModulusSubmenu(numbersList, undoList)
            elif command == '5':
                _filterByRealSubmenu(numbersList, undoList)
            elif command == '6':
                numbersList.clear()
                numbersList.extend(deepcopy(undoList))
            elif command == '0':
                stop = True
            else:
                print("Invalid command!") 
        except ValueError as ve:
            print(ve)

def _addSubmenu(numberList, undoList):
    number = _readComplexNumber()
    _recordForUndo(numberList, undoList)
    addNumber(numberList, number)

def _removeAtPositionSubmenu(numberList, undoList):
    pos = _readPositiveInteger("Please give position:")
    _recordForUndo(numberList, undoList)
    removeNumberAtPos(numberList, pos)

def _removeAllSubmenu(numberList, undoList):
    _recordForUndo(numberList, undoList)
    number = _readComplexNumber()
    removeNumber(numberList, number)

def _displayAllSubmenu(numberList, undoList):
    print(listToStr(numberList))

def _filterByModulusSubmenu(numberList, undoList):
    modulo = _readPositiveInteger("Please give modulus:")
    print(listToStr(filterByModulus(numberList, modulo)))

def _filterByRealSubmenu(numberList, undoList):
    print("The real numbers are: ", listToStr(filterByReal(numberList)))

def _recordForUndo(numberList, undoList):
    undoList.clear()
    undoList.extend(deepcopy(numberList))

def _readPositiveInteger(message):
    """
    Reads a positive integer
    Input: -
    Output: A positive integer 
    """
    result = None
    while result == None: 
        try:
            result = int(input(message))
            if result < 0:
                raise ValueError
        except ValueError:
            print("Please input a positive integer!")
    return result

def _readComplexNumber():
    """
    Reads a complex number
    Input:  -
    Output: The complex number
    Exceptions: - 
    """
    while True:
        try:
            real = int(input("Real part="))
            imag = int(input("Imag part="))
            return [real, imag]
        except ValueError:
            print("Real/Imag parts must be numbers!")
    return []
