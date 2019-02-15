from src.controller.personController import Controller
from src.entities.validators import PersonException, PersonValidatorException
from src.repository.repository import Repository
from src.ui.ui import Ui

if __name__ == "__main__":
    print("Hallo World")

    personRepository = Repository(PersonValidatorException,"/Users/oscar/Documents/College/Fundamentals of Programming/Eclipse1/AndromedaStrain/data/list")
    personController = Controller(personRepository)

    ui = Ui(personController)
    ui.startApp()

    print("Bye Bye")