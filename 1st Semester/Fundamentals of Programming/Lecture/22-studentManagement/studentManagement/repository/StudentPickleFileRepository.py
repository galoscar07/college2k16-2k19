'''
Created on Nov 22, 2016

@author: Arthur
'''
'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.repository.StudentRepository import StudentRepository
import pickle

class StudentPickleFileRepository(StudentRepository):
    def __init__(self, fileName="students.pickle"):
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
        f = open(self.__fName, "rb")
        
        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self._data, f)
        f.close()
        
        
