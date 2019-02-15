from src.graph import Graph


class UI(object):
    def __init__(self,graph):
        self.__graph = graph

    def printMenu(self):
        string = "Available Commands: \n"
        string += "\t 1. Show the number of vertices \n"
        string += "\t 2. Check if exist an edge between 2 vertices \n"
        string += "\t 3. In degree of a vertex \n"
        string += "\t 4. Out degree of a vertex \n"
        string += "\t 5. Iterate through the set of outbound edges of a specified vertex \n"
        string += "\t 6. Iterate through the set of inbound edges of a specified vertex \n"
        string += "\t 7. Modify the information attached to a specified edge \n"
        string += "\t 8. Retrieve the information (the integer) attached to a specified edge \n"
        string += "\t 9. Add an edge \n"
        string += "\t 10. Delete an edge \n"
        string += "\t 11. Add a vertex \n"
        string += "\t 12. Remove a vertex \n"
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
                elif command == 3:
                    self.option3()
                elif command == 4:
                    self.option4()
                elif command == 5:
                    self.option5()
                elif command == 6:
                    self.option6()
                elif command == 7:
                    self.option7()
                elif command == 8:
                    self.option8()
                elif command == 9:
                    self.option9()
                elif command == 10:
                    self.option10()
                elif command == 11:
                    self.option11()
                elif command == 12:
                    self.option12()
            except EnvironmentError as e:
                print(e)
            except Exception as e:
                print(e)

    def option1(self):
        n = self.__graph.numberOfVertices()
        print("The number of vertices is: ", n, "\n")

    def option2(self):
        print("Please give the first vertex: ")
        x = int(input())
        print("Please give the secound vertex: ")
        y = int(input())
        bo = self.__graph.isEdge(x,y)
        if bo == True:
            print("There is an edge between ",x, " and ", y)
        else:
            print("There is no edge between ", x, " and ", y)

    def option3(self):
        print("Please give a vertex: ")
        x = int(input())
        print("The in degree of the vertex ", x, " is: ",len(self.__graph.parseIn(x)))

    def option4(self):
        print("Please give a vertex: ")
        x = int(input())
        print("The out degree of the vertex ", x, " is: ", len(self.__graph.parseOut(x)))

    def option5(self):
        print("Please give a vertex: ")
        x = int(input())
        print(self.__graph.parseIn(x))

    def option6(self):
        print("Please give a vertex: ")
        x = int(input())
        print(self.__graph.parseOut(x))

    def option7(self):
        print("Please give the first vertex: ")
        x = int(input())
        print("Please give the secound vertex: ")
        y = int(input())
        print("Please give a cost")
        z = int(input())
        self.__graph.changeCost(x,y,z)

    def option8(self):
        print("Please give the first vertex: ")
        x = int(input())
        print("Please give the secound vertex: ")
        y = int(input())
        print("The cost from ",x," to ",y," is: ",self.__graph.returnCost(x,y))

    def option9(self):
        print("Please give the first vertex: ")
        x = int(input())
        print("Please give the secound vertex: ")
        y = int(input())
        print("Please give a cost")
        z = int(input())
        self.__graph.addAnEdge(x,y,z)

    def option10(self):
        print("Please give the first vertex: ")
        x = int(input())
        print("Please give the secound vertex: ")
        y = int(input())
        self.__graph.removeEdge(x,y)

    def option11(self):
        print("Please give a vertex: ")
        x = int(input())
        self.__graph.addVertex(x)

    def option12(self):
        print("Please give a vertex")
        x = int(input())
        self.__graph.removeVertex(x)

"""
add remove vertex edge cod la specificatii
"""