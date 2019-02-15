from unittest import TestCase

from src.entities.entities import Person
from src.entities.validators import PersonValidatorException, PersonException


class TestEntities(TestCase):
    def setUp(self):
        super().setUp()
        self.__person = Person(1,"nonvaccinated","healthy")

    def testId(self):
        self.__person.entityId = 3
        self.assertEqual(self.__person.entityId,3)

    def testImmunization(self):
        self.__person.imunization = "vaccinated"
        self.assertEqual(self.__person.imunization,"vaccinated")

    def testStatus(self):
        self.__person.status = "ill"
        self.assertEqual(self.__person.status,"ill")

    def testStr(self):
        self.assertEqual(str(self.__person),"Id: #1, Imunization Status nonvaccinated, Status healthy")

class TestValidators(TestCase):
    def setUp(self):
        super().setUp()
        self.__validator = PersonValidatorException
        self.__person = Person(1,"vaccinated","ill")
    def testvalidator(self):
        self.assertRaises(PersonException,self.__validator.validator,Person(1,"vaccinated","ill"))
        self.assertRaises(PersonException,self.__validator.validator,Person(1,"nonvaccinated","ill"))