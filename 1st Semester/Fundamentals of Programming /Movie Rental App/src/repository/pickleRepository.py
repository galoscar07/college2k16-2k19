import pickle
from datetime import date

from src.repository.repository import Repository


class ClientBinaryFileRepo(Repository):
    def __init__(self,validatorclass,path):
        super().__init__(validatorclass)
        self.__path = path
        self.loadFromFile(self.__path)

    def loadFromFile(self,path):
        self._entities = pickle.load(open(path, "rb"))


    def saved(self):
        pickle.dump(self._entities, open(self.__path, "wb"))


class MovieBinaryFileRepo(Repository):
    def __init__(self, validatorclass,path):
        super().__init__(validatorclass)
        self.__path = path
        self.loadFromFile(self.__path)

    def loadFromFile(self, path):
        self._entities = pickle.load(open(path, "rb"))

    def saved(self):
        pickle.dump(self._entities, open(self.__path, "wb"))


class RentalBinaryFileRepo(Repository):
    def __init__(self, validatorclass, path):
        super().__init__(validatorclass)
        self.__path = path
        self.loadFromFile(self.__path)

    def loadFromFile(self, path):
        self._entities = pickle.load(open(path, "rb"))

    def saved(self):
        pickle.dump(self._entities, open(self.__path, "wb"))
