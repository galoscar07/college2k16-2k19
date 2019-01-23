'''


@author: radu


Write an application which manages the students of a faculty. 
Each student has a unique id, a name and a grade. The application should 
allow to:

F1: print all students 
F2: add students
F3: delete students
F4: show students whose grades are >= a given value
F5: find a student with the maximal grade
F6_: split the application into modules (main, ui, domain, util)
F7_: validate input data
F8_: student_id is unique - validation in add, delete etc.
F9: find all students whose name contain a string t (the match should not be
    case sensitive)  
F10: undo
F11: remove all students with the grade smaller than 5 (using TDD)
F12: sort students according to their grade (descending)  (using TDD)
F13: given an integer 'nr', find the top nr students according 
     to their grade  (using TDD)
F14: compute the average grade of all students having the grade >= 5 (using TDD)
F15: sort all students according to their grade and alphabetically (using TDD). 
------------

I1: F1, F2, F3, F4, F5
I2: F6_, F7_
I3: F8_, F9
I4: F10
I5: F11, F12, F13, F14, F15
'''
from _functools import reduce

#=============================================domain================================================

def create_student(student_id, name, grade):
    return {"student_id":student_id, "name":name, "grade":grade}

def get_student_id(student):
    return student["student_id"]

def get_name(student):
    return student["name"]

def get_grade(student):
    return student["grade"]

def add_student(students, student):
    #TODO check to unique student_id...
    students.append(student)
    
def delete_student(students, student_id):    
    students[:] = [s for s in students if get_student_id(s) != student_id]

def filter_students(students, grade):
    #TODO ??? remove the students from the list instead of returning the filtered students
    return list(filter(lambda s: get_grade(s) >= grade, students))

def find_max_grade_student(students):
    return reduce(lambda x, y:x if get_grade(x) > get_grade(y) else y, students)

#=============================================ui================================================

def read_cmd():
    command = input("command:")
    pos = command.find(" ")
    if(pos == -1):
        return (command, "")
    
    cmd = command[:pos]
    args = command[pos:]
    args = args.split(",")
    args = [e.strip() for e in args]
    
    return (cmd, args)
    

def ui_add_student(students, student_id, name, grade):
    student = create_student(int(student_id), name, int(grade))  # TODO: data validation
    add_student(students, student)


def ui_print_student(student):
    print("(student_id={0}, name={1}, grade={2})".format(
        student["student_id"], student["name"], student["grade"]), end="\t")
     
 
def ui_print_all(students):
    if len(students) == 0:
        print("the list is empty.")
    for s in students:
        ui_print_student(s)
    print()


def ui_delete_student(students, student_id):
    delete_student(students, int(student_id))  # TODO data validation
        

def ui_filter(students, grade):
    ui_print_all(filter_students(students, int(grade)))  # TODO data validation


def ui_find_max_grade_student(students):
    ui_print_student(find_max_grade_student(students))
    print()


def run_app():
    students = []
    cmds = {"add":ui_add_student, "show":ui_print_all, "delete":ui_delete_student,
            "filter":ui_filter, "max":ui_find_max_grade_student}
    while True:
        (cmd, args) = read_cmd()
        if cmd == "exit":
            break
        try:
            cmds[cmd](students, *args)
        except KeyError as ke:
            print("this command is not implemented.", ke)
        except Exception as ex:
            print("an error occurred; try again. " , ex)



#=============================================test==============================================

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
    
def test_all():
    test_add_student()
    test_delete_student()


if __name__ == '__main__':
    test_all()
    
    run_app()
    
    print("Bye")
    
    
    
    
