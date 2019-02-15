'''
Created on Nov 21, 2016

@author: Arthur
'''
class Student:
    """
    Class represents a student
    """
    def __init__(self, studentId, name, address):
        self.__studentId = studentId
        self.__name = name
        self.__address = address

    def getId(self):
        return self.__studentId

    def getName(self):
        return self.__name

    def getAddr(self):
        return self.__address

    def __str__(self):
        return self.__studentId + " " + self.__name + " " + str(self.__address)

    def __eq__(self, ot):
        if ot == None or type(ot) != Student:
            return False
        return self.__studentId == ot.__studentId
    
class Address:
    """
    Represents an address
    """
    def __init__(self, county, city, street):
        self.__county = county
        self.__city = city
        self.__street = street

    def getStreet(self):
        return self.__street

    def getCounty(self):
        return self.__county

    def getCity(self):
        return self.__city

    def __str__(self):
        return "Country " + self.__county + " City " + self.__city + " Street " + self.__street
