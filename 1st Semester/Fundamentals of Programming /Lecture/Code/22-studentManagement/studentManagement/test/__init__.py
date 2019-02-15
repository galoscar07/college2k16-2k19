from examples.studentManagement.domain.entities import *
from examples.studentManagement.repository.inmemory import *

def testStoreGrade():
    st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
    gr = Grade(st, "FP", 9.5)
    rep = GradeRepository()
    assert rep.size()==0
    rep.store(gr)
    assert rep.size()==1
    gr2 = rep.find(st,"FP")
    assert gr2==gr

    gr = Grade(st, "FP", 9)
    try:
        rep.store(gr)
        assert False
    except GradeAlreadyAssignedException:
        assert True

testStoreGrade()

def testGetGrades():
    st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
    gr = Grade(st, "FP", 10)
    rep = GradeRepository()
    rep.store(gr)
    gr = Grade(st, "SO", 9.5)
    rep.store(gr)
    grades = rep.getAll(st)
    assert grades[0].getStudent()==st
    assert grades[0].getGrade()==10
    assert grades[0].getDiscipline()=="FP"

testGetGrades()

def testGetStudentGrades():
    """
     Test function for getForDisc
    """
    rep = GradeRepository()

    st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
    gr = Grade(st, "FP", 10)
    rep.store(gr)
    gr = Grade(st, "SO", 9.5)
    rep.store(gr)

    studentGrades = rep.getAllForDisc("FP")
    assert len(studentGrades)==1
    assert studentGrades[0].getStudentID()=="1"
    assert studentGrades[0].getGrade()==10
    assert studentGrades[0].getDiscipline()=="FP"

    st = Student("2", "Ionel", Address("Adr2", 22, "Cluj"))
    gr = Grade(st, "SO", 9.5)
    rep.store(gr)
    studentGrades = rep.getAllForDisc("SO")
    assert len(studentGrades)==2
    assert studentGrades[0].getStudentID()=="1"
    assert studentGrades[1].getStudentID()=="2"

testGetStudentGrades()