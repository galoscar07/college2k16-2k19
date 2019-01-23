import json

import numpy as np


class FuzzyVariable:
    def __init__(self):
        self.labels = {}
        self.value = 0

    def to_discrete(self):
        ret = {}
        graph = self.labels
        value = self.value
        for key in graph.keys():
            for i in range(len(graph[key]) - 1):
                if graph[key][i][0] <= value <= graph[key][i + 1][0]:
                    if graph[key][i][0] == -np.inf:
                        ret[key] = graph[key][i][1]
                        continue
                    if graph[key][i + 1][0] == np.inf:
                        ret[key] = graph[key][i + 1][1]
                        continue
                    delta_y = graph[key][i + 1][1] - graph[key][i][1]
                    delta_x = graph[key][i + 1][0] - graph[key][i][0]
                    ret[key] = graph[key][i][1] + ((value - graph[key][i][0]) / delta_x) * delta_y
        return ret


class Texture(FuzzyVariable):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.labels = {}


class Capacity(FuzzyVariable):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.labels = {}


class Ruler:
    def __init__(self):
        self.rules = {}

    def evaluate(self, t, c):
        t_dict = t.to_discrete()
        c_dict = c.to_discrete()
        res_dict = {}
        print(t_dict)
        print(c_dict)
        for tk, tv in t_dict.items():
            for ck, cv in c_dict.items():
                res = self.rules[tk][ck]
                val = min(tv, cv)
                if res in res_dict:
                    res_dict[res] = max(res_dict[res], val)
                else:
                    res_dict[res] = val
        return res_dict


class Controller:
    def __init__(self, problem_file, input_file, output_file):
        self.texture = 0
        self.capacity = 0
        self.load_input(input_file)
        self.r = Ruler()
        self.t = Texture(self.texture)
        self.c = Capacity(self.capacity)
        self.load_problem(problem_file)
        self.output = output_file

    def solve(self):
        result = self.r.evaluate(self.t, self.c)
        print(result)
        r = sorted(list(result.items()), key=lambda x: x[1])[-1][0]
        print(r)
        with open(self.output, "w") as file:
            file.write(r)

    def load_problem(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            texture = data["texture"]
            capacity = data["capacity"]
            cycle_type = data["cycle-type"]
            rules = data["rules"]
            self.t.labels = texture
            self.c.labels = capacity
            self.r.rules = rules

    def load_input(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            self.texture = data["texture"]
            self.capacity = data["capacity"]


if __name__ == '__main__':
    cont = Controller("problem.in", "input.in", "output.out")
    cont.solve()
