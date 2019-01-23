from datetime import date
from unittest import TestCase

from src.controller.clientController import ClientController
from src.controller.movieController import MovieController
from src.controller.rentalController import RentalController
from src.controller.statisticsController import StatisticsController
from src.controller.undoController import UndoController
from src.domain.validators import ClientValidator, DuplicateIdException, RepositoryException, InvalidIdException, \
    MovieValidator, RentalValidatorException, RentalValidator
from src.repository.fileRepository import ClientFileRepository, MovieFileRepository, RentalFileRepository
from src.repository.repository import Repository


class testClientController(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__clientRepository = Repository(ClientValidator)
        self.__clientController = ClientController(self.__clientRepository,self.__undoController)

    def test_addClient(self):
        self.__clientController.addClient(1,"Oscar")
        self.assertEqual(len(self.__clientController.getAll()),1)
        self.assertRaises(DuplicateIdException,self.__clientController.addClient,1,"Oscar")
        self.assertRaises(RepositoryException, self.__clientController.addClient, "nana", "Oscar")
        self.assertRaises(RepositoryException, self.__clientController.addClient, 2, "")

    def test_getAll(self):
        self.__clientController.addClient(1,"Gal Oscar")
        self.assertEqual(len(self.__clientController.getAll()), 1)

    def test_deleteClient(self):
        self.__clientController.addClient(1,"Oscar")
        self.__clientController.deleteClient(1)
        self.assertEqual(len(self.__clientController.getAll()), 0)
        self.assertRaises(InvalidIdException, self.__clientController.deleteClient, 1)

    def test_clientUpdate(self):
        self.__clientController.addClient(1,"Gal")
        self.__clientController.clientUpdate(1,"Oscar")
        self.assertEqual(str(self.__clientRepository.findById(1)),"Client Id: #1, Name: Oscar")
        self.assertRaises(InvalidIdException,self.__clientController.clientUpdate,2,"Nana")

    def test_searchById(self):
        self.__clientController.addClient(1,"Gal Oscar")
        self.__clientRepository.findById(1).entityId = str(self.__clientRepository.findById(1).entityId)
        self.assertEqual(self.__clientController.searchById("1")[0].name,"Gal Oscar")

    def test_searchByName(self):
        self.__clientController.addClient(1,"Gal Oscar")
        self.assertEqual(self.__clientController.searchByName("os")[0].name,"Gal Oscar")


class testMovieController(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__movieRepository = Repository(MovieValidator)
        self.__movieController = MovieController(self.__movieRepository,self.__undoController)

    def test_addMovie(self):
        self.__movieController.addMovie(1,"naa","na","a")
        self.assertEqual(len(self.__movieRepository.getAll()),1)

    def test_getAll(self):
        self.assertEqual(len(self.__movieController.getAll()),0)

    def test_deleteMovie(self):
        self.__movieController.addMovie(1, "naa", "na", "a")
        self.__movieController.deleteMovie(1)
        self.assertEqual(len(self.__movieRepository.getAll()), 0)
        self.assertRaises(InvalidIdException,self.__movieController.deleteMovie,2)


    def test_updateMovie(self):
        self.__movieController.addMovie(1,"a","b","c")
        self.__movieController.updateMovie(1,"A","","")
        self.assertEqual(str(self.__movieRepository.findById(1)),"Movie id: #1, Title: A, Genre: b, Description: c")
        self.__movieController.updateMovie(1,"","B","")
        self.assertEqual(str(self.__movieRepository.findById(1)), "Movie id: #1, Title: A, Genre: B, Description: c")
        self.__movieController.updateMovie(1,"","","C")
        self.assertEqual(str(self.__movieRepository.findById(1)), "Movie id: #1, Title: A, Genre: B, Description: C")
        self.__movieController.updateMovie(1, "a", "b", "")
        self.assertEqual(str(self.__movieRepository.findById(1)), "Movie id: #1, Title: a, Genre: b, Description: C")
        self.__movieController.updateMovie(1, "A", "", "c")
        self.assertEqual(str(self.__movieRepository.findById(1)), "Movie id: #1, Title: A, Genre: b, Description: c")
        self.__movieController.updateMovie(1, "", "B", "C")
        self.assertEqual(str(self.__movieRepository.findById(1)), "Movie id: #1, Title: A, Genre: B, Description: C")
        self.__movieController.updateMovie(1, "a", "b", "c")
        self.assertEqual(str(self.__movieRepository.findById(1)), "Movie id: #1, Title: a, Genre: b, Description: c")
        self.assertRaises(InvalidIdException,self.__movieController.updateMovie,1,"","","")

    def test_searchById(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.__movieRepository.findById(1).entityId = str(self.__movieRepository.findById(1).entityId)
        self.assertEqual(self.__movieController.searchById("1")[0].title,"Ratata")

    def test_searchByTitle(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.assertEqual(self.__movieController.searchByTitle("ra")[0].title,"Ratata")

    def test_searchByDescription(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.assertEqual(self.__movieController.searchByDescription("pok")[0].description,"Pokemon")

    def test_serchByGenre(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.assertEqual(self.__movieController.searchByGenre("anim")[0].genre,"Animation")

class TestRentalController(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__clientRepository = ClientFileRepository(ClientValidator,
                                                "/Users/oscar/Documents/College/Fundamentals of Programming"
                                                "/Eclipse1/MovieRentalFinal/data/clients.pickle")
        self.__clientController = ClientController(self.__clientRepository,self.__undoController)
        self.__movieRepository = MovieFileRepository(MovieValidator,
                                              "/Users/oscar/Documents/College/Fundamentals of Programming"
                                              "/Eclipse1/MovieRentalFinal/data/movie.pickle")
        self.__movieController = MovieController(self.__movieRepository,self.__undoController)
        self.__rentalRepository = Repository(RentalValidator)
        self.__rentalController = RentalController(self.__rentalRepository,self.__clientRepository,
                                                   self.__movieRepository,self.__undoController)


    def test_addRental(self):
        self.__rentalController.addRental(3, 3, date(2016, 12, 12), date(2016, 12, 13), None)
        self.assertRaises(RentalValidatorException,self.__rentalController.addRental, 900,4,date(2016, 12, 12),
                          date(2016, 12, 13),None)
        self.assertRaises(RentalValidatorException,self.__rentalController.addRental, 3, 3, date(2016, 12, 20), date(2016, 12, 23), None)

    def test_addRental2(self):
        self.__rentalController.addRental(1,1,date(2016, 12, 12), date(2016, 12, 13), None)
        self.assertRaises(RentalValidatorException,self.__rentalController.addRental,1,3,date(2016, 12, 12), date(2016, 12, 13), None)


    def test_getAll(self):
        self.__rentalController.addRental(3,3,date(2016, 12, 12), date(2016, 12, 13),None)
        self.assertEqual(len(self.__rentalController.getAll()),1)

    def test_returnMovie(self):
        self.__rentalController.addRental(3, 3, date(2016, 12, 13), date(2016, 12, 22), None)
        self.__rentalController.addRental(2, 4, date(2016, 12, 12), date(2016, 12, 13), date(2016, 12, 13))
        self.__rentalController.returnMovie(0,date(2016, 12, 14))
        self.assertEqual(self.__rentalRepository.findById(0).returnedDate,date(2016, 12, 14))
        self.assertRaises(RentalValidatorException,self.__rentalController.returnMovie,1,date(2016, 12, 13))
        self.assertRaises(RentalValidatorException,self.__rentalController.returnMovie,3,date(2016, 1, 23))


class TestStatisticsController(TestCase):
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__clientRepository = ClientFileRepository(ClientValidator,
                                                       "/Users/oscar/Documents/College/Fundamentals of Programming"
                                                       "/Eclipse1/MovieRentalFinal/data/clients.pickle")
        self.__clientController = ClientController(self.__clientRepository,self.__undoController)
        self.__movieRepository = MovieFileRepository(MovieValidator,
                                                     "/Users/oscar/Documents/College/Fundamentals of Programming"
                                                     "/Eclipse1/MovieRentalFinal/data/movie.pickle")
        self.__movieController = MovieController(self.__movieRepository,self.__undoController)
        self.__rentalRepository = RentalFileRepository(RentalValidator,
                                                "/Users/oscar/Documents/College/Fundamentals of Programming"
                                                "/Eclipse1/MovieRentalFinal/data/rental.pickle")
        self.__rentalController = RentalController(self.__rentalRepository, self.__clientRepository,
                                                   self.__movieRepository,self.__undoController)
        self.__statisticsController = StatisticsController(self.__clientRepository,self.__movieRepository,
                                                           self.__rentalRepository)

    def test_howManyTimesRented(self):
        self.__clientController.addClient(101,"Dada")
        self.__rentalController.addRental(4, 101, date(2016, 12, 12), date(2016, 12, 13), None)
        self.assertEqual(self.__statisticsController.howManyTimesRented(4),2)

    def test_howManyDaysRented(self):
        self.assertEqual(self.__statisticsController.howManyDaysRented(3),400)
        self.assertEqual(self.__statisticsController.howManyDaysRented(2),454)


    def test_howManyDaysClientRented(self):
        self.assertEqual(self.__statisticsController.howManyDaysClientRented(11),425)
        self.assertEqual(self.__statisticsController.howManyDaysClientRented(2), 425)

    def test_topByMostRentedTimes(self):
        self.assertEqual(self.__statisticsController.topByMostRentedTimes()[1].nrTimeRented,2)
    def test_allCurrentlyRented(self):
        self.assertEqual(self.__statisticsController.allCurrentlyRented()[1].rentalId,2)
    def test_lateRentals(self):
        self.assertEqual(self.__statisticsController.lateRentals()[1].nrDay,733)
    def test_topByMostRentedDays(self):
        self.assertEqual(self.__statisticsController.topByMostRentedDays()[1].nrDays,737)
    def test_mostActiveClients(self):
        self.assertEqual(self.__statisticsController.mostActiveClients()[1].nrDay,737)

class TestUndoController(TestCase):
    def setUp(self):
        super().setUp()