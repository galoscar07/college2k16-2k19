'''
Created on Nov 21, 2016

@author: Arthur
'''
from examples.studentManagement.controller.Exceptions import StudentNotFoundException
from examples.studentManagement.domain.Grade import Grade

class GradeController:
    """
    Controller class for student grades 
    """
    def __init__(self, gradeRepo, gradeValidator, studentRepo):
        """
          Initialise
          gradeRepo - GradeRepository
          gradeValidator - GradeValidator
          studentRepo - StudentRepository
        """
        self.__gradeRepo = gradeRepo
        self.__gradeValidator = gradeValidator
        self.__studentRepo = studentRepo

    def assign(self, studentId, discipline, gradeValue):
        """
        Assign a grade for a student at a given discipline

        input:
            studentId - id of the student receiving the grade
            discipline - the discipline they are graded in
            gradeValue - numerical value of the grade. Must be an integer between 1 and 10
        output:
            The created Grade object
        raises:
            ValidateException for invalid gradeValue
            StudentNotFound if there is no student for the given id
        """
        student = self.__studentRepo.find(studentId)
        if student == None:
            raise StudentNotFoundException("Student with id = " + str(studentId) + " not found.")

        """
            Create new Grade object
            Validate it
            Store it
            Return it
        """
        newGrade = Grade(student, discipline, gradeValue)
        self.__gradeValidator.validate(newGrade)
        self.__gradeRepo.store(newGrade)

        return newGrade

    def listGrades(self, studentId):
        """
        Get all the grades of a student

        input:
            The id of the student for whom the grades are listed
        output:
            The list of grades for the given student
        raises:
            StudentNotFoundException, if there is no student for the given id
        """
        student = self.__studentRepo.find(studentId)
        if student == None:
            raise StudentNotFoundException()

        return self.__gradeRepo.getAll(student)

    def getTop5(self, discipline):
        """
        Get the best 5 students at a given discipline

        NB!
            Here we use Data Transfer Objects (DTO)
        
        input:
            The discipline for which the best grades are returned
        output:
            The list of the highest grades
        """

        """
            Get all grades for the given discipline
        """
        studentGradeList = self.__gradeRepo.getAllForDisc(discipline)

        """
            Sort it decreasing by grade value, retain top 5 
        """
        sortedStudentGradeList = sorted(studentGradeList, key=lambda studentGrade: studentGrade.getGradeValue(), reverse=True)[:5]
        return sortedStudentGradeList
