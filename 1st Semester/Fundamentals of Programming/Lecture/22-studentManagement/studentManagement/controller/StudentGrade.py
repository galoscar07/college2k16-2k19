'''
Created on Nov 21, 2016

@author: Arthur
'''
class StudentGrade:
    def __init__(self, studentId, studentName, discipline, gradeValue):
        self.__studentId = studentId
        self.__studentName = studentName
        self.__discipline = discipline
        self.__gradeValue = gradeValue

    def getStudentId(self):
        return self.__studentId
    
    def getStudentName(self):
        return self.__studentName

    def getGradeValue(self):
        return self.__gradeValue

    def getDiscipline(self):
        return self.__discipline
    
    def __str__(self):
        return self.__studentId + " " + self.__studentName + " grade= " + str(self.__gradeValue)
