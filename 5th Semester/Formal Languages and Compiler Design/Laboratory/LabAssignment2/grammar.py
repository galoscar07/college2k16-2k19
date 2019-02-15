class Grammar(object):
    arrow_symbol = '->'
    empty_string = 'E'

    def __init__(self):
        self.terminals = set([])
        self.non_terminals = set([])
        self.productions = list()

    @staticmethod
    def str_arrow():
        return ' %s ' % Grammar.arrow_symbol

    @classmethod
    def from_console(cls):
        new = Grammar()
        print('Just enter an empty string when your done.')
        non_terminal = raw_input('Non-terminal: ')
        while non_terminal != '':
            new.non_terminals.add(non_terminal)
            non_terminal = raw_input('Non-terminal: ')
        terminal = raw_input('Terminal: ')
        while terminal != '':
            new.terminals.add(terminal)
            terminal = raw_input('Terminal: ')
        prod = raw_input('Production (ex: S -> aS or A -> E): ')
        while prod != '':
            non_terminal, result = prod.split(cls.str_arrow())
            if len(result) == 1:
                if result != cls.empty_string:
                    print 'Invalid production!'
                    continue
                new.productions.append((non_terminal, result))
            else:
                new.productions.append((non_terminal, result[0], result[1]))
            prod = raw_input('Production (ex: S -> aS or A -> E): ')
        return new

    @classmethod
    def from_file(cls, filename):
        new = Grammar()
        with open(filename, mode='r') as f:
            new.non_terminals = f.readline().strip().split(' ')
            new.terminals = f.readline().strip().split(' ')
            for line in f:
                non_terminal, result = line.strip().split(cls.str_arrow())
                if len(result) == 1:
                    assert result == cls.empty_string, 'Invalid grammar!'
                    new.productions.append((non_terminal, result[0]))
                else:
                    new.productions.append([
                        non_terminal, result[0], result[1]
                    ])
        return new

    @classmethod
    def from_finite_automata(cls, fa):
        new = Grammar()
        new.non_terminals = fa.states
        new.terminals = fa.alphabet
        for a in fa.accepting:
            new.productions.append((a, cls.empty_string))
        for t in fa.transitions:
            new.productions.append((t[0], t[2], t[1]))
        return new

    def is_regular(self):
        return self.is_right_regular() or self.is_left_regular()

    def is_right_regular(self):
        return all([
            prod[0] in self.non_terminals and
            (
                len(prod) == 2 or
                (prod[1] in self.terminals and prod[2] in self.non_terminals)
            )
            for prod in self.productions
        ])

    def is_left_regular(self):
        return all([
            prod[1] in self.non_terminals and prod[0] in self.terminals
            for prod in self.productions
        ])
