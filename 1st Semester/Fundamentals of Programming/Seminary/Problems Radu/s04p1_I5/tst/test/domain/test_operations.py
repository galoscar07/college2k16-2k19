'''

@author: radu
'''


from s02p1.domain.entities import create_student, get_grade
from s02p1.domain.operations import add_student, remove_smaller_than, \
    sort_students_by_grade, find_top_students, compute_avg_grade, \
    sort_students_by_grade_and_by_name


def setUp():
    students = []
    students.append(create_student("sid1", "sn1", 10))
    students.append(create_student("sid2", "sn2", 9))
    return students

def test_add_student():
    l = setUp()
    assert(len(l) == 2)
    
    add_student(l, create_student("sid3", "sn3", 9))
    assert(len(l) == 3)
    
def test_delete_student():
    pass


def test_remove_smaller_than():
    l = setUp()
    
    remove_smaller_than(l, 10)
    assert(len(l) == 1)
    


def test_sort_students_by_grade():
    l = setUp() 
    l.append(create_student(3, "s3", 7))
    l.append(create_student(4, "s4", 8))
    
    result = sort_students_by_grade(l)
    grades = [get_grade(student) for student in result]
    for i in range(len(grades) - 1):
        assert(grades[i] >= grades[i + 1])


def test_find_top_students():
    l = setUp()
    
    result = find_top_students(l, 1)
    assert(len(result) == 1)
    assert(get_grade(result[0]) == 10)   


def test_compute_avg_grade():
    l = setUp()    
    
    avg_grade = compute_avg_grade(l, 5)
    assert(avg_grade == 9.5)
    


def test_sort_students_by_grade_and_by_name():
    l = setUp()
    l.append(create_student(3, "s3", 7))
    l.append(create_student(4, "s4", 8))
    l.append(create_student(5, "s6b", 6))
    l.append(create_student(6, "s6a", 6))
    
    result = sort_students_by_grade_and_by_name(l)
    grades = [get_grade(student) for student in result]
    for i in range(len(grades) - 1):
        assert(grades[i] <= grades[i + 1])
    

#=======================================================================================================

def test_all_operations():
    test_add_student()
    test_delete_student()
    test_remove_smaller_than()
    test_sort_students_by_grade()
    test_find_top_students()
    test_compute_avg_grade()
    test_sort_students_by_grade_and_by_name()
