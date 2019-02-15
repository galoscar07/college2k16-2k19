import datetime

from src.domain.validators import StoreException


class Ui(object):
    """

    """
    def __init__(self,clientController,movieController,rentalController,statisticsController,undoControler):
        self.__clientController = clientController
        self.__movieController = movieController
        self.__rentalController = rentalController
        self.__statisticsController = statisticsController
        self.__undoController = undoControler

    @staticmethod
    def printMainMenu():
        string = "Available commands:\n"
        string += "\t 1 - Client Menu \n"
        string += "\t 2 - Movie Menu \n"
        string += "\t 3 - Rent Menu \n"
        string += "\t 4 - Search Menu \n"
        string += "\t 5 - Statistics Menu \n"
        string += "\t 6 - Undo \n"
        string += "\t 7 - Redo \n"
        string += "\t 0 - Exit \n"
        print(string)

    @staticmethod
    def printClientMenu():
        string = "Available commands:\n"
        string += "\t 1 - Add a client\n"
        string += "\t 2 - Delete a client\n"
        string += "\t 3 - Update a client\n"
        string += "\t 4 - List all clients\n"
        print(string)

    @staticmethod
    def printMovieMenu():
        string = "Available commands:\n"
        string += "\t 1 - Add a movie\n"
        string += "\t 2 - Delete a movie\n"
        string += "\t 3 - Update a movie\n"
        string += "\t 4 - List all movies\n"
        print(string)

    @staticmethod
    def printRentMenu():
        string = "Available Commands:\n"
        string += "\t 1 - Rent a movie \n"
        string += "\t 2 - Return a movie \n"
        string += "\t 3 - List Rents"
        print(string)

    @staticmethod
    def printSearchMenu():
        string = "Available commands \n"
        string += "\t 1 - Search movies by id \n"
        string += "\t 2 - Search movies by title \n"
        string += "\t 3 - Search movies by genre \n"
        string += "\t 4 - Search movies by description \n"
        string += "\t 5 - Search clients by id \n"
        string += "\t 6 - Search clients by name \n"
        print(string)

    @staticmethod
    def printStatisticsMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Most rented movie\n'
        string += '\t 2 - Most activ clients\n'
        string += '\t 3 - All movie currently rented\n'
        string += '\t 4 - Late Rentals\n'
        string += '\t 0 - Back to menu'
        print(string)

    @staticmethod
    def printStatisticsMostRentedMovie():
        string = '\nAvailable commands:\n'
        string += '\t 1 - By the number of times they were rented\n'
        string += '\t 2 - By the number of days they were rented\n'
        string += '\t 0 - Back to menu'
        print(string)

    def mainMenu(self):
        keepAlive = True
        while keepAlive:
            try:
                Ui.printMainMenu()
                command = int(input("Enter command: "))
                if command == 0:
                    print("Thank you for using the program")
                    keepAlive = False
                elif command == 1:
                    self.clientMenu()
                elif command == 2:
                    self.movieMenu()
                elif command == 3:
                    self.rentMenu()
                elif command == 4:
                    self.searchMenu()
                elif command == 5:
                    self.statisticsMenu()
                elif command == 6:
                    self.undo()
                elif command == 7:
                    self.redo()
                else:
                    print("Invali input, sorry ...")
            except StoreException as e:
                print(e)
            except Exception as e:
                print(e)            #TODO change exception in StoreException and add Exception/general


    def clientMenu(self):
        Ui.printClientMenu()
        command = int(input("Enter command: "))
        if command == 0:
            pass
        elif command == 1:
            self.addClient()
        elif command == 2:
            self.deleteClient()
        elif command == 3:
            self.updateClient()
        elif command == 4:
            self.listClients()
        else:
            print("Invalid input, sorry ...")

    def movieMenu(self):
        Ui.printMovieMenu()
        command = int(input("Enter command: "))
        if command == 0:
            pass
        elif command == 1:
            self.addMovie()
        elif command == 2:
            self.deleteMovie()
        elif command == 3:
            self.updateMovie()
        elif command == 4:
            self.listMovies()
        else:
            print("Invalid input, sorry ...")

    def rentMenu(self):
        Ui.printRentMenu()
        command = int(input("Enter command: "))
        if command == 0:
            pass
        elif command == 1:
            self.rentMovie()
        elif command == 2:
            self.returnMovie()
        elif command == 3:
            self.listRent()
        else:
            print("Invalid input, sorry ... ")

    def searchMenu(self):
        Ui.printSearchMenu()
        command = int(input("Command: "))
        if command >= 1 and command <= 4:
            self.searchMovie(command)
        elif command >= 5 and command <=6:
            self.searchClients(command)
        elif command == 0:
            pass
        else:
            print("Invalid input, ",command)

    def statisticsMenu(self):
        Ui.printStatisticsMenu()
        command = int(input("Command: "))
        if command == 1:
            self.mostRentedMovieMenu()
        elif command == 2:
            self.mostActiveClients()
        elif command == 3:
            self.allCurrentlyRented()
        elif command == 4:
            self.lateRentals()
        elif command == 0:
            pass
        else:
            print("Invalid input, ", command)

    def mostRentedMovieMenu(self):
        Ui.printStatisticsMostRentedMovie()
        command = int(input("Command: "))
        if command == 1:
            self.mostRentedMovie()
        elif command == 2:
            self.mostRentedMovieByDays()
        elif command == 0:
            pass
        else:
            print("Invalid input, ", command)


    def addClient(self):
        clientId = int(input("Give an id: "))
        name = input("Give a name: ")
        self.__clientController.addClient(clientId,name)

    def deleteClient(self):
        clientId = int(input("Give an id: "))
        self.__clientController.deleteClient(clientId)


    def updateClient(self):
        clientId = int(input("Give an id: "))
        newName = input("New name: ")
        self.__clientController.clientUpdate(clientId,newName)

    def listClients(self):
        cl = list(self.__clientController.getAll())
        if len(cl) == 0:
            print("Their is no client to be printed.")
        else:
            for i in cl:
                print(i)

    def addMovie(self):
        movieId = int(input("Give an id: "))
        title = input("Give a title: ")
        genre = input("Give a genre: ")
        description = input("Give a description: ")
        self.__movieController.addMovie(movieId,title,genre,description)


    def deleteMovie(self):
        movieId = int(input("Give an id: "))
        self.__movieController.deleteMovie(movieId)

    def updateMovie(self):
        movieId = int(input("Give an id: "))
        print("ps: if you don't want to modifi something just press enter")
        title = input("Give a new title: ")
        genre = input("Give a new genre: ")
        description = input("Give a new description: ")
        self.__movieController.updateMovie(movieId, title, genre, description)

    def listMovies(self):
        mo = list(self.__movieController.getAll())
        if len(mo) == 0:
            print("Their is no movie to be printed.")
        else:
            for i in mo:
                print(i)

    def rentMovie(self):
        print("What movie you want to rent? ")
        movieId = int(input("Movie Id:"))
        print("What client want to rent a movie ? ")
        clientId = int(input("client Id:"))
        rentDate = input("Rent date: ")
        rentDate = datetime.datetime.strptime(rentDate, "%d.%m.%Y").date()
        dueDate = input("Due date: ")
        dueDate = datetime.datetime.strptime(dueDate, "%d.%m.%Y").date()
        returnedDate = None
        self.__rentalController.addRental(movieId, clientId, rentDate, dueDate, returnedDate)

    def returnMovie(self):
        print("What movie you want to give back?")
        rentalId = int(input("Rental Id: "))
        returnedDate = input("Returned Date")
        returnedDate = datetime.datetime.strptime(returnedDate, "%d.%m.%Y").date()
        self.__rentalController.returnMovie(rentalId, returnedDate)

    def listRent(self):
        re = list(self.__rentalController.getAll())
        if len(re) == 0:
            print("Their is no rental to be printed.")
        else:
            for i in re:
                print(i)

    def healpingSearch(self, string):
        string = string.lower()
        string = string.split()
        param = string[0:len(string)]
        newlist = [i for n, i in enumerate(param) if i not in param[:n]]
        return newlist

    def searchMovie(self, command):
        if command == 1:
            movieId = input("Search using id: ")
            param = self.healpingSearch(movieId)
            for i in param:
                print("Search result for: ", i)
                self.printMovies(self.__movieController.searchById(i))
                print()
        elif command == 2:
            title = input("Search using title: ")
            param = self.healpingSearch(title)
            for i in param:
                print("Search result for: ", i)
                self.printMovies(self.__movieController.searchByTitle(i))
                print()
        elif command == 3:
            genre = input("Search using genre: ")
            param = self.healpingSearch(genre)
            for i in param:
                print("Search result for: ", i)
                self.printMovies(self.__movieController.searchByGenre(i))
                print()
        elif command == 4:
            description = input("Search using description: ")
            param = self.healpingSearch(description)
            for i in param:
                print("Search result for: ", i)
                self.printMovies(self.__movieController.searchByDescription(i))
                print()

    def searchClients(self, command):
        if command == 5:
            clientId = input("Search using id: ")
            param = self.healpingSearch(clientId)
            for i in param:
                print("Search result for: ", i)
                self.printClients(self.__clientController.searchById(i))
                print()
        elif command == 6:
            name = input("Search using name: ")
            param = self.healpingSearch(name)
            for i in param:
                print("Search result for: ", i)
                self.printClients(self.__clientController.searchByName(i))
                print()

    @staticmethod
    def printClients(cl):
        if len(cl) == 0:
            print("No clients to be printed")
        for i in cl:
            print(i)

    @staticmethod
    def printMovies(mo):
        if len(mo) == 0:
            print("No movies to be printed")
        for i in mo:
            print(i)

    def mostRentedMovie(self):
        print("By the number of time: ")
        top = self.__statisticsController.topByMostRentedTimes()
        for i in top:
            print(i)

    def mostRentedMovieByDays(self):
        print("By the number of days: ")
        top = self.__statisticsController.topByMostRentedDays()
        for i in top:
            print(i)

    def mostActiveClients(self):
        print("Most active clients list sorted: ")
        most = self.__statisticsController.mostActiveClients()
        for i in most:
            print(i)

    def allCurrentlyRented(self):
        print("All currently rented movies are: ")
        most = self.__statisticsController.allCurrentlyRented()
        for i in most:
            print(i)

    def lateRentals(self):
        print("The late rentals are: ")
        most = self.__statisticsController.lateRentals()
        for i in most:
            print(i)

    def undo(self):
        self.__undoController.undo()

    def redo(self):
        self.__undoController.redo()