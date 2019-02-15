'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.domain.Exceptions import StudentManagerException

class RepositoryException(StudentManagerException):
    """
    Base class for the exceptions in the repository
    """
    def __init__(self, msg):
        self.__msg = msg

    def getMsg(self):
        return self.__msg

    def __str__(self):
        return self.__msg

class DuplicateIDException(RepositoryException):
    """
    Class for duplicated ID's detected in repository
    """
    def __init__(self, msg):
        RepositoryException.__init__(self, "Duplicate ID" + msg)
        
class GradeAlreadyAssignedException(RepositoryException):
    """
    Class for duplicate grades for a given student/discipline
    """
    def __init__(self, msg):
        RepositoryException.__init__(self, "Grade already assigned: " + str(msg))
        
class FileRepositoryException(RepositoryException):
    """
    File-related repository errors
    """
    def __init__(self, msg):
        RepositoryException.__init__(self, "Error while accessing repository file " + msg)
