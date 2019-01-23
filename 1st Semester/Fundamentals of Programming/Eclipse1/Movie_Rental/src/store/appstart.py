'''
Created on Nov 12, 2016

@author: oscar
'''
from src.store.controller.ClientController import ClientController
from src.store.controller.MovieController import MovieController
from src.store.controller.RentalController import RentalController
from src.store.controller.StatisticsController import StatisticsController
from src.store.controller.UndoRedoController import UndoController
from src.store.domain.validators import MovieValidator,RentalValidator,ClientValidator
from src.store.repository.repository import Repository
from src.store.ui.graficUserInterface import MainMenu
from src.store.ui.menu import UI


class RedoController(object):
    pass


if __name__ == "__main__":
    print("Hello World")

    undoController = UndoController()

    movieRepository = Repository(MovieValidator)
    movieController = MovieController(movieRepository,undoController)
    movieController.startUp()

    clientRepository= Repository(ClientValidator)
    clientController= ClientController(clientRepository,undoController)
    clientController.startUp()

    rentalRepository = Repository(RentalValidator)
    rentalController = RentalController(rentalRepository,clientRepository,movieRepository,undoController)
    rentalController.startUp()

    statisticsController = StatisticsController(clientRepository,movieRepository,rentalRepository)
    print("So, what you want to do now, you want to have a grafic interface or no ?")
    print("PS: answer with yes or no!")
    command = input("Command: ")
    if command == "yes":
        console = MainMenu(movieController,clientController,rentalController,statisticsController,undoController)
        console.startUI()
    elif command =="no":
        console = UI(movieController,clientController,rentalController,statisticsController,undoController)
        console.mainmenu()
    else:
        print("Wrong anser, please run again.")

    print("Bye")
