'''

@author: radu
'''
from _functools import reduce

from s02p1.domain.entities import get_student_id, get_grade


def validate_student(student):
    """Validate a student entity.
    
    Arguments:
        student - which has a student_id: int, name: string, grade: int.
    Returns: -
    Exceptions:
        Exception - if the student is not valid, i.e., grade has to be between 1 and 10 etc.
    """
    if get_grade(student) < 1 or get_grade(student) > 10:
        raise Exception("student grade must be between 1 and 10.")
    #TODO validate student_id, etc.

def add_student(students, student):
    # TODO check to unique student_id...
    students.append(student)
    
def delete_student(students, student_id):    
#     for student in students[:]:
#         if get_student_id(student)==student_id:
#             students.remove(student)
#             break 
    students[:] = [s for s in students if get_student_id(s) != student_id]

def filter_students(students, grade):
    # TODO ??? remove the students from the list instead of returning the filtered students
    return list(filter(lambda s: get_grade(s) >= grade, students))

def find_max_grade_student(students):
    return reduce(lambda x, y:x if get_grade(x) > get_grade(y) else y, students)

