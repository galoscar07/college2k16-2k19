'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.repository.GradeRepository import GradeRepository
from examples.studentManagement.repository.Exceptions import FileRepositoryException
from examples.studentManagement.domain.Grade import Grade

class GradeCSVFileRepository(GradeRepository):
    def __init__(self, studentRepo, fileName="grades.txt"):
        GradeRepository.__init__(self)
        self.__studentRepo = studentRepo
        self.__fName = fileName
        self.__loadFromFile()
    
    def store(self, grade):
        GradeRepository.store(self, grade)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
        except IOError:
            raise FileRepositoryException()

        line = f.readline().strip()
        while line != "":
            attrs = line.split(";")

            '''
                First find the student with the given ID
            '''            
            student = self.__studentRepo.find(attrs[0])
            
            '''
                Create the Grade object
            '''
            newGrade = Grade(student, attrs[1], int(attrs[2]))
            GradeRepository.store(self, newGrade)
            line = f.readline().strip()
        f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        gradeList = GradeRepository.getAll(self)
        for grade in gradeList:
            gradeStr = grade.getStudent().getId() + ";" + grade.getDiscipline() + ";" + str(grade.getGradeValue()) + "\n"
            f.write(gradeStr)
        f.close()
