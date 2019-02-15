from src.domain.entities import Sentence


class SentenceController(object):
    def __init__(self, sentenceRepository):
        """
        this function does the initialization for the controller
        :param sentenceRepository: is the repository of the entity sentence
        """
        self.__sentenceRepository = sentenceRepository

    def addSentence(self,uncensored):
        """
        This function will add a new sentence into the database
        :param uncensored: is a sentence to be saved
        :return: the function will return the list modified
        """
        sentenceId = len(self.__sentenceRepository.getAll())
        censored = self.censore(uncensored)
        sentence = Sentence(sentenceId,uncensored,censored)
        self.__sentenceRepository.save(sentence)

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

    def censoreLetter(self,letter,censored,uncensored):
        """
        This function is only going to uncensure a letter if it need to be uncensure
        :param letter: if the letter that we are looking for
        :param censored: is the word with letters covered
        :param uncensored: is the word with letters uncovered
        :return: The function will return a string modified
        """
        string2 = ''
        for i in range(0,len(censored)):
            if censored[i] == '_':
                if uncensored[i] == letter:
                    string2 += letter
                else:
                    string2 += '_'
            else:
                string2 += censored[i]
        return string2


    def getAll(self):
        """
        :return: The function will return the list of entities
        """
        return self.__sentenceRepository.getAll()

    def findById(self,entityId):
        """
        The function will search into the dictionary list for the entity that has as the id the value of entityId
        :param entityId: is the value that we are searching for
        :return: the function will return the position on the entity in the dictionary list and if the element is not in
        the dictionary it will return the value None
        """
        return self.__sentenceRepository.findById(entityId)



