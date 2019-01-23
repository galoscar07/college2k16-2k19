from src.controller.chocolateController import ChocolateController
from src.domain.validators import ChocolateValidators
from src.repository.repository import Repository
from src.ui.ui import Ui

if __name__ == "__main__":
    print("Hello World")

    chocolateRepository = Repository(ChocolateValidators,"/Users/oscar/Documents/College/Fundamentals of Programming/Eclipse1/ChocolateShop/data/chocolateList")
    chocolateController = ChocolateController(chocolateRepository)

    Ui = Ui(chocolateController)
    Ui.start()


    print("Bye")