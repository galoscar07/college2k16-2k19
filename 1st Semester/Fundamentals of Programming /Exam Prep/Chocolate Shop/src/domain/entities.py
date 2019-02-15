class Chocolate(object):
    """
    This class is the object which will have 4 fields: id, name, type, and quatities
    """
    def __init__(self,entityId,name,type,quant):
        self.__entityId = entityId
        self.__name = name
        self.__type = type
        self.__quant = quant

    @property
    def entityId(self):
        return self.__entityId

    @entityId.setter
    def entityId(self, value):
        self.__entityId = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def quant(self):
        return self.__quant

    @quant.setter
    def quant(self, value):
        self.__quant = value

    def __str__(self,*args,**kwargs):
        return "The chocolate {0}, with the type {1}, and quant {2}".format(self.name,self.type,self.quant)