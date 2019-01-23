'''
Created on Nov 1, 2016

@author: Arthur
'''

class FirstClass:
    pass

class SecondClass:
    def __init__(self):
        self.testOne = "Test One"
        self._testTwo = "Test Two"
        self.__testThree = "Test Three"

obj = SecondClass()
print(obj.__testThree)
#print(obj._SecondClass__testThree)
