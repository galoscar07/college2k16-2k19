from Algorithm import Algorithm
from Problem import Problem

if __name__ == '__main__':
    problem = Problem()
    algorithm = Algorithm(problem)
    algorithm.run_with_print()
    algorithm.statistics()
