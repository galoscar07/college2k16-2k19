from copy import deepcopy

from src.State import State

class Problem:
    def __init__(self, filename):
        self.__initialConfig = []
        self.__finalConfig = []
        self.loadFromFile(filename)
        self.__initialState = State()
        self.__initialState.setValues([self.__initialConfig])

    def loadFromFile(self, filename):
        with open(filename) as file:
            line = [line.split() for line in file]
            n = len(line)

            for i in range(0,n):
                for j in range(0,n//2):
                    line[i][j] = int(line[i][j])

            self.__initialConfig = line[0:n//2]
            self.__finalConfig = line[n//2:]


    def expand(self, currentState):
        myList = []
        for i in self.nextConfig(currentState.getValues()[-1]):
            myList.append(currentState + i)
        return myList


    def getFinal(self):
        return self.__finalConfig

    def getRoot(self):
        return self.__initialState

    def heuristics(self, state, finalC):
        l = len(finalC)
        count = 2 * l
        for i in range(l):
            for j in range(l):
                if state.getValues()[-1][i][j] != finalC[i][j]:
                    count = count - 1
        return count

    def nextConfig(self, currentConfig):
        for i in range(0,len(currentConfig)):
            for j in range(0, len(currentConfig)):
                if currentConfig[i][j] == 0:
                    a = i
                    b = j
        nextC = []
        if a < len(currentConfig)-1:
            aux = deepcopy(currentConfig)
            aux[a][b], aux[a+1][b] = aux[a+1][b], aux[a][b]
            nextC.append(aux)
        if a > 0:
            aux = deepcopy(currentConfig)
            aux[a][b], aux[a-1][b] = aux[a-1][b], aux[a][b]
            nextC.append(aux)
        if b < len(currentConfig)-1:
            aux = deepcopy(currentConfig)
            aux[a][b], aux[a][b+1] = aux[a][b+1], aux[a][b]
            nextC.append(aux)
        if b > 0:
            aux = deepcopy(currentConfig)
            aux[a][b], aux[a][b-1] = aux[a][b-1], aux[a][b]
            nextC.append(aux)

        return nextC


