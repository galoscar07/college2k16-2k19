from datetime import date
from unittest import TestCase

from src.store.domain.entities import Client, Movie, Rental


class TestClient(TestCase):
    def setUp(self):
        super().setUp()
        self.__client = Client(1,"Gal Oscar")

    def test_id(self):
        self.__client.entityId = 3
        self.assertEqual(self.__client.entityId,3)

    def test_name(self):
        self.__client.name = "mihai"
        self.assertEqual(self.__client.name,"mihai")

    def test_str(self):
        self.assertEqual(str(self.__client),"Client id: #1, Name: Gal Oscar")

class TestMovie(TestCase):
    def setUp(self):
        super().setUp()
        self.__movie = Movie(1,"Spider-Man","Action","spider")

    def test_id(self):
        self.__movie.entityId = 4
        self.assertEqual(self.__movie.entityId,4)

    def test_title(self):
        self.__movie.title = "Yes man"
        self.assertEqual(self.__movie.title,"Yes man")

    def test_genre(self):
        self.__movie.genre = "Comedy"
        self.assertEqual(self.__movie.genre,"Comedy")

    def test_description(self):
        self.__movie.description = "A happy man"
        self.assertEqual(self.__movie.description,"A happy man")

    def test_str(self):
        self.assertEqual(str(self.__movie),"Movie id: #1, Title: Spider-Man, Genre: Action, Description: spider")

class TestRental(TestCase):
    def setUp(self):
        super().setUp()
        self.__rental = Rental(1,1,1,date(2016, 11, 11),date(2016, 11, 12), None)

    def test_id(self):
        self.__rental.entityId = 4
        self.assertEqual(self.__rental.entityId,4)

    def test_movieId(self):
        self.__rental.movieId = 3
        self.assertEqual(self.__rental.movieId,3)

    def test_clientId(self):
        self.__rental.clientId = 3
        self.assertEqual(self.__rental.clientId,3)

    def test_rentDate(self):
        self.__rental.rentDate = date(2011,12,14)
        self.assertEqual(self.__rental.rentDate,date(2011,12,14))

    def test_dueDate(self):
        self.__rental.dueDate = date(2013, 12, 14)
        self.assertEqual(self.__rental.dueDate, date(2013, 12, 14))

    def test_returnedDate(self):
        self.__rental.returnedDate = date(2015, 12, 14)
        self.assertEqual(self.__rental.returnedDate, date(2015, 12, 14))

    def test_str(self):
        self.assertEqual(str(self.__rental),"Rental Id: #1, Movie Id: 1, Client Id: 1, Rented Date: 2016-11-11, Due Date:2016-11-12, Returned Date: None)")
