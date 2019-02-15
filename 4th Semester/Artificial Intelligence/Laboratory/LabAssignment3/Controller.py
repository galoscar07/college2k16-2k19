from random import random

import numpy
import matplotlib.pyplot as plt

from Swarm import Swarm


class Controller:
    def __init__(self, problem):
        self.__w = 0
        self.__c1 = 0
        self.__c2 = 0
        self.__size = 0
        self.__iterations = 0
        self.__problem = problem
        self.read_parameters("param.in")
        self.__population = Swarm(self.__size, self.__problem.get_min(), self.__problem.get_max(), problem.function)
        self.__population.evaluate()

    @property
    def problem(self):
        return self.__problem

    @property
    def population(self):
        return self.__population

    def iteration(self):
        best_neighbor = self.population.values[0]
        for p in self.population.values:
            if p.fitness < best_neighbor.fitness:
                best_neighbor = p

        # update the velocity for each particle
        for i in range(self.__size):
            social = (best_neighbor.position - self.population.values[i].position) * self.__c2 * random()
            personal = \
                (self.population.values[i].best_position - self.population.values[i].position) * self.__c1 * random()
            new_velocity = self.__population.values[i].velocity * self.__w + social + personal

            self.population.values[i].velocity = new_velocity

        # update the position for each particle
        for p in self.population.values:
            p.position = p.position + p.velocity
            if p.position.x > self.__problem.get_max():
                p.position.x = self.__problem.get_max()
            if p.position.x < self.__problem.get_min():
                p.position.x = self.__problem.get_min()
            if p.position.y > self.__problem.get_max():
                p.position.y = self.__problem.get_max()
            if p.position.y < self.__problem.get_min():
                p.position.y = self.__problem.get_min()

        #  update fitnesses
        self.population.evaluate()

    def run(self, iterations=None):
        if not iterations:
            iterations = self.__iterations
        for i in range(iterations):
            self.iteration()

    def run_with_print(self, iterations=None):
        if not iterations:
            iterations = self.__iterations

        variations = []
        for i in range(iterations):
            self.iteration()
            fitnesses = self.__population.fitnesses()
            arr = numpy.array(fitnesses)
            std = numpy.std(arr, axis=0)
            variations.append(std)

        # print the best individual
        best = self.__population.values[0]
        for p in self.__population.values:
            if p.best_fitness < best.best_fitness:
                best = p

        print(
            f"Result: The detected minimum point after {iterations:d} "
            f"iterations is f({best.best_position.x:3.5f},{best.best_position.y:3.5f}) = {best.best_fitness:3.5f}.")

        plt.plot(variations)
        plt.show()

    def statistics(self):
        fitnesses = []
        for test in range(30):
            self.__population = Swarm(40, self.__problem.get_min(), self.__problem.get_max(), self.problem.function)
            self.__size = 40
            self.run(1000)

            # print the best individual
            best = self.__population.values[0]
            for p in self.__population.values:
                if p.best_fitness < best.best_fitness:
                    best = p

            print(f"f({best.best_position.x:3.5f},{best.best_position.y:3.5f}) = {best.best_fitness:3.5f}.")
            fitnesses.append(best.best_fitness)

        arr = numpy.array(fitnesses)
        mean = numpy.mean(arr, axis=0)
        std = numpy.std(arr, axis=0)
        print("Mean: %.4f" % mean)
        print("Std:  %.4f" % std)

    def read_parameters(self, filename):
        with open(filename) as file:
            lines = [line for line in file]

        self.__w = float(lines[0])
        self.__c1 = float(lines[1])
        self.__c2 = float(lines[2])
        self.__size = int(lines[3])
        self.__iterations = int(lines[4])

        return True
