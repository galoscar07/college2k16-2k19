class Graph(object):
    def __init__(self, mat, noVertices):
        """
        The function will initialize the class called UnDirGraph
        :param noVertices: the parameter is a integer one and it represents the no of vertices
        """
        self.__noVertices = noVertices
        self.__matrix = mat

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

    def isEdge(self, x, y):
        """
        The function will verify if their is an edge between the vertex x and y
        :param x: represents a vertex
        :param y: represents another vertex
        :return: The function will return true is their is an edge between x and y and false otherwise
        """
        if self.__matrix[x][y] == 1 and self.__matrix[y][x] == 1:
            return True
        return False

    def minKey(self, key, mstSet):
        min = 99999
        for v in range(0,self.__noVertices):
            if (mstSet[v] == False) and (key[v] < min):
                min = key[v]
                minIndex = v

        return minIndex

    def printMST(self, parent):
        print("Edge \n")
        for i in range(1, self.__noVertices):
            print(parent[i]," - ", i)
        print("\n")

    def primMST(self):
        parent = [0]*self.__noVertices
        key = [999]*self.__noVertices
        mstSet = [False]*self.__noVertices
        for i in range(0, self.__noVertices):
            key[i] = 9
            mstSet[i] = False
        key[0] = 0
        parent[0] = -1
        for count in range(0, self.__noVertices-1):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(0, self.__noVertices):
                if (self.__matrix[u][v] and mstSet[v] == False and self.__matrix[u][v] < key[v]):
                    parent[v] = u
                    key[v] = self.__matrix[u][v]
        self.printMST(parent)
