from time import time

from src.Controller import Controller
from src.Problem import Problem


class UI:

    def __init__(self):
        self.__p = Problem("/Users/oscar/Documents/College/4th Semester/Artificial Intelligence/Laboratory/lab1/src/inputReallySmall")
        self.__contr = Controller(self.__p)

    def printMainMenu(self):
        s = ''
        s += "0 - exit \n"
        s += "1 - Print what is loaded \n"
        s += "2 - find a path with BFS \n"
        s += "3 - find a path with BestFS \n"
        print(s)

    def findPathBFS(self):
        startClock = time()
        print(str(self.__contr.BFS(self.__p.getRoot())))
        print('execution time = ', time() - startClock, " seconds")

    def findPathBestFS(self):
        startClock = time()
        print(str(self.__contr.BestFS(self.__p.getRoot())))
        print('execution time = ', time() - startClock, " seconds")

    def printLoaded(self):
        print("Initial")
        print(str(self.__contr.returnInitial()))
        print("\n Final")
        print(str(self.__contr.returnFinal()))

    def run(self):
        runM = True
        self.printMainMenu()
        while runM:
            try:
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 1:
                    self.printLoaded()
                elif command == 2:
                    self.findPathBFS()
                elif command == 3:
                    self.findPathBestFS()
            except EnvironmentError:
                print('invalid command')