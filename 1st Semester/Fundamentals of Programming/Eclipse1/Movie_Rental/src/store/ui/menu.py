'''
Created on Nov 6, 2016

@author: oscar

The application must allow the user to add, remove, update, and list both clients and movies.
'''
import datetime

class UI:
    def __init__(self, movieController,clientController,rentalController,statisticsController,undoController):
        self.__movieController = movieController
        self.__clientController = clientController
        self.__rentalController = rentalController
        self.__statisticsController = statisticsController
        self.__undoController = undoController

    @staticmethod
    def printMainMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Movie Menu\n'
        string += '\t 2 - Clients Menu\n'
        string += '\t 3 - Rent Menu\n'
        string += '\t 4 - Search Menu\n'
        string += '\t 5 - Statistics Menu\n'
        string += '\t 6 - Undo\n'
        string += '\t 7 - Redo\n'
        string += '\t 0 - Exit\n'
        print(string)
        
    @staticmethod
    def printMovieMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add a new movie into database\n'
        string += '\t 2 - Remove a movie from database\n'
        string += '\t 3 - Update a movie from database\n'
        string += '\t 4 - List all movies from database\n'
        string += '\t 0 - Back to menu\n'
        print(string)
        
    @staticmethod
    def printClientsMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add a new client into database\n'
        string += '\t 2 - Remove a client from database\n'
        string += '\t 3 - Update a client from database\n'
        string += '\t 4 - List all client from database\n'
        string += '\t 0 - Back to menu\n'
        print(string)

    @staticmethod
    def printRentMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Rent a movie\n'
        string += '\t 2 - Return a movie\n'
        string += '\t 3 - List all rents\n'
        string += '\t 0 - Back to menu'
        print(string)

    @staticmethod
    def printSearchMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - After movie id\n'
        string += '\t 2 - After movie title\n'
        string += '\t 3 - After movie genre\n'
        string += '\t 4 - After movie description\n'
        string += '\t 5 - After client id\n'
        string += '\t 6 - After client name\n'
        string += '\t 0 - Back to menu'
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


    def mainmenu(self):

        keepAlive = True
        while keepAlive:
            try:
                UI.printMainMenu()
                command = input("Enter command: ")
                command = int(command)
                if command == 0:
                    print("Thank you for using the program")
                    keepAlive = False
                elif command == 1:
                    self.MovieMenu()
                elif command == 2:
                    self.ClientMenu()
                elif command == 3:
                    self.RentMenu()
                elif command == 4:
                    self.SearchMenu()
                elif command == 5:
                    self.StatisticsMenu()
                elif command == 6:
                    self.Undo()
                elif command == 7:
                    self.Redo()
                else:
                    print("Invalid input ",command)
            except EnvironmentError as ex:               #TODO delete this exception
                print(ex)                                #TODO add store exception which should stop any exception

    def MovieMenu(self):
        UI.printMovieMenu()
        command = input("Enter command: ")
        command = int(command)
        if command == 1:
            self.addMovie()
        elif command == 2:
            self.deleteMovie()
        elif command == 3:
            self.updateMovie()
        elif command == 4:
            self.listMovies()
        elif command == 0:
            pass
        else:
            print("Invalid command!")

    def ClientMenu(self):
        UI.printClientsMenu()
        command = input("Enter command: ")
        command = int(command)
        if command == 1:
            self.addClient()
        elif command == 2:
            self.deleteClient()
        elif command == 3:
            self.updateClient()
        elif command == 4:
            self.listClients()
        elif command == 0:
            pass
        else:
            print("Invalid command ",command)

    def RentMenu(self):
        UI.printRentMenu()
        command = int(input("Command: "))
        if command == 1:
            self.rentMovie()
        elif command == 2:
            self.returnMovie()
        elif command == 3:
            self.listRent()
        elif command == 0:
            pass
        else:
            print("Invalid command ",command)

    def SearchMenu(self):
        UI.printSearchMenu()
        command = int(input("Command: "))
        if command >= 1 and command <= 4:
            self.searchMovie(command)
        elif command >= 5 and command <=6:
            self.searchClients(command)
        elif command == 0:
            pass
        else:
            print("Invalid input, ",command)

    def StatisticsMenu(self):
        UI.printStatisticsMenu()
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
            print("Invalid input, ",command)

    def mostRentedMovieMenu(self):
        UI.printStatisticsMostRentedMovie()
        command = int(input("Command: "))
        if command == 1:
            self.mostRentedMovie()
        elif command == 2:
            self.mostRentedMovieByDays()
        elif command == 0:
            pass
        else:
            print("Invalid input, ",command)


    def addClient(self):
        id = int(input("Client's id: "))
        name = input("Give a name: ")
        self.__clientController.addClient(id,name)

    def addMovie(self):
        id = int(input("Movie Id: "))
        title = input("Movie title: ")
        genre = input("Give a genre: ")
        description = input("Give a description: ")
        self.__movieController.addMovie(id,title,genre,description)

    def listClients(self):
        cl = list(self.__clientController.getAll())
        self.printClients(cl)

    def listMovies(self):
        mo = list(self.__movieController.getAll())
        self.printMovies(mo)

    def listRent(self):
        re = list(self.__rentalController.getAll())
        self.printRent(re)

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

    @staticmethod
    def printRent(re):
        if len(re) == 0:
            print("No rents to be printed")
        for i in re:
            print(i)

    def deleteClient(self):
        clientId = int(input("Give an id: "))
        self.__clientController.deleteClient(clientId)

    def deleteMovie(self):
        movieId = int(input("Give an id: "))
        self.__movieController.deleteMovie(movieId)

    def updateClient(self):
        print("At what id you want to update the name?")
        clientId = int(input("Give an id: "))
        print("And what's the name update ?")
        newname = input("Give a name: ")
        self.__clientController.updateClient(clientId,newname)

    def updateMovie(self):
        print("At what id you want to update ?")
        movieId = int(input("Give an id: "))
        print("What do you want to update?")
        print("\t 1. Movie Title")
        print("\t 2. Movie Genre")
        print("\t 3. Movie Description")
        command = int(input("Command: "))
        if command == 1:
            new = input("Give a movie title: ")
        elif command == 2:
            new = input("Give a movie genre: ")
        elif command == 3:
            new = input("Give a descriprion: ")
        self.__movieController.updateMovie(movieId,command,new)

    def rentMovie(self):
        print("What movie you want to rent? ")
        movieId = int(input("Movie Id:"))
        print("What client want to rent a movie ? ")
        clientId = int(input("client Id:"))
        rentDate = input("Rent date: ")
        rentDate = datetime.datetime.strptime(rentDate,"%d.%m.%Y").date()
        dueDate = input("Due date: ")
        dueDate = datetime.datetime.strptime(dueDate,"%d.%m.%Y").date()
        returnedDate = None
        self.__rentalController.addRental(movieId,clientId,rentDate,dueDate,returnedDate)

    def returnMovie(self):
        print("What movie you want to give back?")
        rentalId = int(input("Rental Id: "))
        returnedDate = input("Returned Date")
        returnedDate = datetime.datetime.strptime(returnedDate,"%d.%m.%Y").date()
        self.__rentalController.returnMovie(rentalId,returnedDate)

    def healpingSearch(self,string):
        string = string.lower()
        string = string.split()
        param = string[0:len(string)]
        newlist = [i for n, i in enumerate(param) if i not in param[:n]]
        return newlist


    def searchMovie(self,command):
        if command == 1:
            movieId = input("Search using id: ")
            param = self.healpingSearch(movieId)
            for i in param:
                print("Search result for: ",i)
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
                print("Search result for: ",i)
                self.printMovies(self.__movieController.searchByGenre(i))
                print()
        elif command == 4:
            description = input("Search using description: ")
            param = self.healpingSearch(description)
            for i in param:
                print("Search result for: ", i)
                self.printMovies(self.__movieController.searchByDescription(i))
                print()


    def searchClients(self,command):
        if command == 5:
            clientId = input("Search using id: ")
            param = self.healpingSearch(clientId)
            for i in param:
                print("Search result for: ", i)
                self.printClients(self.__movieController.searchById(i))
                print()
        elif command == 6:
            name = input("Search using name: ")
            param = self.healpingSearch(name)
            for i in param:
                print("Search result for: ", i)
                self.printClients(self.__clientController.searchByName(i))
                print()

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

    def Undo(self):
        self.__undoController.undo()

    def Redo(self):
        self.__undoController.redo()
