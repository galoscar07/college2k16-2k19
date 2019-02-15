class Sentence():

    def __init__(self,entityId,uncensored,censored):
        self.__entityId = entityId
        self.__uncensored = uncensored
        self.__censored = censored
        
    @property
    def entityId(self):
        return self.__entityId
    
    @entityId.setter
    def entityId(self, value):
        self.__entityId = value
        
    @property
    def uncensored(self):
        return self.__uncensored
    
    @uncensored.setter
    def uncensored(self, value):
        self.__uncensored = value
        
    @property
    def censored(self):
        return self.__censored
    
    @censored.setter
    def censored(self, value):
        self.__censored = value
        
    