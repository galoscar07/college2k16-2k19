from examples.studentManagement.repository.GradeCSVFileRepository import GradeCSVFileRepository
from examples.studentManagement.repository.StudentCSVFileRepository import StudentCSVFileRepository

from examples.studentManagement.domain.GradeValidator import GradeValidator 
from examples.studentManagement.domain.StudentValidator import StudentValidator
from examples.studentManagement.controller.StudentController import StudentController
from examples.studentManagement.controller.GradeController import GradeController
from examples.studentManagement.ui.Console import ConsoleUI
from examples.studentManagement.repository.StudentPickleFileRepository import StudentPickleFileRepository
from examples.studentManagement.repository.GradeRepository import GradeRepository
from examples.studentManagement.repository.GradePickleFileRepository import GradePickleFileRepository

"""
    1. Set up entity validators
"""
studentValidator = StudentValidator()
gradeValidator = GradeValidator()

"""
    2. Initialize the repositories
"""
# studentRepo = StudentCSVFileRepository("students.txt")
studentRepo = StudentPickleFileRepository()
# gradeRepo = GradeCSVFileRepository(studentRepo, "grades.txt")
gradeRepo = GradePickleFileRepository(studentRepo)

"""
    3. Initialize GRASP controllers
"""
studentController = StudentController(studentValidator, studentRepo)
gradeController = GradeController(gradeRepo, gradeValidator, studentRepo)

"""
    4. Start up the UI
"""
ui = ConsoleUI(studentController, gradeController)
ui.startUI()