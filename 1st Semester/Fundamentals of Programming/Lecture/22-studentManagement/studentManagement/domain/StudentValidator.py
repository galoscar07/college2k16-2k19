'''
Created on Nov 21, 2016

@author: Arthur
'''

from examples.studentManagement.domain.Exceptions import ValidationException

class StudentValidator:
    """
    Validator class for Student
    """
    def __init__(self):
        pass

    def validate(self, student):
        """
        Validate the given student
        
        input: 
            student - the student instance to be validated
        output: 
            None
        raises: 
            ValidationException in case of validation error
        """
        errorMsg = []
        if student.getId() == "":
            errorMsg.append("Id can not be empty")
        if student.getName() == "":
            errorMsg.append("Name can not be empty")
        if student.getAddr() == None or student.getAddr().getStreet() == "":
            errorMsg.append("Address can not be empty")

        if errorMsg != []:
            raise ValidationException(errorMsg)
