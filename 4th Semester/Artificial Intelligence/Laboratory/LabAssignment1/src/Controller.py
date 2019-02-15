class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def returnInitial(self):
        return self.__problem.getRoot()

    def returnFinal(self):
        return self.__problem.getFinal()


    def BFS(self, root):

        q = [root]
        visited = []

        while len(q) > 0:
            currentState = q.pop(0)
            if currentState.getValues()[-1] == self.__problem.getFinal():
                return currentState
            aux = self.__problem.expand(currentState)
            aux = [x for x in aux if x.getValues()[-1] not in visited]
            q = q + aux
            for e in aux:
                visited.append(e.getValues()[-1])

    def BestFS(self, root):

        visited = []
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node.getValues()[-1]]
            if node.getValues()[-1] == self.__problem.getFinal():
                return node
            aux = self.__problem.expand(node)
            aux = [x for x in aux if x.getValues()[-1] not in visited]

            aux = sorted([x for x in aux], key=lambda z: self.__problem.heuristics(z, self.__problem.getFinal()))

            toVisit = aux[:] + toVisit
