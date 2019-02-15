class ChocolateController(object):
    def __init__(self,chocolateRepository):
        self.__chocolateRepository = chocolateRepository

    def getAll(self):
        return self.__chocolateRepository.getAll()