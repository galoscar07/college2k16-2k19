'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.repository.Exceptions import GradeAlreadyAssignedException
from examples.studentManagement.controller.StudentGrade import StudentGrade

class GradeRepository:
    """
      Repository of grades
      grades are stored in memory
    """
    def __init__(self):
        self._data = []

    def store(self, grade):
        """
          Store a grade
          post: grade is in the repository
          raise GradeAlreadyAssignedException exception if we already have a grade for the student at the given discipline
        """
        if self.find(grade.getStudent(), grade.getDiscipline()) != None:
            raise GradeAlreadyAssignedException("student =" + str(grade.getStudent().getName()) + ", discipline = " + str(grade.getDiscipline()))

        self._data.append(grade)

    def size(self):
        """
          Return the number of elements in the repository
        """
        return len(self._data)

    def __len__(self):
        return self.size()

    def __str__(self):
        result = "Grade Repository:\n"
        for grade in self._data:
            result += "\t" + str(grade) + "\n"
        return result

    def find(self, student, discipline):
        """
          Lookup a grade for a given student and discipline
          student - student
          discipline - discipline
          return Grade or None if there is no grade in the repository
        """
        for gr in self._data:
            if gr.getStudent() == student and gr.getDiscipline() == discipline:
                return gr
        return None

    def getAll(self, student=None):
        """
         Return the grades for a given student. If no student is given, returns all grades

         input:
             An optional parameter representing the student for whom the grades are returned
         output:
             The list of Grade objects
        """
        if student == None:
            return self._data[:]

        result = []
        for grade in self._data:
            if grade.getStudent() == student:
                result.append(grade)
        return result
    
    def getAllForDisc(self, discipline):
        """
        Return all the grades for a given discipline
        
        NB!
            Here we use Data Transfer Objects (DTO)

        input:
            The discipline
        output:
            A list of StudentGrade data transfer objects
        """
        result = []
        for grade in self._data:
            if grade.getDiscipline() == discipline:
                studentGrade = StudentGrade(grade.getStudent().getId(), grade.getStudent().getName(), grade.getDiscipline(), grade.getGradeValue())
                result.append(studentGrade)
        return result