class Graph:
    """

    Input:
    Output:
    Precondition:
    """
    def __init__(self, n):
        self._dictOut = {}
        self._dictIn = {}
        self._dictCost = {}
        self._length = n
        for i in range(n):
            self._dictOut[i] = []
            self._dictIn[i] = []

    def parseOut(self, x):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ",x)
        else:
            return self._dictOut[x]

    def parseIn(self, x):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ",x)
        else:
            return self._dictIn[x]

    def isEdge(self, x, y):
        if self.isVertex(x) == False:
            return EnvironmentError("There is no edge ",x)
        elif self.isVertex(y) == False:
            return EnvironmentError("There is no edge ",y)
        else:
            return y in self._dictOut[x]

    def addEdge(self, x, y, z = 0):
        if self.isVertex(x) == False:
            raise Exception("There is no edge ")
        elif self.isVertex(y) == False:
            raise Exception("There is no edge ")
        else:
            self._dictOut[x].append(y)
            self._dictIn[y].append(x)
            if z > 0:
                self._dictCost[(x,y)] = z

    def addAnEdge(self,x,y,z):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ")
        elif self.isVertex(y) == False:
            raise EnvironmentError("There is no edge ")
        else:
            if y in self._dictOut[x] != None:
                raise EnvironmentError("There is already an edge like this")
            self._dictOut[x].append(y)
            self._dictIn[x].append(y)
            self._dictCost[(x,y)] = z

    def removeVertex(self, x):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ",x)
        else:
            toDelete = []
            for i in self._dictCost:
                if x in i:
                    toDelete.append(i)
            for i in self._dictOut[x]:
                self._dictIn[i].remove(x)
            for i in self._dictIn[x]:
                self._dictOut[i].remove(x)
        for j in toDelete:
            del self._dictCost[j]
        del self._dictOut[x]
        del self._dictIn[x]
        self._length -= 1

    def removeEdge(self, x, y):
        if self.isVertex(x) == False:
            raise Exception("There is no edge ",x)
        elif self.isVertex(y) == False:
            raise Exception("There is no edge ",x)
        else:
            self._dictOut[x].remove(y)
            self._dictIn[y].remove(x)
            del self._dictCost[(x,y)]

    def numberOfVertices(self):
        return self._length

    def addVertex(self, x):
        if self.isVertex(x) != False:
            raise EnvironmentError("There is already an vertex like this ",x)
        else:
            self._dictOut[x] = []
            self._dictIn[x] = []
            self._length += 1

    def returnCost(self,x,y):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ",x)
        elif self.isVertex(y) == False:
            raise EnvironmentError("There is no edge ",y)
        else:
            return self._dictCost[(x,y)]

    def changeCost(self,x,y,z):
        if self.isVertex(x) == False:
            raise EnvironmentError("There is no edge ",x)
        elif self.isVertex(y) == False:
            raise EnvironmentError("There is no edge ",y)
        else:
            self._dictCost[(x,y)] = z

    def isVertex(self,x):
        if not x in self._dictOut or not x in self._dictIn:
            return False

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
