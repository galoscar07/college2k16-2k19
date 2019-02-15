'''
Created on Nov 20, 2016

@author: Arthur
'''
from examples.studentManagement.repository.StudentRepository import StudentRepository
from examples.studentManagement.repository.GradeRepository import GradeRepository
from examples.studentManagement.domain.Student import Student, Address
from examples.studentManagement.domain.Grade import Grade
from examples.studentManagement.repository.Exceptions import DuplicateIDException, GradeAlreadyAssignedException

import unittest

class StudentRepositoryTest(unittest.TestCase):
    def testStoreStudent(self):
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        rep = StudentRepository()

        """
            Test adding students
        """        
        self.assertEqual(rep.size() , 0)
        rep.store(st)
        self.assertEqual(rep.size() , 1)
        st2 = Student("2", "Vasile", Address("Adr2", 1, "Cluj"))
        rep.store(st2)
        self.assertEqual(rep.size() , 2)
        
        """
            Test with duplicate student id
        """
        st3 = Student("2", "Ana", Address("Adr3", 1, "Cluj"))
        try:
            rep.store(st3)
            self.assertTrue(False)
        except DuplicateIDException:
            pass
    
    def testDeleteStudent(self):
        rep = StudentRepository()
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        rep.store(st)
        st = Student("2", "Ion2", Address("Adr2", 1, "Cluj"))
        rep.store(st)
        self.assertEqual(rep.size() , 2)
        rep.remove("1")
        self.assertEqual(rep.size() , 1)

        try:
            rep.remove("3")
            self.assertTrue(False)
        except ValueError:
            pass

    def testListStudent(self):
        rep = StudentRepository()
        st = Student("1", "Ion", Address("Tulcea","Tulcea","Adr1"))
        rep.store(st)
        st = Student("2", "Ion2", Address("Cluj","Cluj-Napoca","Adr2"))
        rep.store(st)
    
        allStudents = rep.getAll()
        self.assertEqual(len(allStudents) , 2)
        st1 = rep.find("1")
        self.assertEqual(st1.getId() , "1")
        self.assertEqual(st1.getName() , "Ion")
        self.assertEqual(st1.getAddr().getStreet() , "Adr1")
        
        st2 = rep.find("2")
        self.assertEqual(st2.getId() , "2")
        self.assertEqual(st2.getName() , "Ion2")
        self.assertEqual(st2.getAddr().getStreet() , "Adr2")


    def testUpdate(self):
        rep = StudentRepository()
        st = Student("1", "Ion", Address("Cluj", "Cluj-Napoca", "Adr"))
        rep.store(st)
        st = Student("1", "Ionel", Address("Bihor", "Oradea", "Adr8"))
        rep.update("1", st)

        self.assertEqual(rep.find("1").getName() , "Ionel")
        self.assertEqual(rep.find("1").getAddr().getStreet() , "Adr8")
    
        try:
            rep.update("2", st)
            self.assertTrue(False)
        except ValueError:
            pass

class GradeRepositoryTest(unittest.TestCase):
    def testStoreGrade(self):
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        rep = GradeRepository()
        self.assertEqual(rep.size() , 0)

        gr1 = Grade(st, "FP", 9.5)
        rep.store(gr1)
        self.assertEqual(rep.size() , 1)
        gr2 = rep.find(st, "FP")
        self.assertEqual(gr2 , gr1)
    
        gr1 = Grade(st, "FP", 9)
        try:
            rep.store(gr1)
            self.assertTrue(False)
        except GradeAlreadyAssignedException:
            pass
    
    def testGetGrades(self):
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        gr = Grade(st, "FP", 10)
        rep = GradeRepository()
        rep.store(gr)
        gr = Grade(st, "SO", 9.5)
        rep.store(gr)
        grades = rep.getAll(st)
        self.assertEqual(grades[0].getStudent() , st)
        self.assertEqual(grades[0].getGradeValue() , 10)
        self.assertEqual(grades[0].getDiscipline() , "FP")
    
    def testGetStudentGrades(self):
        rep = GradeRepository()
    
        st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
        gr = Grade(st, "FP", 10)
        rep.store(gr)
        gr = Grade(st, "SO", 9.5)
        rep.store(gr)
    
        studentGrades = rep.getAllForDisc("FP")
        self.assertEqual(len(studentGrades) , 1)
        self.assertEqual(studentGrades[0].getStudentId() , "1")
        self.assertEqual(studentGrades[0].getGradeValue() , 10)
        self.assertEqual(studentGrades[0].getDiscipline() , "FP")
    
        st = Student("2", "Ionel", Address("Adr2", 22, "Cluj"))
        gr = Grade(st, "SO", 9.5)
        rep.store(gr)
        studentGrades = rep.getAllForDisc("SO")
        self.assertEqual(len(studentGrades) , 2)
        self.assertEqual(studentGrades[0].getStudentId() , "1")
        self.assertEqual(studentGrades[1].getStudentId() , "2")


