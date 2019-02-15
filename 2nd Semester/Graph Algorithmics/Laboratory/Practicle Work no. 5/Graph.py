import itertools

class Graph:
    def __init__(self, n):
        self.__noVertices = n
        self.__neighbours = {}
        for i in range(0,n+1):
            self.__neighbours[i] = set()

    def addEdge(self, x, y):
        self.__neighbours[x].add(y)

    def parseX(self):
        return self.__neighbours.keys()

    def parseNeighbors(self, x):
        return self.__neighbours[x]

    def vertexCover(graph):
        visited = set()
        for u in graph.parseX():
            print(visited)
            if u not in visited:
                for v in graph.parseNeighbors(u):
                    if v not in visited:
                        visited.add(u)
                        visited.add(v)
                        break
        return visited

def loadFromFile(path):
    f = open(path,"r")
    line = f.readline().strip().split()
    nrVertices = int(line[0])
    nrEdges = line[1]
    graph = Graph(nrVertices)
    for line in f:
        something = line.split(" ")
        something = [int(s) for s in something]
        graph.addEdge(something[0],something[1])
    return graph