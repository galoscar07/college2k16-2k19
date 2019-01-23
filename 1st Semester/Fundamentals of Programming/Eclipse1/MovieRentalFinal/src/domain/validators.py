class StoreException(Exception):
    """
    This is the class that store all exceptions :D
    """
    pass

class MovieValidatorException(StoreException):
    """
    This excption will be used for movie exceptions
    """
    pass

class MovieValidator(object):
    """
    This class will validate the movie data input
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
    This exception will be used for client exceptions
    """
    pass

class ClientValidator(object):
    """
    This class is a validator and will validate the client input data
    """
    @staticmethod
    def validate(client):
        if not type(client.entityId) is int :
            raise ClientValidatorException("Client id must be an integer")
        if client.name == "":
            raise ClientValidatorException("You must give a name")



class RentalValidatorException(StoreException):
    """
    This exception will be used for rental exceptions
    """
    pass

class RentalValidator(object):
    """
    This class is th rental validator, and will validate the input data for the rental variables
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

class UndoException(StoreException):
    """
    This exception is used when you don't have anything to undo
    """
    pass

class RedoException(StoreException):
    """
    This class will handel the redo exceptions
    """
    pass