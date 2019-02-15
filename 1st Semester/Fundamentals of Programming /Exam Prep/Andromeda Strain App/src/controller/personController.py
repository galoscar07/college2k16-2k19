from src.entities.entities import Person
from src.entities.validators import PersonException


class Controller(object):
    """
    This is the controller of the persons
    """
    def __init__(self,personRepository):
        """
        This is the initialization function of the controller
        :param personRepository: is the repository
        """
        self.__personRepository = personRepository

    def getAll(self):
        """
        the function will take the list of dictionaries
        :return: a list of dictionaries
        """
        return self.__personRepository.getAll()

    def addPerson(self,entityId,imunization,status):
        """
        The function will add a person into the program
        :param entityId: is the unique id of the person
        :param imunization: is the type of a person (vaccinated or non vaccinated)
        :param status: is the status is a person is vaccinated or not
        :return: the list modified with the new element in it
        """
        person = Person(entityId,imunization,status)
        self.__personRepository.save(person)

    def vaccinate(self,entityId):
        """
        The function will change a parameter in the list
        :param entityId: is the unique id of a person
        :return: the list modified
        """
        person = self.__personRepository.findById(entityId)
        if not( person.status == "ill") :
            person.imunization = "vaccinated"
        else:
            raise PersonException("The person can't be vaccinated")
