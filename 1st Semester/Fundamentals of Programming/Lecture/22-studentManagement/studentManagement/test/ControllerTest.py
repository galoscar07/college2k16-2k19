'''
Created on Nov 21, 2016

@author: Arthur
'''
import unittest
from examples.studentManagement.controller.StudentController import StudentController
from examples.studentManagement.controller.GradeController import GradeController
from examples.studentManagement.repository.StudentRepository import StudentRepository
from examples.studentManagement.repository.GradeRepository import GradeRepository
from examples.studentManagement.domain.StudentValidator import StudentValidator
from examples.studentManagement.domain.GradeValidator import GradeValidator
from examples.studentManagement.domain.Exceptions import ValidationException
from examples.studentManagement.repository.Exceptions import DuplicateIDException


class ControllerTest(unittest.TestCase):
    def testCreateStudent(self):
        """
         test function for create student
         Feature 1 - add a student
         Task 4 - Create student - controller
        """
        ctr = StudentController(StudentValidator(), StudentRepository())
        st = ctr.create("1", "Ion", "Cluj-Napoca", "Turda", "Addr")
        self.assertEqual(st.getId(), "1")
        self.assertEqual(st.getName(), "Ion")
        self.assertEqual(st.getAddr().getStreet(), "Addr")
        self.assertEqual(ctr.getNrStudents(), 1)

        """
            Test for invalid Student instance
        """
        try:
            ctr.create("1", "", "", 1, "Cluj")
            self.assertTrue(False)
        except ValidationException:
            pass
        
        """
            Test for duplicate id
        """
        try:
            ctr.create("1", "Ion2", "Adr2", 1, "Cluj")
            self.assertTrue(False)
        except DuplicateIDException:
            pass
    
    def testRemoveStudent(self):
        ctr = StudentController(StudentValidator(), StudentRepository())
        ctr.create("1", "Ion", "Cluj", "Dej", "Clujului 82")
        
        """
            Test for invalid id
        """
        try:
            ctr.remove("2")
            self.assertTrue(False)
        except ValueError:
            pass
        
        self.assertEqual(ctr.getNrStudents() , 1)
    
        st = ctr.remove("1")
        self.assertEqual(ctr.getNrStudents() , 0)
        self.assertEqual(st.getId(), "1")
        self.assertEqual(st.getName() , "Ion")
        self.assertEqual(st.getAddr().getStreet() , "Clujului 82")
    
    def testSearchCriteria(self):
        rep = StudentRepository()
        ctr = StudentController(StudentValidator(), rep)
        ctr.create("1", "Ion", "Adr", 1, "Cluj")
        st2 = ctr.create("2", "Ion2", "Adr", 1, "Cluj")
        ctr.create("3", "Ioana1", "Adr", 1, "Cluj")
        st4 = ctr.create("4", "Ioana2", "Adr", 1, "Cluj")
        ctr.create("5", "Vlad", "Adr", 1, "Cluj")
    
        studs = ctr.search("Ion")
        self.assertEqual(len(studs) , 2)
        self.assertTrue(st2 in studs)
    
        studs = ctr.search("Io")
        self.assertEqual(len(studs) , 4)
        self.assertTrue(st4 in studs)
    
        studs = ctr.search("Al")
        self.assertEqual(len(studs) , 0)
    
        studs = ctr.search("")
        self.assertEqual(len(studs) , 5)
    
    def testUpdate(self):
        ctr = StudentController(StudentValidator(), StudentRepository())
        ctr.create("1", "Ion", "Cluj", "Turda", "Adr1")
        st = ctr.update("1", "Ionel", "Cluj", "Dej", "Clujului")
    
        studs = ctr.search("Ionel")
        self.assertEqual(len(studs) , 1)
        self.assertEqual(studs[0].getAddr().getStreet() , "Clujului")
        
        """
            Verify the old student is returned
        """
        self.assertEqual(st.getName() , "Ion")
        self.assertEqual(st.getAddr().getStreet() , "Adr1")
    
        """
            Try to update an inexisting student
        """
        try:
            st = ctr.update("2", "Ionel", "Addrr", 1, "Cluj")
            self.assertTrue(False)
        except ValueError:
            pass
    
        """
            Try to update to invalid data
        """
        try:
            ctr.update("1", "", "", 1, "Cluj")
            self.assertTrue(False)
        except ValidationException:
            pass

    def testAssignGrade(self):
        stRep = StudentRepository()
        stctr = StudentController(StudentValidator(), stRep)
        stctr.create("1", "Ion", "Cluj", "Turda", "Addrr8")
        ctr = GradeController(GradeRepository(), GradeValidator(), stRep)
    
        gr = ctr.assign("1", "FP", 10)
        self.assertEqual(gr.getDiscipline() , "FP")
        self.assertEqual(gr.getGradeValue() , 10)
        self.assertEqual(gr.getStudent().getId() , "1")
        self.assertEqual(gr.getStudent().getName() , "Ion")
    
    def testListGrade(self):
        stRep = StudentRepository()
        stctr = StudentController(StudentValidator(), stRep)
        stctr.create("1", "Ion", "Adr", 1, "Cluj")
    
        ctr = GradeController(GradeRepository(), GradeValidator(), stRep)
        gr = ctr.assign("1", "FP", 10)
        grs = ctr.listGrades("1")
        self.assertEqual(len(grs) , 1)
        gr = ctr.assign("1", "SO", 10)
        grs = ctr.listGrades("1")
        self.assertEqual(len(grs) , 2)
    
    def testListFirst5(self):
        stRep = StudentRepository()
        stctr = StudentController(StudentValidator(), stRep)
        stctr.create("1", "Ion", "Cluj","Gherla","Turzii")
        stctr.create("2", "Ion2", "Cluj","Gherla","Turzii")
        stctr.create("3", "Ion3", "Cluj","Gherla","Turzii")
        stctr.create("4", "Ion4", "Cluj","Gherla","Turzii")
        stctr.create("5", "Ion5", "Cluj","Gherla","Turzii")
        stctr.create("6", "Ion6", "Cluj","Gherla","Turzii")
    
        ctr = GradeController(GradeRepository(), GradeValidator(), stRep)
        ctr.assign("1", "FP", 2)
        ctr.assign("2", "FP", 7)
        ctr.assign("3", "FP", 8)
        ctr.assign("4", "FP", 10)
        ctr.assign("5", "FP", 6)
        ctr.assign("6", "FP", 9)
    
        stgrs = ctr.getTop5("FP")
        self.assertEqual(len(stgrs) , 5)
        self.assertEqual(stgrs[0].getStudentId() , "4")
        self.assertEqual(stgrs[1].getStudentId() , "6")
        self.assertEqual(stgrs[2].getStudentId() , "3")
        self.assertEqual(stgrs[3].getStudentId() , "2")
        self.assertEqual(stgrs[4].getStudentId() , "5")





