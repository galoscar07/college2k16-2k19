class FiniteAutomata(object):
    def __init__(self):
        self.states = set([])
        self.alphabet = set([])
        self.start = ''
        self.accepting = set([])
        self.transitions = list()

    @classmethod
    def from_file(cls, filename):
        new = FiniteAutomata()
        with open(filename, mode='r') as f:
            new.states = f.readline().strip().split(' ')
            new.alphabet = f.readline().strip().split(' ')
            new.start = f.readline().strip()
            new.accepting = f.readline().strip().split(' ')
            for line in f:
                s, d, a = line.strip().split(' ')
                new.transitions.append((s, d, a))
        return new

    @classmethod
    def from_grammar(cls, g):
        new = FiniteAutomata()
        new.states = g.non_terminals
        new.alphabet = g.terminals
        new.start = g.non_terminals[0]
        new.accepting = {
            p[0] for p in g.productions if p[1] == g.empty_string
        }
        for p in g.productions:
            if len(p) == 3:
                new.transitions.append((p[0], p[2], p[1]))
        return new
