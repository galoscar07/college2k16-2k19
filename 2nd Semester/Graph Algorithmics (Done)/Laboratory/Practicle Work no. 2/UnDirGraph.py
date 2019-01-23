class UnDirGraph(object):
    def __init__(self, noVertices):
        """
        The function will initialize the class called UnDirGraph
        :param noVertices: the parameter is a integer one and it represents the no of vertices
        """
        self.__list = {}
        self.__noVertices = noVertices
        self.__acc = set()
        for i in range(noVertices):
            self.__list[i] = []

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
        return self.__list.keys()

    def addVertex(self,Vertex):
        """
        The function will add a vertex into the database of the graph
        :param Vertex: Is the vertex that need to be added
        """
        self.__list[Vertex] = []
        self.__noVertices += 1

    def removeVertex(self, vertex):
        """
        The function will remove a vertex from the list
        :param vertex: Is the vertex that we want to remove
        """
        for x in self.__list[vertex]:
            self.__list[x].remove(vertex)
        del self.__list[vertex]
        self.__noVertices -= 1

    def isEdge(self, x, y):
        """
        The function will verify if their is an edge between the vertex x and y
        :param x: represents a vertex
        :param y: represents another vertex
        :return: The function will return true is their is an edge between x and y and false otherwise
        """
        if x in self.__list[y]:
            return True
        return False

    def addEdge(self, x, y):
        """
        The function will add an edge between the vertices x and y
        :param x: represents a vertex
        :param y: represents another vertex
        """
        self.__list[x].append(y)
        self.__list[y].append(x)

    def removeEdge(self, x, y):
        """
        The function will remove an edge between the vertices
        :param x: represents a vertex
        :param y: represents another vertex y
        """
        self.__list[x].remove(y)
        self.__list[y].remove(x)

    def vertexDegree(self, vertex):
        """
        The function will retrun the degree of a given vertex
        :param vertex: Is the vertex that we want to find the degree
        :return: The function will return the degree of a vertex beeing an integer
        """
        return len(self.__list[vertex])

    def adjVertices(self, vertex):
        """
        The function will return the list of vertices of a vertex
        :param vertex: Is the vertex for which we return the neighbours vertices
        :return: the function will return a list of vertices
        """
        return self.__list[vertex]

    def neighbourList(self):
        something = self.getVertices()
        list = []
        i = 0
        for i in something:
            list.append(self.adjVertices(i))
        return list

    def aceessibleVertices(self, s):
        acc = set()
        acc.add(s)
        q = [s]
        while q:
            x = q[-1]
            q.pop()
            for y in self.adjVertices(x):
                if y not in acc:
                    acc.add(y)
                    q.append(y)
        return acc

    def bfs(self, s):
        acc = set()
        acc.add(s)
        q =[s]
        while q:
            x = q[0]
            q.pop(0)
            for y in self.adjVertices(x):
                if y not in acc:
                    acc.add(y)
                    q.append(y)
        return acc

    def connectedComponents(self):
        self.__acc = set()
        theListOfConnected = []
        for i in self.getVertices():
            if i not in self.__acc:
                something = self.bfs(i)
                for j in something:
                    self.__acc.add(j)
                theListOfConnected.append(something)
        return theListOfConnected


def loadFromFile(path):
    f = open(path, "r")
    line = f.readline().strip().split()
    nbrVertices = int(line[0])
    nbrEdges = int(line[1])
    graph = UnDirGraph(nbrVertices)
    for x in range(nbrEdges):
        line = f.readline().strip().split()
        x = int(line[0])
        y = int(line[1])
        graph.addEdge(x, y)
    return graph