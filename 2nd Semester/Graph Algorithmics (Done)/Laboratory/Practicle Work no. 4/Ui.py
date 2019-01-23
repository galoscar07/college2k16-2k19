class UI(object):
    def __init__(self,graph):
        self.__graph = graph

    def printMenu(self):
        string = "Available Commands: \n"
        string += "\t 1. Write a program that, given an undirected connected graph, constructs a minumal spanning " \
                  "tree using the Prim's algorithm. \n"
        string += "\t 0. Exit"
        print (string)

    def menu(self):
        keepAlive = True
        while keepAlive:
            try:
                self.printMenu()
                command = int(input("Command: "))
                if command == 0:
                    keepAlive = False
                    print("Thank you for using the program. \n")
                elif command == 1:
                    self.option1()
            except EnvironmentError:
                print(" ")

    def option1(self):
        self.__graph.primMST()
