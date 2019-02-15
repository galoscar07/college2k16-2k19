'''
Created on Nov 21, 2016

@author: Arthur
'''
class Grade:
    """
    Class represents the grade of one student at a given discipline
    """
    def __init__(self, studentId, discipline, gradeValue):
        self.__studentId = studentId
        self.__discipline = discipline
        self.__gradeValue = gradeValue

    def getStudent(self):
        return self.__studentId

    def getDiscipline(self):
        return self.__discipline

    def getGradeValue(self):
        return self.__gradeValue

    def __str__(self):
        return self.__studentId.getName() + ", discipline= " + str(self.__discipline) + ", grade= " + str(self.__gradeValue)

    def __eq__(self, ot):
        if ot == None: return False
        return self.__studentId == ot.__studentId and self.__discipline == ot.__discipline