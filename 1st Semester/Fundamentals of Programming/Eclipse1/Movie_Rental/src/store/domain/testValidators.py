from unittest import TestCase
from src.store.domain.entities import Movie, Client, Rental
from src.store.domain.validators import MovieValidatorException,MovieValidator, ClientValidator, \
    ClientValidatorException, RentalValidator, RentalValidatorException


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
