from src.controller.sentenceController import SentenceController
from src.domain.validators import SentenceValidator
from src.repository.fileRepository import SentenceFileRepository
from src.repository.repository import Repository
from src.ui.ui import UI

if __name__ == '__main__':
    print("Hello world")

    sentenceRepository = SentenceFileRepository(SentenceValidator,"/Users/oscar/Documents/College/Fundamentals of"
                                                                  " Programming/Eclipse1/Exam/data/sentence.txt")
    sentenceController = SentenceController(sentenceRepository)

    ui = UI(sentenceController)
    ui.runMenu()

    sentenceRepository.saved("/Users/oscar/Documents/College/Fundamentals of"
                                                                  " Programming/Eclipse1/Exam/data/sentence.txt")
    print("Bye Bye")
    pass
