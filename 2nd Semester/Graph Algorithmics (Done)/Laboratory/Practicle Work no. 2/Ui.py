class UI(object):
    def __init__(self,graph):
        self.__graph = graph

    def printMenu(self):
        string = "Available Commands: \n"
        string += "\t 1. Finds the connected components of an undirected graph using a breadth-first traversal of the graph \n"
        string += "\t 2. Print the list of adjancency\n"
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
                elif command == 2:
                    self.option2()
            except EnvironmentError:
                print(" ")

    def option1(self):
        print(self.__graph.connectedComponents())

    def option2(self):
        for i in self.__graph.getVertices():
            print(self.__graph.adjVertices(i))
