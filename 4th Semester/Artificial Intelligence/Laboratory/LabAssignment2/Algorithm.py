from random import randint
import matplotlib.pyplot as plt

import numpy

from Individual import Individual
from Population import Population


class Algorithm:
    def __init__(self, problem):
        self.__generations = 0
        self.__problem = problem
        self.__probability = 0
        self.__size = 0
        self.read_parameters("param.in")
        self.__population = Population(self.__size, self.__problem.get_min(), self.__problem.get_max())

    @property
    def problem(self):
        return self.__problem

    @property
    def population(self):
        return self.__population

    def iteration(self):
        i1 = randint(0, len(self.__population.values) - 1)
        i2 = randint(0, len(self.__population.values) - 1)
        if i1 != i2:
            c = Individual.crossover(self.__population.values[i1], self.__population.values[i2], self.__probability)
            c.mutate(self.__probability, self.__problem.get_min(), self.__problem.get_max())

            f1 = self.__population.values[i1].fitness(self.__problem)
            f2 = self.__population.values[i2].fitness(self.__problem)
            fc = c.fitness(self.__problem)

            if (f1 > f2) and (f1 > fc):
                self.__population.values[i1] = c
            if (f2 > f1) and (f2 > fc):
                self.__population.values[i2] = c

    def run(self, generations=None):
        if not generations:
            generations = self.__generations
        for i in range(generations):
            self.iteration()

    def read_parameters(self, filename):
        with open(filename) as file:
            lines = [line for line in file]

        self.__probability = float(lines[0])
        self.__size = int(lines[1])
        self.__generations = int(lines[2])

    def run_with_print(self, generations=None):
        if not generations:
            generations = self.__generations

        variations = []
        for i in range(generations):
            self.iteration()
            graded = self.__population.evaluate(self.__problem)
            arr = numpy.array([x[0] for x in graded])
            std = numpy.std(arr, axis=0)
            variations.append(std)

        # print the best individual
        graded = self.__population.evaluate(self.__problem)

        graded = sorted(graded, key=lambda x: x[0])
        result = graded[0]
        fitness_optim = result[0]
        individual_optim = result[1]
        generations = self.__generations
        print(
            f"Result: The detected minimum point after {generations:d} "
            f"iterations is f({individual_optim.x:3.5f},{individual_optim.y:3.5f}) = {fitness_optim:3.5f}.")

        plt.plot(variations)
        plt.show()

    def statistics(self):
        fitnesses = []
        for test in range(30):
            self.__population = Population(40, self.__problem.get_min(), self.__problem.get_max())
            self.run(1000)

            # print the best individual
            graded = self.__population.evaluate(self.__problem)

            graded = sorted(graded, key=lambda x: x[0])
            result = graded[0]
            fitness_optim = result[0]
            individual_optim = result[1]
            print(f"f({individual_optim.x:3.5f},{individual_optim.y:3.5f}) = {fitness_optim:3.5f}.")
            fitnesses.append(fitness_optim)

        arr = numpy.array(fitnesses)
        mean = numpy.mean(arr, axis=0)
        std = numpy.std(arr, axis=0)
        print("Mean: %.4f" % mean)
        print("Std:  %.4f" % std)
