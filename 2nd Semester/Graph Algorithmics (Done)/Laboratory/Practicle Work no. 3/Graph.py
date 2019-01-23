import math

from copy import deepcopy


class Graph(object):
    def __init__(self, n):
        self.__dictOut = {}
        self.__dictIn = {}
        self.__dictCost = {}
        self.__noVertices = n
        for i in range(n):
            self.__dictOut[i] = []
            self.__dictIn[i] = []

    def isVertex(self, x):
        if not x in self.__dictOut or not x in self.__dictIn:
            return False

    def getCost(self, x, y):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ", x)
        elif self.isVertex(y) == False:
            raise EnvironmentError("There is no edge ", y)
        else:
            return self.__dictCost[(x, y)]

    def getNoVertices(self):
        """
        The function will return the number of vertices in the class UnDirGraph
        :return: the number of vertices which is an integer
        """
        return self.__noVertices

    def getVertices(self):
        """
        The function will return the list of vertices that are into the class UnDirGraph
        """
        list = []
        for i in range(0, self.__noVertices):
            list[i] = i

    def addEdge(self, x, y, z = 0):
        if self.isVertex(x) == False:
            raise Exception("There is no edge ")
        elif self.isVertex(y) == False:
            raise Exception("There is no edge ")
        else:
            self.__dictOut[x].append(y)
            self.__dictIn[y].append(x)
            if z > 0:
                self.__dictCost[(x,y)] = z


    def isEdge(self, x, y):
        if self.isVertex(x) == False:
            return EnvironmentError("There is no edge ",x)
        elif self.isVertex(y) == False:
            return EnvironmentError("There is no edge ",y)
        else:
            return y in self.__dictOut[x]

    def shortestPath(graph, vertex1, vertex2):
        """Finds the shortest path between the 2 vertices.
        Returns a list containing the path.
        Will raise an exception if there are negative cycles."""

        dim = graph.__noVertices
        dist = [[math.inf for x in range(dim)] for y in range(dim)]
        prev = [[y for x in range(dim)] for y in range(dim)]

        for i in range(dim):
            for j in range(dim):
                if not graph.isEdge(i, j):
                    prev[i][j] = None


        for x in range(dim):
            for y in range(dim):
                if graph.isEdge(x, y):
                    dist[x][y] = graph.getCost(x, y)
                if x == y:
                    dist[x][y] = 0

        nr = int(math.log2(dim)) + 1

        for i in range(nr):
            D = deepcopy(dist)
            for x in range(dim):
                for y in range(dim):
                    for k in range(dim):
                        if dist[x][y] > D[x][k] + D[k][y]:
                            dist[x][y] = D[x][k] + D[k][y]
                            prev[x][y] = k

        for i in range(dim):
            if dist[i][i] < 0:
                raise KeyError("There are negative cycles.")

        return dist[vertex1][vertex2]

def loadFromFile(path):
    f = open(path,"r")
    line = f.readline().strip().split()
    nrVertices = int(line[0])
    nrEdges = line[1]
    graph = Graph(nrVertices)
    for line in f:
        something = line.split(" ")
        something = [int(s) for s in something]
        graph.addEdge(something[0],something[1],something[2])
    return graph