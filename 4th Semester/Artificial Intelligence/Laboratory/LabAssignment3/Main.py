from Controller import Controller
from Problem import Problem

if __name__ == '__main__':
    # best params
    # w = 0.729
    # c1 = 2.0
    # c2 = 2.0
    problem = Problem()
    controller = Controller(problem)
    controller.run_with_print()
    controller.statistics()
