from controllers.controllers import StudentController
from domain.validators import StudentValidator
from repository.file import StudentFileRepository
from repository.inmemory import StudentRepository
from ui.console import ConsoleUI
from ui.gui import StudentGUI


#Application coordinator
#Use dependency injection pattern to asemble the application
#create a validator
val = StudentValidator()

#create repository
#repo = StudentRepository()

repo = StudentFileRepository("students.txt")

#create controller and inject dependencies
ctr = StudentController(val, repo)

#create console ui and provide (inject) the controller
#ui = ConsoleUI(ctr)
ui = StudentGUI(ctr)
ui.startUI()

