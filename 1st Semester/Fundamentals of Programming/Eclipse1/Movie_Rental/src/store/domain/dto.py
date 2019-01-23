class DTOAssembler(object):
    """
    This class will only create elemens for statistics
    """
    @staticmethod
    def createMostRentedMovieDTO(title,nrTimeRented):
        return MostRentedMovieDTO(title,nrTimeRented)

    @staticmethod
    def createMostRentedMovieDaysDTO(title,nrDays):
        return MostRentedMovieDaysDTO(title,nrDays)

    @staticmethod
    def createMostActiveClientsDTO(clientName, nrDay):
        return MostActiveClientsDTO(clientName, nrDay)

    @staticmethod
    def createAllCurrentlyRentedDTO(rentalId, movieTitle):
        return AllRentalsDTO(rentalId,movieTitle)

    @staticmethod
    def createLateRentalDTO(rentalId,nrDay):
        return LateRentalDTO(rentalId,nrDay)


class MostRentedMovieDaysDTO():
    """
    This classed is used for the most Rented Movies by Days
    """
    def __init__(self, movieTitle, nrDays):
        self.__movieTitle = movieTitle
        self.__nrDays = nrDays

    @property
    def movieTitle(self):
        return self.__movieTitle

    @movieTitle.setter
    def movieTitle(self, value):
        self.__movieTitle = value

    @property
    def nrDays(self):
        return self.__nrDays

    @nrDays.setter
    def nrDays(self, value):
        self.__nrDays = value

    def __str__(self):
        return "(The movie: {0} was rented {1} days)".format(self.movieTitle, self.nrDays)

class MostRentedMovieDTO(object):
    """
    This class is used for the Most Rented Movies by how many times were rented
    """
    def __init__(self, movieTitle, nrTimeRented ):
        self.__movieTitle = movieTitle
        self.__nrTimeRented = nrTimeRented

    @property
    def movieTitle(self):
        return self.__movieTitle
    
    @movieTitle.setter
    def movieTitle(self, value):
        self.__movieTitle = value
    
    @property
    def nrTimeRented(self):
        return self.__nrTimeRented
    
    @nrTimeRented.setter
    def nrTimeRented(self, value):
        self.__nrTimeRented = value

    def __str__(self):
        return "(The movie: {0} was rented {1} times)".format(self.movieTitle, self.nrTimeRented)

class MostActiveClientsDTO(object):
    """
    This class is used for the most active clients, which rented the most movies
    """
    def __init__(self,clientName,nrDay):
        self.__clientName = clientName
        self.__nrDay = nrDay

    @property
    def clientName(self):
        return self.__clientName

    @clientName.setter
    def clientName(self, value):
        self.__clientName = value

    @property
    def nrDay(self):
        return self.__nrDay

    @nrDay.setter
    def nrDay(self, value):
        self.__nrDay = value

    def __str__(self):
        if self.__nrDay == 0:
            return"(The client: {0} didn't rent a movie)".format(self.__clientName)
        return "(The client: {0}, rented a movie, {1} days)".format(self.__clientName,self.__nrDay)


class AllRentalsDTO(object):
    """
    This class will make an element for a rental
    """
    def __init__(self,rentalId,movieTitle):
        self.__rentalId = rentalId
        self.__movieTitle = movieTitle

    @property
    def rentalId(self):
        return self.__rentalId

    @rentalId.setter
    def rentalId(self, value):
        self.__rentalId = value

    @property
    def movieTitle(self):
        return self.__movieTitle

    @movieTitle.setter
    def movieTitle(self, value):
        self.__movieTitle = value

    def __str__(self):
        return "(The rental {0}, has the movie {1} rented)".format(self.__rentalId,self.__movieTitle)


class LateRentalDTO(object):
    """
    This class will make itmes for the late rental statistics
    """
    def __init__(self,rentalId,nrDay):
        self.__rentalId = rentalId
        self.__nrDay = nrDay

    @property
    def rentalId(self):
        return self.__rentalId

    @rentalId.setter
    def rentalId(self, value):
        self.__rentalId = value

    @property
    def nrDay(self):
        return self.__nrDay

    @nrDay.setter
    def nrDay(self, value):
        self.__nrDay = value

    def __str__(self):
        return "( The rental has the id: {0}, the client delay bringing the movie with {1} days)".\
            format(self.rentalId,self.nrDay)

