from datetime import date

from src.controller.undoController import FunctionCall, Operation
from src.domain.entities import Rental
from src.domain.validators import RentalValidatorException


class RentalController(object):
    """
    The class is the controller for the rentals in the app
    """
    def __init__(self, rentalRepository, clientRepository, movieRepository,undoController):
        """
        The function is only to set up
        :param rentalRepository: a class, in which are it is a set of operations visible for all controllers
        :param clientRepository: a class, in which are it is a set of operations visible for all controllers
        :param movieRepository: a class, in which are it is a set of operations visible for all controllers
        """
        self.__rentalRepository = rentalRepository
        self.__clientRepository = clientRepository
        self.__movieRepository = movieRepository
        self.__undoController = undoController

    def getAll(self):
        """
        This function will return a list of elements from the controller
        """
        return self.__rentalRepository.getAll()

    def addRental(self, movieId,clientId,rentedDate,dueDate,returnedDate):
        """
        The function will save the entity rental into the rental repository
        :param movieId: is the id of the movie that was rented
        :param clientId: is the id of the client that rented a movie
        :param rentedDate: is the date when the movie was rented
        :param dueDate: is the day in which the client should return the movie
        :param returnedDate: is the date in which the movie is returned
        :return: the function will return the list modified
        :exception: RentalValidatorException: will be raised when the client or the movies cannot be found
                    RentalValidatorException: will be raised when the client have a movie that is already rented and not
                                              returned to the store
                    RentalValidatorException: will be raised when the movie is already rented
        """
        self.__undoController.newOperation()
        if self.__movieRepository.findById(movieId) is None or self.__clientRepository.findById(clientId)is None:
            raise RentalValidatorException("Movie or client not found.")
        for i in self.__rentalRepository.getAll():
            if i.clientId == clientId:
                if i.returnedDate is None:
                    raise RentalValidatorException("First the client needs to return the movie already rented.")
        for i in self.__rentalRepository.getAll():
            if i.movieId == movieId:
                if i.returnedDate == None:
                    raise RentalValidatorException("Movie is rented ")
        rentalId = len(self.__rentalRepository.getAll())
        rental = Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        self.__rentalRepository.save(rental)
        redo = FunctionCall(self.addRentalForUndo, rental)
        undo = FunctionCall(self.deleteRental,rental.entityId)
        operation = Operation(redo,undo)
        self.__undoController.recordOperation(operation)

    def returnMovie(self,rentalId,returnedDate):
        """
        The function will change the returnedDate field on one element in the repository
        :param rentalId: is the Id of the element that should be changed
        :param returnedDate: is the field of the element that should be changed
        :return: The list with an element modified
        :exception: RentalValidatorException: will be raised if the movie is already returned
                    RentalValidatorException: will be raised if the rental id cannot be found
        """
        self.__undoController.newOperation()
        op = self.__rentalRepository.findById(rentalId)
        if op != None:
            if op.returnedDate == None:
                redo = FunctionCall(self.returnMovie,rentalId,returnedDate)
                undo = FunctionCall(self.returnMovieForUndo,rentalId)
                operation = Operation(redo, undo)
                op.returnedDate = returnedDate
                self.__undoController.recordOperation(operation)
            else:
                raise RentalValidatorException("The movie has already returned")
        else:
            raise RentalValidatorException("Rent Id not found")

    def deleteRental(self,rentalId):
        """
        This function will be used only for undo, and the function will delete an element from the rental repository
        :param rentalId: is the id of the element that is going to be deleted
        :return: The list modified
        """
        self.__rentalRepository.delete(rentalId)

    def addRentalForUndo(self,entity):
        """
        This function is also for undo only, and this function will add a rental but without asking for conditions
        :param enitity: is the entity that will be saved into the rental repository
        :return: the function will return the list modofied
        """
        self.__rentalRepository.save(entity)

    def returnMovieForUndo(self,rentalId):
        """
        The function is also for undo only, and this function will make the returnedDate field of the rental entity None
        :param rentalId: is the id of the element that will be changed
        :return: the function will return the list modified
        """
        op = self.__rentalRepository.findById(rentalId)
        op.returnedDate = None

    def startUp(self):
        """
        The function will give 100 elements into the controller for start up
        :return: the list with 100 elements in it
        """
        self.addRental(1, 1, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(2, 15, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(2, 2, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(3, 3, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(4, 4, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(5, 5, date(2016, 7, 22), date(2016, 7, 25), date(2016,7,25))
        self.addRental(6, 6, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(7, 7, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(8, 8, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(9, 9, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(19, 10, date(2015, 10, 2), date(2015, 10, 6), None)
        self.addRental(10, 15, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(11, 11, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(12, 12, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(13, 13, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(14, 14, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(15, 15, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(16, 16, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(17, 17, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(18, 18, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(29, 19, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(20, 20, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(21, 21, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(22, 22, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(23, 4, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(24, 18, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(25, 9, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(26, 16, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(27, 13, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(28, 4, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(50, 30, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(30, 20, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(31, 20, date(2015, 11, 10), date(2015, 11, 15), date(2016,11,15))
        self.addRental(32, 16, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(33, 4, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(34, 5, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(35, 4, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(36, 7, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(37, 20, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(38, 40, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(39, 41, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(40, 42, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(41, 43, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(42, 44, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(43, 46, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(44, 48, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(45, 49, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(46, 51, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(47, 52, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(48, 55, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(49, 56, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(46, 57, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(53, 58, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(54, 59, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(55, 60, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(56, 61, date(2016, 7, 22), date(2016, 7, 25), date(2016, 7, 25))
        self.addRental(57, 62, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(58, 63, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(59, 64, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(60, 65, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(61, 66, date(2015, 10, 2), date(2015, 10, 6), None)
        self.addRental(62, 67, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(63, 68, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(64, 69, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(65, 70, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(66, 72, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(67, 73, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(68, 74, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(69, 75, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(70, 76, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(71, 77, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(72, 78, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(73, 79, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(74, 80, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(75, 81, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(77, 82, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(78, 83, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(79, 84, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(80, 85, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(81, 86, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(82, 87, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(83, 88, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(84, 89, date(2015, 11, 10), date(2015, 11, 15), date(2016, 11, 15))
        self.addRental(85, 90, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(86, 91, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(87, 92, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(88, 93, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(89, 94, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(90, 95, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(91, 96, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
        self.addRental(92, 97, date(2015, 1, 2), date(2015, 1, 6), None)
        self.addRental(93, 98, date(2015, 2, 7), date(2015, 3, 9), date(2015, 3, 8))
        self.addRental(94, 99, date(2015, 11, 10), date(2015, 11, 15), None)
        self.addRental(95, 100, date(2015, 12, 5), date(2015, 12, 7), None)
        self.addRental(96, 46, date(2016, 5, 20), date(2016, 5, 27), date(2016, 5, 25))
        self.addRental(97, 98, date(2016, 7, 22), date(2016, 7, 25), None)
        self.addRental(98, 94, date(2016, 8, 29), date(2016, 8, 30), None)
        self.addRental(99, 51, date(2016, 3, 10), date(2016, 3, 15), date(2016, 3, 14))
        self.addRental(100, 65, date(2016, 7, 15), date(2016, 7, 19), None)
        self.addRental(48, 55, date(2016, 2, 4), date(2016, 2, 8), date(2016, 2, 7))
