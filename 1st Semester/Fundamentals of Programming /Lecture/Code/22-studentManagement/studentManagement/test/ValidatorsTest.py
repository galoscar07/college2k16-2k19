'''
Created on Nov 21, 2016

@author: Arthur
'''
import unittest
from examples.studentManagement.domain.StudentValidator import StudentValidator
from examples.studentManagement.domain.Student import Address, Student
from examples.studentManagement.domain.Grade import Grade
from examples.studentManagement.domain.GradeValidator import GradeValidator
from examples.studentManagement.domain.Exceptions import ValidationException

class ValidatorTest(unittest.TestCase):
    def testValidateStudent(self):
        val = StudentValidator()

        """
            Student ID must exist
        """
        st = Student("", "Ion", Address("Adr", 1, "Cluj"))
        try:
            val.validate(st)
            self.assertTrue(False)
        except ValidationException:
            pass
    
        """
            Student name must exist
        """
        st = Student("3", "", Address("Adr", 1, "Cluj"))
        try:
            val.validate(st)
            self.assertTrue(False)
        except ValidationException:
            pass
    
        """
            Address must exist
        """
        st = Student("3", "Ion", Address("", "Cluj", ""))
        try:
            val.validate(st)
            self.assertTrue(False)
        except ValidationException:
            pass
            
    def testValidateGrade(self):
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        
        """
            Grade must be between 1 and 10
        """
        gr = Grade(st, "FP", 11)
        val = GradeValidator()
        try:
            val.validate(gr)
            self.assertTrue(False)
        except ValidationException:
            pass
