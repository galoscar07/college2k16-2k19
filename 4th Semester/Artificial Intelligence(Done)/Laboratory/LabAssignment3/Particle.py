from cmath import sqrt
from random import random


class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @staticmethod
    def random(vmin, vmax):
        v = Vector2d(random() * (vmax - vmin) + vmin, random() * (vmax - vmin) + vmin)
        return v

    def copy(self):
        return Vector2d(self.x, self.y)

    def __mul__(self, number):
        if isinstance(number, int) or isinstance(number, float):
            return Vector2d(self.x * number, self.y * number)

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)


class Particle:
    def __init__(self, vmin, vmax):
        self.__fitness = 0
        self.__position = Vector2d.random(vmin, vmax)
        self.__velocity = Vector2d(0, 0)

        # the memory of that particle
        self.__best_position = self.__position.copy()
        self.__best_fitness = self.__fitness

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value.copy()

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        self.__velocity = value.copy()

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, value):
        self.__fitness = value
        if self.__best_fitness > self.__fitness:
            self.__best_fitness = self.__fitness
            self.__best_position = self.__position.copy()

    @property
    def best_position(self):
        return self.__best_position

    @best_position.setter
    def best_position(self, value):
        self.__best_position = value

    @property
    def best_fitness(self):
        return self.__best_fitness

    @best_fitness.setter
    def best_fitness(self, value):
        self.__best_fitness = value
