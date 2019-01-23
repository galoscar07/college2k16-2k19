'''
Created on Nov 21, 2016

@author: Arthur
'''
from examples.studentManagement.domain.Student import Address, Student

class StudentController:
    """
      Class responsible with the use cases related to Student CRUD
      GRASP Controller
    """
    def __init__(self, val, repo):
        """
          Initialise the controller,
          controller need a validator and a repository to perform the operations
          val - StudentValidator (injected)
          repo - StudentRepository (injected
        """
        self.__val = val
        self.__repo = repo

    def create(self, studentId, name, county, city, street):
        """
        Create, validate and store a student

        input:
            studentId, name, street, city - strings
            nr - int
        output:
            Returns the newly created Student object
        raises:
            ValueEror if the data is invalid, on duplicated studentId
        """
        st = Student(studentId, name, Address(county, city, street))

        """
            Validate and store the student
        """
        self.__val.validate(st)
        self.__repo.store(st)
        return st

    def getNrStudents(self):
        """
          Return the number of students
          return int
        """
        return self.__repo.size()

    def remove(self, studentId):
        """
         Remove student with the given studentId
         studentId - string, student studentId
         return Student, the removed Student
         raise ValueError if there is no student with the given studentId
        """
        return self.__repo.remove(studentId)
    
    def search(self, criteria):
        """
          Search students with name containing criteria
          criteria string
          return list of students, where the name contains criteria
        """
        studentList = self.__repo.getAll()
        if criteria == "":
            return studentList

        rez = []
        for st in studentList:
            if criteria in st.getName():
                rez.append(st)
        return rez

    def update(self, studentId, name, county, city, street):
        """
          Update student with the given studentId
          studentId,name, adr strings
          return the old student
          raise ValueError if the student is invalid, if there is no student with the given studentId
        """
        newSt = Student(studentId, name, Address(county, city, street))

        # validate the student
        self.__val.validate(newSt)

        # get the old student
        oldSt = self.__repo.find(studentId)

        # update the student
        self.__repo.update(studentId, newSt)
        return oldSt
