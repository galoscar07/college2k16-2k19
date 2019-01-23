'''
Created on Nov 22, 2016

@author: Arthur
'''
class Person:
    def __init__(self, personId, familyName, givenName):
        self.__personId = personId
        self.__familyName = familyName
        self.__givenName = givenName
    
    def getId(self):
        return self.__personId
    
    def getFamilyName(self):
        return self.__familyName
    
    def getGivenName(self):
        return self.__givenName
    
    def __str__(self):
        return str(self.__personId) + " - " + self.__familyName + " " + self.__givenName
    
def writeToFile(fileName, persons):
    f = open(fileName, "w")
    try:
        for p in persons:
            pString = str(p.getId()) + ";" + p.getFamilyName() + ";" + p.getGivenName() + "\n"
            f.write(pString)
        f.close()
    except Exception as e:
        print("An error occured -" + str(e))

def readFile(fileName):
    result = []
    try:
        f = open(fileName, "r")
        line = f.readline().strip()
        while  len(line) > 0:
            line = line.split(";")
            result.append(Person(int(line[0]), line[1], line[2]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        """
            Here we 'log' the error, and throw it to the outer layers 
        """
        print("An error occured - " + str(e))
        raise e

    return result

"""
    Initialize a list of objects
"""
persons = [Person(1, "Pop", "Anca"), Person(2, "Morariu", "Sergiu"), Person(3, "Moldovean", "Iuliu")]

"""
    Write it to a text file
"""
writeToFile("persons.txt", persons)

"""
    Read it back and see what we have
"""
for p in readFile("persons.txt"):
    print(p)


