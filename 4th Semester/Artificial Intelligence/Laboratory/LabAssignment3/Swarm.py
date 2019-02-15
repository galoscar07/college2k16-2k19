from Particle import Particle


class Swarm:
    def __init__(self, count, vmin, vmax, func):
        self.__values = [Particle(vmin, vmax) for _ in range(count)]
        self.__function = func
        self.evaluate()

    @property
    def values(self):
        return self.__values

    def evaluate(self):
        for p in self.__values:
            f = self.__function(p.position.x, p.position.y)
            p.fitness = f

    def fitnesses(self):
        return [x.fitness for x in self.__values]
