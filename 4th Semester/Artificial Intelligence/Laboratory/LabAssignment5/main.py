from random import random, randint
import numpy as np
from math import sin, cos

# parameters
TrainSIZE = 0.75  # percentage of training size
TestSIZE = 0.25  # percentage of testing size
DEPTH_MAX = 11
ITER = 100
HEADER = []
F = ['+', '-', '*', 'sin', 'cos']
P = [0.332, 0.332, 0.332, 0.002, 0.002]
T = ["v" + str(x) for x in range(18)] + \
    ["c" + str(x) for x in range(10)]
C = [random() for _ in range(10)]


class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.size = 1

    def deepcopy(self):
        copy = Node()
        copy.val = self.val
        copy.size = self.size
        if self.left:
            copy.left = self.left.deepcopy()
        if self.right:
            copy.right = self.right.deepcopy()
        return copy

    def change(self, root, node1, node2):
        self.val = root.val
        if root.left:
            if root.left == node1:
                self.left = node2.deepcopy()
            else:
                self.left = Node()
                self.left.change(root.left, node1, node2)
        if root.right:
            if root.right == node1:
                self.right = node2.deepcopy()
            else:
                self.right = Node()
                self.right.change(root.right, node1, node2)
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def init(self, d):
        if d == 0:  # terminal
            self.val = np.random.choice(T)
            return
        self.val = np.random.choice(F, p=P)
        self.left = Node()
        self.left.init(d - 1)
        self.size += self.left.size
        if self.val != 'sin' and self.val != 'cos':
            self.right = Node()
            self.right.init(d - 1)
            self.size += self.right.size

    def get_nodes(self):
        ret = []
        if self.left:
            ret += self.left.get_nodes()
        ret.append(self)
        if self.right:
            ret += self.right.get_nodes()
        return ret

    def get_node(self, pos):
        if pos <= 0:
            assert False
        if pos > self.size:
            assert False
        if self.left and pos <= self.left.size:
            return self.left.get_node(pos)
        else:
            left_size = 0
            if self.left:
                left_size = self.left.size
            if left_size + 1 == pos:
                return self
            else:
                return self.right.get_node(pos - left_size - 1)

    def mutate(self, pos, prob):
        if pos <= 0:
            assert False
        if pos > self.size:
            assert False
        if self.left and pos <= self.left.size:
            self.left.mutate(pos, prob)
        else:
            left_size = 0
            if self.left:
                left_size = self.left.size
            if left_size + 1 == pos:
                if random() < prob:
                    if self.val in T:
                        self.val = np.random.choice(T)
                    else:
                        if self.val == 'sin':
                            self.val = 'cos'
                        elif self.val == 'cos':
                            self.val = 'sin'
                        else:
                            self.val = np.random.choice(F[:3])
            else:
                self.right.mutate(pos - left_size - 1, prob)

    def __str__(self):
        if self.val in T:
            return str(C[int(self.val[1])]) if self.val[0] == 'c' else str(self.val)
        if self.val == "sin" or self.val == "cos":
            return self.val + "(" + str(self.left) + ")"
        return str(self.left) + self.val + str(self.right)

    def __repr__(self):
        return self.__str__()


class Chromosome:
    def __init__(self, d=DEPTH_MAX):
        self.maxDepth = d
        self.fitness = 0
        self.root = Node()
        self.root.init(d)

    def evaluate(self, x, y):
        self.fitness = 0
        exp = str(self.root)
        cnt = 0
        for (x, y) in zip(x, y):
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            for i in range(len(x)):
                exec("{} = {}".format(HEADER[i], x[i]))
            res = eval(exp)
            self.fitness += abs(res - y)
        self.fitness = self.fitness / len(x)
        return self.fitness

    @staticmethod
    def crossover(ch1, ch2):
        node1 = np.random.choice(ch1.root.get_nodes())
        node2 = np.random.choice(ch2.root.get_nodes())
        c = Chromosome()
        if ch1.root == node1:  # if we must change the whole tree
            c.root = node2.deepcopy()
        else:
            c.root = Node()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)


class Population:
    def __init__(self, nr_ind):
        self.nr_ind = nr_ind
        self.arr = [Chromosome() for _ in range(nr_ind)]

    def evaluate(self, x, y):
        for ch in self.arr:
            ch.evaluate(x, y)

    def selection(self, max_ind):
        if max_ind < self.nr_ind:
            self.nr_ind = max_ind
            self.arr = sorted(self.arr, key=lambda x: x.fitness)
            self.arr = self.arr[:max_ind]

    def reunion(self, other):
        self.nr_ind += other.nr_ind
        self.arr = self.arr + other.arr

    def best(self, max_ind):
        arr_sorted = sorted(self.arr, key=lambda x: x.fitness)
        return arr_sorted[:max_ind]


class GPAlgorithm:
    def __init__(self, filename, nr_ind):
        self.n = 0
        self.x = []
        self.y = []
        self.xTest = []
        self.yTest = []
        self.xTrain = []
        self.yTrain = []
        self.filename = filename
        self.nr_ind = nr_ind
        self.pop = Population(nr_ind)
        self.probability_mutate = 0.5
        self.probability_crossover = 0.5

    def iteration(self):
        parents = range(self.nr_ind)
        nr_children = len(parents) // 2
        offspring = Population(nr_children)
        for i in range(nr_children):
            offspring.arr[i] = Chromosome.crossover(self.pop.arr[i << 1], self.pop.arr[(i << 1) | 1])
            offspring.arr[i].mutate(self.probability_mutate)
        offspring.evaluate(self.xTrain, self.yTrain)
        self.pop.reunion(offspring)
        self.pop.selection(self.nr_ind)

    def run(self):
        global ITER
        self.load_data_set()
        self.pop.evaluate(self.xTrain, self.yTrain)
        for i in range(ITER):
            print("Iteration: " + str(i))
            self.iteration()
            self.pop.evaluate(self.xTrain, self.yTrain)
            self.pop.selection(self.nr_ind)
            best = self.pop.best(1)[0]
            print("Best fitness: " + str(best.fitness) + " function: " + str(best.root))

    def load_data_set(self):
        global TrainSIZE, TestSIZE, HEADER
        with open(self.filename) as file:
            lines = [line.split(",") for line in file]
            lines = lines[:101]
            HEADER = lines[0][1:-1]
            for line in lines[1:]:
                self.y.append(float(line[5]))
                self.x.append(line[1:3] + line[6:])
                self.n += 1

        for a in self.x:
            a = [float(i) for i in a]

        self.xTrain = self.x[:int(self.n * TrainSIZE)]
        self.yTrain = self.y[:int(self.n * TrainSIZE)]
        self.xTest = self.x[int(self.n * TrainSIZE):]
        self.yTest = self.y[int(self.n * TrainSIZE):]
        print("Training size: " + str(len(self.xTrain)))
        print("Testing size: " + str(len(self.yTest)))


if __name__ == '__main__':
    alg = GPAlgorithm("data.txt", 10)
    alg.run()
