from random import random


class Individual:
    def __init__(self, vmin, vmax):
        self.__x = random() * (vmax - vmin) + vmin
        self.__y = random() * (vmax - vmin) + vmin

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def fitness(self, problem):
        return problem.function(self.__x, self.__y)

    def mutate(self, probability, vmin, vmax):
        if probability > random():
            if random() > 0.5:
                self.__x = random() * (vmax - vmin) + vmin
            else:
                self.__y = random() * (vmax - vmin) + vmin

    @staticmethod
    def crossover(parent1, parent2, probability):
        return Individual(probability * (parent1.x - parent2.x) + parent2.x,
                          probability * (parent1.y - parent2.y) + parent2.y)
