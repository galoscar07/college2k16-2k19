'''
Created on Nov 6, 2016

@author: oscar
'''

class Movie(object):
    '''
    This class represent the movies class, each class will have 4 atributes
    '''
    
    def __init__(self, movieId, title, genre, description):
        """
        :param movieId: Is the id of the class Movie, each id will be unique
        :param title: Is a title of a movie
        :param genre: Is the genre of the movie
        :param description: Is the description of a movie
        """
        self.__movieId = movieId
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def entityId(self):
        return self.__movieId

    @entityId.setter
    def entityId(self, value):
        self.__movieId = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    def __str__(self, *args, **kwargs):
        return "Movie id: #{0}, Title: {1}, Genre: {2}, Description: {3}".format(self.entityId, self.title,
                                                                               self.genre, self.description)
    
class Client(object):
    """
    The class represent the client class, which have 2 atributtes
    """
    def __init__(self,clientId,name):
        """

        :param clientId: is a unique variable
        :param name: represent the name of the client
        """
        self.__clientId = clientId
        self.__name = name
        
    @property
    def entityId(self):
        return self.__clientId
    
    @entityId.setter
    def entityId(self,value):
        self.__clientId = value
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
        
    def __str__(self, *args, **kwargs):
        return "Client id: #{0}, Name: {1}".format(self.entityId, self.name)
    
class Rental(object):
    """
    The class represent the rental class, which have 6 atributes
    """
    def __init__(self,rentalId,movieId,clientId,rentDate,dueDate,returnedDate):
        """

        :param rentalId: is the rental id which is unique
        :param movieId: is the id which can be found in the previous class
        :param clientId: is the id which can be found in the previous class
        :param rentDate: is a value under the form dd.mm.yyyy which represent the day in which a movie was rented
        :param dueDate: is a value under the form dd.mm.yyyy ehich represent the day in ehich a movie must be returned
        :param returnedDate: is a value under the form dd.mm.yyyy, which represent the day a movie was returned
        """
        self.__rentalId = rentalId
        self.__movieId = movieId
        self.__clientId = clientId
        self.__rentDate = rentDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate
            
    @property
    def entityId(self):
        return self.__rentalId
    
    @entityId.setter
    def entityId(self,value):
        self.__rentalId = value
    
    @property
    def clientId(self):
        return self.__clientId
    
    @clientId.setter
    def clientId(self,value):
        self.__clientId = value
    
    @property
    def movieId(self):
        return self.__movieId

    @movieId.setter
    def movieId(self, value):
        self.__movieId = value
    
    @property
    def rentDate(self):
        return self.__rentDate

    @rentDate.setter
    def rentDate(self, value):
        self.__rentDate = value
        
    @property
    def dueDate(self):
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, value):
        self.__dueDate = value
        
    @property
    def returnedDate(self):
        return self.__returnedDate

    @returnedDate.setter
    def returnedDate(self, value):
        self.__returnedDate = value

    def __str__(self, *args, **kwargs):
        return "Rental Id: #{0}, Movie Id: {1}, Client Id: {2}, Rented Date: {3}, Due Date:{4}, Returned Date: {5})".format(self.entityId, self.movieId,self.clientId,self.rentDate,self.dueDate,self.returnedDate)
    
    