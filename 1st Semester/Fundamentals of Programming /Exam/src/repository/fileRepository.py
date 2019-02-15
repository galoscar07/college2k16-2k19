from src.domain.entities import Sentence
from src.repository.repository import Repository


class SentenceFileRepository(Repository):
    def __init__(self, validatorClass, path):
        """
        The function will initialize the repository
        :param validatorClass: is the validator class of the entity
        :param path: Is the place from where we will read the values which will be put into the controllers
        """
        super().__init__(validatorClass)
        self.__path = path
        self.__loadFromFile(self.__path)

    def __loadFromFile(self,path):
        """
        The function will load from file the
        :param path: is the file from where we will save items
        :return: The function will return the controller of the class whit elements loaded from file
        """
        file = open(path, 'r')
        for line in file:
            if line != "\n":
                line.strip()
                sentenceId = len(super().getAll())
                censored = super().censore(line)
                sentence = Sentence(sentenceId,line,censored)
                super().save(sentence)

    def saved(self,path):
        fi = open(path, 'w')
        li = self.getAll()
        for i in li:
            print(i.uncensored,file=fi)



