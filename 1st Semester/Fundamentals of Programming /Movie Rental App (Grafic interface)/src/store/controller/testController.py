from datetime import date
from unittest import TestCase
from src.store.controller.ClientController import ClientController
from src.store.controller.MovieController import MovieController
from src.store.controller.RentalController import RentalController
from src.store.controller.StatisticsController import StatisticsController

from src.store.controller.UndoRedoController import UndoController
from src.store.domain.validators import ClientValidator, ClientIdNotFound, MovieValidator, \
    MovieValidatorException, RentalValidator, RentalValidatorException
from src.store.repository.repository import Repository


class TestClientController(TestCase):
    def setUp(self):
        super().setUp()
        self.__clientRepository = Repository(ClientValidator)
        self.__undoController = UndoController()
        self.__clientController = ClientController(self.__clientRepository,self.__undoController)

    def test_addClient(self):
        self.__clientController.addClient(1,"Gal Oscar")
        self.assertEqual(len(self.__clientController.getAll()),1)

    def test_deleteClient(self):
        self.__clientController.addClient(1, "Gal Oscar")
        self.assertEqual(len(self.__clientController.getAll()), 1)
        self.__clientController.deleteClient(1)
        self.assertEqual(len(self.__clientController.getAll()),0)

    def test_updateClient(self):
        self.__clientController.addClient(1, "Gal Oscar")
        self.__clientController.updateClient(1,"Oscar")
        self.assertEqual(self.__clientRepository.findById(1).name,"Oscar")
        self.assertRaises(ClientIdNotFound, self.__clientController.updateClient, 109,"Gal Oscar")

    def test_getAll(self):
        self.__clientController.addClient(1,"Gal Oscar")
        op = self.__clientRepository.getAll()
        self.assertEqual(len(op),1)

    def test_startUp(self):
        self.__clientController.startUp()
        self.assertEqual(len(self.__clientRepository.getAll()),100)

    def test_searchById(self):
        self.__clientController.addClient(1,"Gal Oscar")
        self.__clientRepository.findById(1).entityId = str(self.__clientRepository.findById(1).entityId)
        self.assertEqual(self.__clientController.searchById("1")[0].name,"Gal Oscar")

    def test_searchByName(self):
        self.__clientController.addClient(1,"Gal Oscar")
        self.assertEqual(self.__clientController.searchByName("os")[0].name,"Gal Oscar")

class TestMovieController(TestCase):
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__movieRepository = Repository(MovieValidator)
        self.__movieController = MovieController(self.__movieRepository,self.__undoController)

    def test_addMovie(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.assertEqual(len(self.__movieController.getAll()), 1)

    def test_deleteClient(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.assertEqual(len(self.__movieController.getAll()), 1)
        self.__movieController.deleteMovie(1)
        self.assertEqual(len(self.__movieController.getAll()), 0)

    def test_updateClient(self):
        self.__movieController.addMovie(1, "Ratata", "Animation", "Pokemon")
        self.__movieController.updateMovie(1, 1,"NewTitle")
        self.assertEqual(self.__movieRepository.findById(1).title,"NewTitle")
        self.__movieController.updateMovie(1, 2, "NewGenre")
        self.assertEqual(self.__movieRepository.findById(1).genre, "NewGenre")
        self.__movieController.updateMovie(1, 3, "NewDescription")
        self.assertEqual(self.__movieRepository.findById(1).description, "NewDescription")
        self.assertRaises(MovieValidatorException,self.__movieController.updateMovie,3,1,"nop")

    def test_startUp(self):
        self.__movieController.startUp()
        self.assertEqual(len(self.__movieRepository.getAll()),100)

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
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__clientRepository = Repository(ClientValidator)
        self.__clientController = ClientController(self.__clientRepository,self.__undoController)
        self.__clientController.startUp()
        self.__movieRepository = Repository(MovieValidator)
        self.__movieController = MovieController(self.__movieRepository,self.__undoController)
        self.__movieController.startUp()
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

    def test_startUp(self):
        self.__rentalController.startUp()
        self.assertEqual(len(self.__rentalRepository.getAll()),100)

class TestStatisticsController(TestCase):
    def setUp(self):
        super().setUp()
        self.__undoController = UndoController()
        self.__clientRepository = Repository(ClientValidator)
        self.__clientController = ClientController(self.__clientRepository,self.__undoController)
        self.__clientController.startUp()
        self.__movieRepository = Repository(MovieValidator)
        self.__movieController = MovieController(self.__movieRepository,self.__undoController)
        self.__movieController.startUp()
        self.__rentalRepository = Repository(RentalValidator)
        self.__rentalController = RentalController(self.__rentalRepository, self.__clientRepository,
                                                   self.__movieRepository,self.__undoController)
        self.__rentalController.startUp()
        self.__statisticsController = StatisticsController(self.__clientRepository,self.__movieRepository,
                                                           self.__rentalRepository)

    def test_howManyTimesRented(self):
        self.__clientController.addClient(101,"Dada")
        self.__rentalController.addRental(4, 101, date(2016, 12, 12), date(2016, 12, 13), None)
        self.assertEqual(self.__statisticsController.howManyTimesRented(4),2)

    def test_howManyDaysRented(self):
        self.assertEqual(self.__statisticsController.howManyDaysRented(3),395)
        self.assertEqual(self.__statisticsController.howManyDaysRented(2),449)


    def test_howManyDaysClientRented(self):
        self.assertEqual(self.__statisticsController.howManyDaysClientRented(11),420)
        self.assertEqual(self.__statisticsController.howManyDaysClientRented(2), 420)

    def test_topByMostRentedTimes(self):
        self.assertEqual(self.__statisticsController.topByMostRentedTimes()[1].nrTimeRented,2)
    def test_allCurrentlyRented(self):
        self.assertEqual(self.__statisticsController.allCurrentlyRented()[1].rentalId,2)
    def test_lateRentals(self):
        self.assertEqual(self.__statisticsController.lateRentals()[1].nrDay,728)
    def test_topByMostRentedDays(self):
        self.assertEqual(self.__statisticsController.topByMostRentedDays()[1].nrDays,732)
    def test_mostActiveClients(self):
        self.assertEqual(self.__statisticsController.mostActiveClients()[1].nrDay,732)

def TestUndoController(TestCase):
    pass

def TestRedoController(TestCase):
    pass
