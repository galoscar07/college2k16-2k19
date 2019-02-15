class Person(object):
    """

    """
    def __init__(self,entityId,imunization,status):
        """
        This is the person entity
        :param entityId: this is the id which is unique
        :param imunization: is a status of a person (vaccinated or nonvaccinated)
        :param status: this is amother status of a person(healthy or ill)
        """
        self.__entityId = entityId
        self.__imunization = imunization
        self.__status = status

    @property
    def entityId(self):
        return self.__entityId

    @entityId.setter
    def entityId(self, value):
        self.__entityId = value

    @property
    def imunization(self):
        return self.__imunization

    @imunization.setter
    def imunization(self, value):
        self.__imunization = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def __str__(self, *args, **kwargs):
        return "Id: #{0}, Imunization Status {1}, Status {2}".format(self.__entityId,self.__imunization,self.__status)