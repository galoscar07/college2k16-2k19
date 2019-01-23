from unittest import TestCase
from src.store.domain.entities import Movie
from src.store.repository.repository import Repository,DuplicateIdException,RepositoryException, InvalidIdException
from src.store.domain.validators import MovieValidator

class TestRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__repository = Repository(MovieValidator)

    def test_findById(self):
        movie1 = Movie(1, "Ride along", "Funny", "Comedy")
        self.__repository.save(movie1)
        self.assertEqual(self.__repository.findById(1),movie1)
        self.assertEqual(self.__repository.findById(100),None)

    def test_save(self):
        movie1 = Movie(1,"Ride along","Funny","Comedy")
        self.__repository.save(movie1)
        self.assertEqual(len(self.__repository.getAll()), 1)

        movie2 = Movie(1,"Ratatouille","Rat","Action")
        self.assertRaises(DuplicateIdException, self.__repository.save, movie2)

        movie3 = Movie(1,"Selfie","Romanesc","Comedy")
        self.assertRaises(RepositoryException, self.__repository.save, movie3)

        movie4 = Movie("four","Ride along","Funny","Comedy")
        self.assertRaises(RepositoryException, self.__repository.save,movie4)

    def test_getAll(self):
        movie1 = Movie(1, "Ride along", "Funny", "Comedy")
        movie2 = Movie(2, "Selfie", "Romanesc", "Comedy")
        self.__repository.save(movie1)
        self.__repository.save(movie2)
        self.assertEqual(len(self.__repository.getAll()), 2)

    def test_delete(self):
        movie1 = Movie(1, "Ride along", "Funny", "Comedy")
        movie2 = Movie(2, "Selfie", "Romanesc", "Comedy")
        self.__repository.save(movie1)
        self.__repository.save(movie2)
        self.__repository.delete(1)
        self.assertEqual(len(self.__repository.getAll()),1)
        self.assertRaises(InvalidIdException,self.__repository.delete,4)
