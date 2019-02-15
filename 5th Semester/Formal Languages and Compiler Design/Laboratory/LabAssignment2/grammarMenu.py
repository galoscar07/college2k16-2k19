from finiteAutomata import FiniteAutomata
from grammar import Grammar


class GrammarMenu(object):
    def __init__(self, grammar):
        self.grammar = grammar

    def go(self):
        print GrammarMenu.str_menu()
        choice = raw_input('Choice: ')
        while choice != '6':
            if choice == '1':
                print 'Non-terminals:'
                print ', '.join(self.grammar.non_terminals)
            elif choice == '2':
                print 'Terminals:'
                print ', '.join(self.grammar.terminals)
            elif choice == '3':
                print 'Productions set:'
                for prod in self.grammar.productions:
                    res = prod[1:]
                    print '%s%s%s' % (
                        prod[0], self.grammar.str_arrow(), ''.join(res)
                    )
            elif choice == '4':
                non_terminal = raw_input('Please give non-terminal: ')
                if non_terminal not in self.grammar.non_terminals:
                    print 'Invalid non-terminal!'
                else:
                    print 'Productions for non-terminal %s:' % non_terminal
                    for prod in self.grammar.productions:
                        if prod[0] == non_terminal:
                            print '%s%s%s%s' % (
                                prod[0], self.grammar.str_arrow(), prod[1], prod[2]
                            )
            elif choice == '5':
                print self.grammar.is_regular()

            print '__' * 20
            choice = raw_input('Choice: ')

    @staticmethod
    def str_menu():
        return ''.join([
            '1. Non-terminals\n',
            '2. Terminals\n',
            '3. Productions\n',
            '4. Productions for non-terminal\n',
            '5. Check if grammar is regular.\n',
            '6. Exit\n'
        ])