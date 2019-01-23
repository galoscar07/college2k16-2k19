from unittest import TestCase

from src.domain.entities import Chocolate
from src.domain.validators import StoreException, ChocolateValidators, ChocolateValidatorException


class TestChocolate(TestCase):
    def setUp(self):
        super().setUp()
        self.__chocolate = Chocolate(1,"milka","milk",10)

    def testId(self):
        self.__chocolate.entityId = 3
        self.assertEqual(self.__chocolate.entityId,3)

    def testName(self):
        self.__chocolate.name = "haha"
        self.assertEqual(self.__chocolate.name,"haha")

    def testType(self):
        self.__chocolate.type = "nu e amuzant"
        self.assertEqual(self.__chocolate.type,"nu e amuzant")

    def testQuant(self):
        self.__chocolate.quant = 4
        self.assertEqual(self.__chocolate.quant,4)

    def testStr(self):
        self.assertEqual(str(self.__chocolate),"The chocolate milka, with the type milk, and quant 10")

class TestValidator(TestCase):
    def setUp(self):
        super().setUp()
        self.__validator = ChocolateValidators

    def testValidator(self):
        self.assertRaises(ChocolateValidatorException,self.__validator.validator,Chocolate("g","ga","ga",5))
        self.assertRaises(ChocolateValidatorException,self.__validator.validator,Chocolate(5,"S","s",-1))