'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.repository.StudentRepository import StudentRepository
from examples.studentManagement.repository.Exceptions import FileRepositoryException
from examples.studentManagement.domain.Student import Student, Address

class StudentCSVFileRepository(StudentRepository):
    def __init__(self, fileName="students.txt"):
        StudentRepository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def store(self, student):
        StudentRepository.store(self, student)
        self.__storeToFile()
    
    def remove(self, studentId):
        StudentRepository.remove(self, studentId)
        self.__storeToFile()        
    
    def removeAll(self):
        StudentRepository.removeAll(self)
        self.__storeToFile()
    
    def update(self, studentId, student):
        StudentRepository.update(self, studentId, student)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(";")
                student = Student(attrs[0], attrs[1], Address(attrs[2], attrs[3], attrs[4]))
                StudentRepository.store(self, student)
                line = f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        sts = StudentRepository.getAll(self)
        for st in sts:
            strf = st.getId() + ";" + st.getName() + ";"
            strf = strf + st.getAddr().getStreet() + ";" + str(st.getAddr().getNr()) + ";" + st.getAddr().getCity()
            strf = strf + "\n"
            f.write(strf)
        f.close()
