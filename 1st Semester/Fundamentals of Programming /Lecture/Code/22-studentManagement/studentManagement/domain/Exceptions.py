'''
Created on Nov 20, 2016

@author: Arthur
'''
class StudentManagerException(Exception):
    pass

class ValidationException(StudentManagerException):
    def __init__(self, msgs):
        self.__msgs = msgs

    def getMsg(self):
        return self.__msgs

    def __str__(self):
        return str(self.__msgs)
