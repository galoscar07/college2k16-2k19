from math import exp, sqrt, cos, pi


class Problem:
    @staticmethod
    def function(x, y):
        f = -20 * exp(-0.2 * sqrt(0.5 * (x * x + y * y)))
        - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + exp(1) + 20
        return f

    @staticmethod
    def get_min():
        return -5

    @staticmethod
    def get_max():
        return 5


