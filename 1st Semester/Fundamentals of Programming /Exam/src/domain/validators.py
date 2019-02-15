class StoreException(Exception):
    pass

class DuplicateSentence(StoreException):
    pass

class SentenceValidatorException(StoreException):
    pass

class RepositoryException(StoreException):
    pass

class SentenceValidator(object):
    @staticmethod
    def validate(sentence):
        cop = sentence.uncensored.split()
        if len(cop) < 1:
            raise SentenceValidatorException("The sentence was not good")
        for i in range(0,len(cop)):
            if len(cop[i]) < 3:
                raise SentenceValidatorException("The sentence was not good")
