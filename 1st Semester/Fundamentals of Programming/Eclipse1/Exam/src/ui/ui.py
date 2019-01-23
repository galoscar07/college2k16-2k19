import random

from src.domain.validators import StoreException


class UI(object):
    def __init__(self,sentenceController):
        self.__sentenceController = sentenceController


    @staticmethod
    def printMenu():
        string = "Available Comands \n"
        string += "\t 1. Add a santance into the database \n"
        string += "\t 2. List all sentence \n"
        string += "\t 3. Start the game \n"
        string += "\t 4. Exit the game \n"
        print(string)

    def runMenu(self):
        keepAlive = True
        while keepAlive:
            self.printMenu()
            try:
                command = int(input("Command: "))
                if command == 4:
                    keepAlive = False
                elif command == 1:
                    self.addSentence()
                elif command == 2:
                    self.list()
                elif command == 3:
                    self.startGame()
                else:
                    print("Invalid command: ",command)
            except StoreException as se:
                print(se)
            except Exception as e:
                print("Something went wrong")

    def readCommand(self,cmd):
        cop = cmd.split()


    def addSentence(self):
        uncensored = input("Give a sentence: ")
        self.__sentenceController.addSentence(uncensored)

    def list(self):
        lis = (self.__sentenceController.getAll())
        if len(lis) == 0:
            print("no elements to be printed!")
        else:
            for i in lis:
                print("id:",i.entityId, "uncensored: ",i.uncensored,"censored: ",i.censored ,"\n")

    def startGame(self):
        no = len(self.__sentenceController.getAll())
        id = random.randint(0,no-1)
        hangman = ['','h','ha','han','hang','hangm','hangma','hangman']
        c = 0
        indexHangman = 0
        win = False
        sentence = self.__sentenceController.findById(id)
        string = sentence.censored
        lastValue = sentence.censored
        while indexHangman != 7 and win == False:
            print(string, " - ", hangman[indexHangman])
            letter = input("Give a letter: ")
            string = self.__sentenceController.censoreLetter(letter,string,sentence.uncensored)
            if string == lastValue:
                indexHangman += 1
            for i in string:
                if i == '_':
                    c += 1
            if c == 0:
                win = True
            lastValue = string
            c = 0
        if win == True:
            print("You win")
        else:
            print("You have failed this game")









