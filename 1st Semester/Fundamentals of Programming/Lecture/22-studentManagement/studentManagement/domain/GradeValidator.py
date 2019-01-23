'''
Created on Nov 21, 2016

@author: Arthur
'''
from examples.studentManagement.domain.Exceptions import ValidationException
from examples.studentManagement.domain.Grade import Grade

class GradeValidator:
    """
        Validator class for grades
    """
    def validate(self, grade):
        """
        Validate the given grade
        
        input: 
            grade - the grade to be validated
        output: 
            None
        raises:
            ValidationException in case of validation error
        """
        if type(grade) is not Grade:
            raise ValidationException("Can only calidate Grade instances!")
        if grade.getGradeValue() not in range(1, 11):
            raise ValidationException("Grade needs to be an integer between 1 and 10")
