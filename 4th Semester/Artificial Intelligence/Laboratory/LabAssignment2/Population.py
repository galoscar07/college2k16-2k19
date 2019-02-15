from Individual import Individual


class Population:
    def __init__(self, n, vmin, vmax):
        self.__no_individuals = n
        self.__v = [Individual(vmin, vmax) for _ in range(n)]

    def evaluate(self, problem):
        return [(x.fitness(problem), x) for x in self.__v]

    @property
    def values(self):
        return self.__v
