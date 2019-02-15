'''
Created on Nov 13, 2016

@author: oscar
'''
from datetime import date


class StoreException(Exception):
    """
    This is the class in which we will store all the exceptions
    """
    pass

class MovieValidatorException(StoreException):
    """
    The class is an exception for the movie class which is an extension of StoreException
    """
    pass

class MovieValidator(object):
    """
    The class has an validator which will validate the values which will be introduced into the class movie
    """
    @staticmethod
    def validate(movie):
        if not type(movie.entityId) is int:
            raise MovieValidatorException("Movie id must be an integer")
        if movie.description == "":
            raise MovieValidatorException("You must give a description")
        if movie.genre == "":
            raise MovieValidatorException("You must give a genre")
        if movie.title == "":
            raise MovieValidatorException("You must give a title")

class ClientValidatorException(StoreException):
    """
    The class is an exception for the clients class which is an extension of StoreException
    """
    pass

class ClientValidator(object):
    """
    The class has an validator which will validate the values which will be introduced into the class clients
    """
    @staticmethod
    def validate(client):
        if not type(client.entityId) is int :
            raise ClientValidatorException("Client id must be an integer")
        if client.name == "":
            raise ClientValidatorException("You must give a name")



class RentalValidatorException(StoreException):
    """
    The class is an exception for the clients class which is an extension of StoreException
    """
    pass

class RentalValidator(object):
    """
    The class has an validator which will validate the values which will be introduced into the class rental
    """
    @staticmethod
    def validate(rental):
        if not type(rental.entityId) is int:
            raise RentalValidatorException("Rental id must be a integer")
        if not type(rental.movieId) is int:
            raise RentalValidatorException("Movie id must be an integer")
        if not type(rental.clientId) is int:
            raise RentalValidatorException("Client id must be an integer")
        if rental.dueDate < rental.rentDate:
            raise RentalValidatorException("Due date can't be befor rent date")


class RepositoryException(StoreException):
    """
    The class stores exception for repository class
    """
    pass

class DuplicateIdException(RepositoryException):
    """
    This class is an exception for duplicated id
    """
    pass

class InvalidIdException(RepositoryException):
    """
    This Class is an exception for invalid id (id - string, etc)
    """
    pass

class ClientIdNotFound(StoreException):
    """
    This class is an exception when we search a client and we can not found it.
    """
    pass

class UndoExcept(StoreException):
    """
    This class is an exception for undo
    """
    pass

class RedoExcept(StoreException):
    """
    This class is an exception for redo
    """
    pass
        