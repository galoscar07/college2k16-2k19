import datetime

from src.store.domain.dto import DTOAssembler


class StatisticsController(object):
    """
    The class will return statistics made with informations from controllers
    """
    def __init__(self,clientRepository,movieRepository,rentalRepository):
        """
        The controllers are in here because we will take information from them
        """
        self.__clientRepository = clientRepository
        self.__movieRepository = movieRepository
        self.__rentalRepository = rentalRepository

    def howManyTimesRented(self,movieId):
        """
        The function will return the numbers of times a movies has been rented
        """
        lis = self.__rentalRepository.getAll()
        c = 0
        for i in lis:
            if i.movieId == movieId:
                c = c+1
        return c

    def howManyDaysRented(self,movieId):
        """
        The function will return the numbers of days the movies has been rented
        """
        today = datetime.datetime.now().date()
        lis = self.__rentalRepository.getAll()
        d = 0
        for i in lis:
            if i.movieId == movieId:
                if i.returnedDate is not None:
                    d = d + (i.returnedDate - i.rentDate).days
                else:
                    d = d + (today - i.rentDate).days
        return d

    def topByMostRentedTimes(self):
        """
        The function will realize a top in descending order of the movies by the times they were rented
        :return: a list with the condition from above
        """
        lis = self.__movieRepository.getAll()
        top = []
        for i in lis:
            top.append(DTOAssembler.createMostRentedMovieDTO(i.title,self.howManyTimesRented(i.entityId)))
        top = sorted(top, key=lambda d: d.nrTimeRented, reverse=True)
        return top

    def topByMostRentedDays(self):
        """
        The function will realize a top in descending order of the movies by the days the movies were rented
        :return: a list with the condition from above
        """
        lis = self.__movieRepository.getAll()
        top = []
        for i in lis:
            top.append(DTOAssembler.createMostRentedMovieDaysDTO(i.title,self.howManyDaysRented(i.entityId)))
        top = sorted(top, key=lambda d: d.nrDays, reverse=True)
        return top


    def howManyDaysClientRented(self,clientId):
        """
        The function will return how many days a client rented a movie
        :return: a number which represents the number of days a client rented movies
        """
        today = datetime.datetime.now().date()
        lis = self.__rentalRepository.getAll()
        c = 0
        for i in lis:
            if i.clientId == clientId:
                if i.returnedDate is not None:
                    c = c + (i.returnedDate - i.rentDate).days
                else:
                    c = c + (today - i.rentDate).days
        return c

    def mostActiveClients(self):
        """
        The function will return a list in descending order of the most active clients
        """
        lis = self.__clientRepository.getAll()
        top = []
        for i in lis:
            top.append(DTOAssembler.createMostActiveClientsDTO(i.name,self.howManyDaysClientRented(i.entityId)))
        top = sorted(top, key = lambda d: d.nrDay, reverse = True)
        return top

    def allCurrentlyRented(self):
        """
        The function will return a list of the currently rented movies
        """
        lis = self.__rentalRepository.getAll()
        top = []
        for i in lis:
            if i.returnedDate == None:
                top.append(DTOAssembler.createAllCurrentlyRentedDTO(i.entityId,
                                                                    self.__movieRepository.findById(i.movieId).title))
        return top

    def lateRentals(self):
        """
        The function will return a list sorted decreasing by the number of days a movie is late to return.
        :return:
        """
        today = datetime.datetime.now().date()
        lis = self.__rentalRepository.getAll()
        top = []
        for i in lis:
            if i.dueDate < today:
                top.append(DTOAssembler.createLateRentalDTO(i.entityId,(today-i.dueDate).days))
        top = sorted(top, key = lambda d: d.nrDay, reverse = True)
        return top