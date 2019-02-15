'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.repository.GradeRepository import GradeRepository
from examples.studentManagement.repository.Exceptions import FileRepositoryException
from examples.studentManagement.domain.Grade import Grade
import pickle

class GradePickleFileRepository(GradeRepository):
    def __init__(self, studentRepo, fileName="grades.pickle"):
        GradeRepository.__init__(self)
        self.__studentRepo = studentRepo
        self.__fName = fileName
        self.__loadFromFile()
    
    def store(self, grade):
        GradeRepository.store(self, grade)
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
            self._data = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self._data, f)
        f.close()
