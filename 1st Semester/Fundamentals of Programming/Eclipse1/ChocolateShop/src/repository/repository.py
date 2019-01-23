from src.domain.entities import Chocolate


class Repository(object):
    """

    """
    def __init__(self,validator,path):
        self.__validator = validator
        self.__entities = {}
        self.__path = path
        self.__loadFromFile(self.__path)

    def __loadFromFile(self,path):
        file = open(path, "r")
        c = 1
        for line in file:
            data = line.split(",")
            chocolate = Chocolate(c,data[0],data[1],int(data[2]))
            c = c+1
            self.save(chocolate)

    def getAll(self):
        return self.__entities.values()

    def findById(self,entityId):
        if entityId in self.__entities:
            raise Exception
        return None

    def save(self,entity):
        if not self.findById(entity.entityId) is None:
            raise Exception("Dublicate Id")
        try:
            self.__validator.validator(entity)
        except EnvironmentError:
            print("a")
        self.__entities[entity.entityId] = entity