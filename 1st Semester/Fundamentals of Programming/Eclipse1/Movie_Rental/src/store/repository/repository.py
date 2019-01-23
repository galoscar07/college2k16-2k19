'''
Created on Nov 7, 2016

@author: oscar
'''
from src.store.domain.validators import StoreException, InvalidIdException, RepositoryException, DuplicateIdException

class Repository(object):
    """
    This class is a class that suits all the controller classes.
    """

    def __init__(self, validatorClass):
        """
        This function will set up the class
        :param validatorClass: is the validator class the the controller that enter
        """
        self.__validatorClass = validatorClass
        self.__entities = {}

    def findById(self, entityId):
        """
        This function will search for the entity id in the class dictionary
        :return: None is the entityId was not found and will return the class in the case we found it
        """
        if entityId in self.__entities:
            return self.__entities[entityId]
        return None

    def save(self, entity):
        """
        The function will save an element in the list
        :param entity: can be any class from the controller
        :return: the list with a new element in it
        """
        if not self.findById(entity.entityId) is None:
            raise DuplicateIdException("Duplicate id {0}.".format(entity.entityId))
        try:
            self.__validatorClass.validate(entity)
        except StoreException as mve:
            raise RepositoryException(mve)
        self.__entities[entity.entityId] = entity

    def getAll(self):
        """
        The function will return a list with all the element in the class
        """
        return self.__entities.values()

    def delete(self,entityId):
        """
        The function will delete the element with entityId
        """
        if self.findById(entityId) is None:
            raise InvalidIdException("Invalid id {0}.".format(entityId))
        del(self.__entities[entityId])


