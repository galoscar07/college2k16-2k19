from src.entities.entities import Person
from src.entities.validators import PersonException


class Repository(object):
    """
    This is the repository
    """
    def __init__(self,personValidator,path):
        self.__personValidator = personValidator
        self.__entities = {}
        self.__path = path
        self.__loadFromFile(self.__path)

    def __loadFromFile(self,path):
        """

        :param path:
        :return:
        """
        file = open(path, "r")
        for line in file:
            data = line.split(",")
            id = int(data[0])
            imunization = data[1]
            status = data[2]
            person = Person(id,imunization,status)
            self.saveFile(person)

    def findById(self,entityId):
        """

        :return:
        """
        if entityId in self.__entities:
            return self.__entities[entityId]
        return None

    def saveFile(self,entity):
        self.__entities[entity.entityId] = entity

    def save(self,entity):
        """

        :param entity:
        :return:
        """
        if not self.findById(entity.entityId) is None:
            raise PersonException("The id is already in")
        else:
            try:
                self.__personValidator.validator(entity)
            except:
                raise PersonException("Invalid Input")
        self.__entities[entity.entityId] = entity

    def getAll(self):
        return self.__entities.values()


