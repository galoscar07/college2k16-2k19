'''
Created on Nov 21, 2016

@author: Arthur
'''
import unittest
from examples.studentManagement.domain.Student import Address, Student
from examples.studentManagement.domain.Grade import Grade

class DomainTest(unittest.TestCase):
    def testStudentIdentity(self):
        """
            Student objects are defined by their identity and their lifecycle within the application
        """
        st1 = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        st2 = Student("1", "Ion", Address("Adr2", 1, "Cluj"))
        self.assertEqual(st1, st2)

        st1 = Student("1", "Popescu", Address("Adr", 1, "Cluj"))
        st2 = Student("2", "Popescu", Address("Adr2", 1, "Cluj"))
        self.assertNotEqual(st1, st2)

    def testCreateStudent(self):
        st = Student("1", "Ion", Address("Cluj", "Cluj", "Adr2"))
        self.assertEqual(st.getId(), "1")
        self.assertEqual(st.getName(), "Ion")
        self.assertEqual(st.getAddr().getStreet(), "Adr2")
        
        st = Student("2", "Ion2", Address("Cluj", "Cluj", "Adr2"))
        self.assertEqual(st.getId(), "2")
        self.assertEqual(st.getName(), "Ion2")
        self.assertEqual(st.getAddr().getStreet(), "Adr2")
        self.assertEqual(st.getAddr().getCity(), "Cluj")

    def testCreateGrade(self):
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        gr = Grade(st, "FP", 9.5)
        
        self.assertEqual(gr.getStudent(), st)
        self.assertEqual(gr.getDiscipline(), "FP")
        self.assertEqual(gr.getGradeValue() , 9.5)
    
    def testIdentityGrade(self):
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        gr1 = Grade(st, "FP", 9.5)
        gr2 = Grade(st, "FP", 8.5)
        self.assertEqual(gr1, gr2)
