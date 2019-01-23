from unittest import TestCase

from src.controller.sentenceController import SentenceController
from src.domain.validators import SentenceValidator
from src.repository.fileRepository import SentenceFileRepository


class testSentenceController(TestCase):
    def setUp(self):
        super().setUp()
        self.__sentenceRepository = SentenceFileRepository(SentenceValidator, "/Users/oscar/Documents/College/Fundamentals of"
                                                                       " Programming/Eclipse1/Exam/data/sentence.txt")
        self.__sentenceController = SentenceController(self.__sentenceRepository)

    def testAdd(self):
        li = len(self.__sentenceController.getAll())
        self.__sentenceController.addSentence("ana are mere")
        self.assertEqual(li+1,len(self.__sentenceController.getAll()))

    def testFindById(self):
        no = self.__sentenceController.findById(1)
        self.assertEqual(no.uncensored,"patricia has pears\n")

    def testCensorLetter(self):
        s = self.__sentenceController.censoreLetter("n","a___a","annha")
        self.assertEqual(s,"ann_a")