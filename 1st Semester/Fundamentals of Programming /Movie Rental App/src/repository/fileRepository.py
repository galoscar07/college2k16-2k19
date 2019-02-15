import datetime

from src.domain.entities import Client, Movie, Rental
from src.repository.repository import Repository


class ClientFileRepository(Repository):
    def __init__(self, validatorClass, path):
        """
        The function will initialize the repository
        :param validatorClass: is the validator class of the entity
        :param path: Is the place from where we will read the values which will be put into the controllers
        """
        super().__init__(validatorClass)
        self.__path = path
        self.__loadFromFile(self.__path)

    def __loadFromFile(self,path):
        """
        The function will load from file the
        :param path: is the file from where we will save items
        :return: The function will return the controller of the class whit elements loaded from file
        """
        file = open(path, 'r')
        for line in file:
            if line != "\n":
                line.strip("\n")
                data = line.split("Ω")
                clientId = int(data[0].strip("\n"))
                name = data[1]
                client = Client(clientId,name)
                super().save(client)

    def saved(self,path):
        fi = open(path, 'w')
        li = self.getAll()
        for i in li:
            print(i.entityId,"Ω",i.name, file = fi)

class MovieFileRepository(Repository):
    def __init__(self,validatorClass, path):
        """
        The function will initialize the repository
        :param validatorClass: is the validator class of the entity
        :param path: Is the place from where we will read the values which will be put into the controllers
        """
        super().__init__(validatorClass)
        self.__path = path
        self.__loadFromFile(self.__path)

    def __loadFromFile(self,path):
        """
        The function will load from file the
        :param path: is the file from where we will save items
        :return: The function will return the controller of the class whit elements loaded from file
        """
        file = open(path,'r')
        for line in file:
            if line != "\n":
                line.strip("\n")
                data = line.split("Ω")
                movieId = int(data[0].strip("\n"))
                title = data[1]
                genre = data[2]
                description = data[3]
                movie = Movie(movieId,title,genre,description)
                super().save(movie)

    def saved(self,path):
        fi = open(path, 'w')
        li = self.getAll()
        for i in li:
            print(i.entityId,"Ω",i.title,"Ω",i.genre,"Ω",i.description, file = fi)

class RentalFileRepository(Repository):
    def __init__(self,validatorClass, path):
        """
        The function will initialize the repository
        :param validatorClass: is the validator class of the entity
        :param path: Is the place from where we will read the values which will be put into the controllers
        """
        super().__init__(validatorClass)
        self.__path = path
        self.__loadFromFile(self.__path)

    def __loadFromFile(self,path):
        """
        The function will load from file the
        :param path: is the file from where we will save items
        :return: The function will return the controller of the class whit elements loaded from file
        """
        file = open(path,'r')
        c = 0
        for line in file:
            if line != "\n":
                line.strip("\n")
                datac = line.split("Ω")
                if len(datac) == 5:
                    movieId = int(datac[0].strip())
                    clientId = int(datac[1].strip())
                    rentedDatec = datac[2].strip()
                    rentedDate = datetime.datetime.strptime(rentedDatec,"%Y-%m-%d").date()
                    dueDatec = datac[3].strip()
                    dueDate = datetime.datetime.strptime(dueDatec, "%Y-%m-%d").date()
                    returnedDate = None
                    rent = Rental(c,movieId,clientId,rentedDate,dueDate,returnedDate)
                    super().save(rent)
                else:
                    movieId = int(datac[0].strip())
                    clientId = int(datac[1].strip())
                    rentedDatec = datac[2].strip()
                    rentedDate = datetime.datetime.strptime(rentedDatec,"%Y-%m-%d").date()
                    dueDatec = datac[3].strip()
                    dueDate = datetime.datetime.strptime(dueDatec, "%Y-%m-%d").date()
                    returnedDatec = datac[4].strip()
                    returnedDate = datetime.datetime.strptime(returnedDatec, "%Y-%m-%d").date()
                    rent = Rental(c,movieId, clientId, rentedDate, dueDate, returnedDate)
                    super().save(rent)
                c += 1


    def saved(self,path):
        fi = open(path, 'w')
        li = self.getAll()
        for i in li:
            print(i.movieId,"Ω",i.clientId,"Ω",i.rentDate,"Ω",i.dueDate,"Ω",i.returnedDate, file = fi)