from finiteAutomata import FiniteAutomata
from grammar import Grammar


class FiniteAutomataMenu(object):
    def __init__(self, fa):
        self.fa = fa

    def go(self):
        print FiniteAutomataMenu.str_menu()
        keyboard_input = raw_input('Choice: ')
        while keyboard_input != '6':
            if keyboard_input == '1':
                print ', '.join(self.fa.states)
            elif keyboard_input == '2':
                print ', '.join(self.fa.alphabet)
            elif keyboard_input == '3':
                print self.fa.start
            elif keyboard_input == '4':
                print ', '.join(self.fa.accepting)
            elif keyboard_input == '5':
                for t in self.fa.transitions:
                    print '%s -- (%s) --> %s' % (t[0], t[2], t[1])

            print '___' * 20
            print('\n')
            keyboard_input = raw_input('Choice: ')

    @staticmethod
    def str_menu():
        return ''.join([
            '1. States\n',
            '2. Alphabet\n',
            '3. Start state\n',
            '4. Accepting states\n',
            '5. Transitions\n',
            '6. Exit\n'
        ])
