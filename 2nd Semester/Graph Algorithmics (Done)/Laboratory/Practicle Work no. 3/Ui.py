class UI(object):
    def __init__(self,graph):
        self.__graph = graph

    def printMenu(self):
        string = "Available Commands: \n"
        string += "\t 1. Lowest cost walk between 2 vertices \n"
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
        print("Please give 2 vertices: ")
        vertex1 = int(input("Vertex 1:"))
        vertex2 = int(input("Vertex 2:"))
        something = self.__graph.shortestPath(vertex1, vertex2)
        print (something)
