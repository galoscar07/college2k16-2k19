from src.domain.entities import Client, Movie, Rental
from src.domain.validators import DuplicateIdException, StoreException, RepositoryException, InvalidIdException


class Repository(object):
    """
    This class is the class representing the repository for all the controllers
    """
    def __init__(self,validatorClass):
        """
        This function is initializing the repository which is a class of object, and each object has a different
        validator
        :param validatorClass: Is the validator class of the object that has a repository
        """
        self.__validatorClass = validatorClass
        self._entities = {}

    def findById(self,entityId):
        """
        The function will search into the dictionary list for the entity that has as the id the value of entityId
        :param entityId: is the value that we are searching for
        :return: the function will return the position on the entity in the dictionary list and if the element is not in
        the dictionary it will return the value None
        """
        if entityId in self._entities:
            return self._entities[entityId]
        return None

    def save(self,entity):
        """
        The function save the object into the dictionary list
        :param entity: is the object that is going to be saved
        :return: The function will return the list modified
        Exceptons: DuplicateIdException will be raised is the entity id which is supposed to be unique is already in the
               dictionary.
                   StoreException will be raised is thir is something wrong with the entity which is checked by the
               validator class
        """
        if not self.findById(entity.entityId) is None:
            raise DuplicateIdException("Duplicate id {0}".format(entity.entityId))
        try:
            self.__validatorClass.validate(entity)
        except StoreException as st:
            raise RepositoryException(st)
        self._entities[entity.entityId] = entity

    def getAll(self):
        """
        :return: The function will return the list of entities
        """
        return self._entities.values()

    def delete(self,entityId):
        """
        The function will delete the element which have as id the value of entityId
        :param entityId: if the variable after which we will search the element which needs to be deleted
        :return: The list modified or not, depends if the element was found or not
        Exceptions: InvalidIdException: will be raised if the element cannot be found in the list
        """
        if self.findById(entityId) is None:
            raise InvalidIdException("Invalid id {0}.".format(entityId))
        del(self._entities[entityId])

    def update(self,entity):
        """
        The function will update the element in the repository
        :param entity: is the element which will be pun into the list
        :return: The list with one element modified
        Exceptions: InvalidIdException will be raised if the elements has the id None
                    InvalidIdException will also be raised if the element is not into the list
        """
        if entity.entityId is None:
            raise InvalidIdException("Something went wrong ...")
        if self.findById(entity.entityId) is None:
            raise InvalidIdException("Invalid id {0}".format(entity.entityId))
        self._entities[entity.entityId] = entity

    def addClient(self, clientId,name):
        """
        The function will add clients into the controller
        :param clientId: is the key which will help us to save into the dictionary
        :param name: is the value fro the key clientId
        :return: The function will return the list of clients with a new client in it
        """
        client = Client(clientId,name)
        self.save(client)

    def addMovie(self, movieId,title,genre,description):
        """
        The function add a movie into a controller
        :param movieId: is the key to the dictionary
        :param title: is a field of the movie
        :param genre: is another field of the movie
        :param description: another field of the movie
        :return: The function will return the list with the new movie in it
        """
        movie = Movie(movieId,title,genre,description)
        self.save(movie)

    def addRental(self, movieId,clientId,rentedDate,dueDate,returnedDate):
        """
        The function will add a new rental into the list.
        :var: All those variables are for a new rental.
        :except if the movieId, or clientId does not exist and some other exceptions
        """
        rentalId = len(self.getAll())
        rental = Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        self.save(rental)