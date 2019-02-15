from src.domain.validators import DuplicateSentence, StoreException, RepositoryException


class Repository(object):
    def __init__(self, ValidatorClass):
        self.__validatorClass = ValidatorClass
        self._entities = {}

    def findByUncensored(self,uncensored):
        """
        The function will search into the dictionary list for the entity that has as the sentence value same as uncesored
        :param uncensored is a string with no _ in it
        :return: the function will return the position on the entity in the dictionary list and if the element is not in
        the dictionary it will return the value None
        """
        for i in self._entities:
            if uncensored in self._entities[i].uncensored and len(uncensored) == len(self._entities[i].uncensored)+1:
                return True
        return None

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
        Exceptons: Duplicatesentence will be raised is the entity id which is supposed to be unique is already in the
               dictionary.
                   StoreException will be raised is thir is something wrong with the entity which is checked by the
               validator class
        """
        if not self.findByUncensored(entity.uncensored) is None:
            raise DuplicateSentence("The sentence is already in the game")
        try:
            self.__validatorClass.validate(entity)
        except StoreException as se:
            raise RepositoryException(se)
        self._entities[entity.entityId] = entity

    def getAll(self):
        """
        :return: The function will return the list of entities
        """
        return self._entities.values()

    def censore(self,uncensored):
        """
        This function censore a sentence, by the rule of hangman, the first and the last letters remain the same, and all
        their aparition will be also releved
        :param uncensored: Is the sentence that need to be censored
        :return: the function will return a string, in which the first and the last letter of each word will be uncovered
                and all their aparition in the string
        """
        cop = uncensored.split()
        string = ''
        lis = []
        for i in range(0,len(cop)):
            a = cop[i][0]
            b = cop[i][len(cop[i])-1]
            lis.append(a)
            lis.append(b)
        for i in range(0,len(cop)):
            for j in range(0,len(cop[i])):
                if cop[i][j] in lis:
                    string += cop[i][j]
                else:
                    string += '_'
            string += ' '
        return string




