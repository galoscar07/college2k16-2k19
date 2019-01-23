from src.controller.clientController import ClientController
from src.controller.movieController import MovieController
from src.controller.rentalController import RentalController
from src.controller.statisticsController import StatisticsController
from src.controller.undoController import UndoController
from src.domain.validators import ClientValidator, MovieValidator, RentalValidator
from src.repository.fileRepository import ClientFileRepository, MovieFileRepository, RentalFileRepository
from src.repository.pickleRepository import ClientBinaryFileRepo, RentalBinaryFileRepo, MovieBinaryFileRepo
from src.repository.repository import Repository
from src.ui.ui import Ui
from src.ui.uiGraphic import UiGraphic

if __name__ == "__main__":
    print("Hello World")

    undoController = UndoController()
    file = open("/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                            "/Eclipse1/MovieRentalFinal/data/settings.properties",'r')
    for line in file:
        data = line.split("=")
        if data[1] == "textFile\n":
            clientRepository = ClientFileRepository(ClientValidator,
                                                    "/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                    "/Eclipse1/MovieRentalFinal/data/client")
            clientController = ClientController(clientRepository, undoController)
            movieRepository = MovieFileRepository(MovieValidator,
                                                  "/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                  "/Eclipse1/MovieRentalFinal/data/movie")
            movieController = MovieController(movieRepository, undoController)
            rentalRepository = RentalFileRepository(RentalValidator,
                                                    "/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                    "/Eclipse1/MovieRentalFinal/data/rental")
            rentalController = RentalController(rentalRepository, clientRepository, movieRepository, undoController)
            statisticsController = StatisticsController(clientRepository, movieRepository, rentalRepository)
            graphicUserInterface = UiGraphic(clientController,movieController,rentalController,statisticsController,undoController)
            graphicUserInterface.startUI()
            movieRepository.saved("/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                  "/Eclipse1/MovieRentalFinal/data/movie")
            clientRepository.saved("/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                    "/Eclipse1/MovieRentalFinal/data/client")
            rentalRepository.saved("/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                    "/Eclipse1/MovieRentalFinal/data/rental")

        elif data[1] == "inMemory\n":
            clientRepository = Repository(ClientValidator)
            clientController = ClientController(clientRepository, undoController)
            movieRepository = Repository(MovieValidator)
            movieController = MovieController(movieRepository, undoController)
            rentalRepository = Repository(RentalValidator)
            rentalController = RentalController(rentalRepository, clientRepository, movieRepository, undoController)
            statisticsController = StatisticsController(clientRepository, movieRepository, rentalRepository)
            userInterface = Ui(clientController, movieController, rentalController, statisticsController,
                               undoController)
            userInterface.mainMenu()


        elif data[1] == "binary\n":
            clientRepository = ClientBinaryFileRepo(ClientValidator,"/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                        "/Eclipse1/MovieRentalFinal/data/clients.pickle")
            clientController = ClientController(clientRepository,undoController)
            movieRepository = MovieBinaryFileRepo(MovieValidator,"/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                        "/Eclipse1/MovieRentalFinal/data/movie.pickle")
            movieController = MovieController(movieRepository,undoController)
            rentalRepository = RentalBinaryFileRepo(RentalValidator,"/Users/oscar/Documents/College/1st Semester/Fundamentals of Programming"
                                                        "/Eclipse1/MovieRentalFinal/data/rental.pickle")
            rentalController = RentalController(rentalRepository, clientRepository, movieRepository, undoController)
            statisticsController = StatisticsController(clientRepository, movieRepository, rentalRepository)
            userInterface = Ui(clientController, movieController, rentalController, statisticsController,
                               undoController)
            userInterface.mainMenu()

            clientRepository.saved()
            movieRepository.saved()
            rentalRepository.saved()


    #graphicUserInterface = UiGraphic(clientController,movieController,rentalController,statisticsController,undoController)
    #graphicUserInterface.startUI()

    print("Bye Bye")

