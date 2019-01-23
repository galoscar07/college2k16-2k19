from datetime import date
from unittest import TestCase

from src.domain.dto import MostRentedMovieDaysDTO, MostRentedMovieDTO, MostActiveClientsDTO, AllRentalsDTO, \
    LateRentalDTO
from src.domain.entities import Client, Movie, Rental
from src.domain.validators import MovieValidator, ClientValidator, ClientValidatorException, RentalValidator, \
    RentalValidatorException
from src.domain.validators import MovieValidatorException


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
        self.assertEqual(str(self.__client),"Client Id: #1, Name: Gal Oscar")

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



class TestValidatorsMovie(TestCase):
    def setUp(self):
        super().setUp()
        self.__validators = MovieValidator

    def test_validate(self):
        self.assertRaises(MovieValidatorException, self.__validators.validate, Movie("a", "Ride", "Funny", "Comedy"))
        self.assertRaises(MovieValidatorException, self.__validators.validate, Movie(1, "", "a", "a"))
        self.assertRaises(MovieValidatorException, self.__validators.validate, Movie(2, "a", "", "a"))
        self.assertRaises(MovieValidatorException, self.__validators.validate, Movie(3, "a", "a", ""))



class TestValidatorClient(TestCase):
    def setUp(self):
        super().setUp()
        self.__validators = ClientValidator

    def test_validate(self):
        self.assertRaises(ClientValidatorException, self.__validators.validate, Client("a", "Gal Oscar"))
        self.assertRaises(ClientValidatorException, self.__validators.validate, Client(1, ""))


class TestValidatorRental(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__validators = RentalValidator

    def test_validate(self):
        self.assertRaises(RentalValidatorException, self.__validators.validate,
                          Rental(1, 1, 1, "01.12.2016", "01.02.2016", None))
        self.assertRaises(RentalValidatorException, self.__validators.validate,
                          Rental("a", 1, 1, "01.12.2016", "01.02.2016", None))
        self.assertRaises(RentalValidatorException, self.__validators.validate,
                          Rental(1, "a", 1, "01.12.2016", "01.02.2016", None))
        self.assertRaises(RentalValidatorException, self.__validators.validate,
                          Rental(1, 1, "a", "01.12.2016", "01.02.2016", None))
        self.assertRaises(RentalValidatorException, self.__validators.validate,
                          Rental(1, 1, 1, "01.12.2015", "01.02.2017", None))
        self.assertRaises(RentalValidatorException, self.__validators.validate,
                          Rental(1, 1, 1, "1.02.2016", "01.02.2016", None))

class TestMostRentedMovieDaysDTO(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__something = MostRentedMovieDaysDTO("Hulk",5)

    def test_movieTitle(self):
        self.__something.movieTitle = "Haha"
        self.assertEqual(self.__something.movieTitle,"Haha")

    def test_nrDays(self):
        self.__something.nrDays = 10
        self.assertEqual(self.__something.nrDays,10)

    def test_str(self):
        self.assertEqual(str(self.__something),"(The movie: Hulk was rented 5 days)")

class TestMostRentedMovieDTO(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__something = MostRentedMovieDTO("Hulk",5)

    def test_movieTitle(self):
        self.__something.movieTitle = "Haha"
        self.assertEqual(self.__something.movieTitle,"Haha")

    def test_nrTimesRented(self):
        self.__something.nrTimeRented = 10
        self.assertEqual(self.__something.nrTimeRented,10)

    def test_str(self):
        self.assertEqual(str(self.__something),"(The movie: Hulk was rented 5 times)")

class TestMostActiveClientsDTO(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__something = MostActiveClientsDTO("Oscar",5)

    def test_clientName(self):
        self.__something.clientName = "Haha"
        self.assertEqual(self.__something.clientName,"Haha")

    def test_nrDay(self):
        self.__something.nrDay = 10
        self.assertEqual(self.__something.nrDay,10)

    def test_str(self):
        self.assertEqual(str(self.__something),"(The client: Oscar, rented a movie, 5 days)")
        self.__something.nrDay = 0
        self.assertEqual(str(self.__something),"(The client: Oscar didn't rent a movie)")

class TestAllRentalsDTO(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__something = AllRentalsDTO(1,"Hulk")

    def test_rentalId(self):
        self.__something.rentalId = 4
        self.assertEqual(self.__something.rentalId,4)

    def test_movieTitle(self):
        self.__something.movieTitle = "Haha"
        self.assertEqual(self.__something.movieTitle,"Haha")

    def test_str(self):
        self.assertEqual(str(self.__something),"(The rental 1, has the movie Hulk rented)")

class TestLateRentalDTO(TestCase):
    """

    """
    def setUp(self):
        super().setUp()
        self.__something = LateRentalDTO(1,5)

    def test_rentalId(self):
        self.__something.rentalId = 4
        self.assertEqual(self.__something.rentalId,4)

    def test_nrDay(self):
        self.__something.nrDay = 1
        self.assertEqual(self.__something.nrDay,1)

    def test_str(self):
        self.assertEqual(str(self.__something),"( The rental has the id: 1, the client delay bringing the movie with 5 days)")

