from finiteAutomata import FiniteAutomata
from finiteAutomataMenu import FiniteAutomataMenu
from grammar import Grammar
from grammarMenu import GrammarMenu

if __name__ == '__main__':

    g_f = Grammar.from_file('/Users/galoscar/Documents/uni&shit/Formal Languages and Compiler Design/Laboratory/'
                            'LabAssignment2/data/grammar.txt')
    fa_g = FiniteAutomata.from_grammar(g_f)
    fam = FiniteAutomataMenu(fa_g)
    fam.go()

    # g_c = Grammar.from_console()
    # g_fa = Grammar.from_finite_automata(fa_f)

    # fa_f = FiniteAutomata.from_file('/Users/galoscar/Documents/uni&shit/Formal Languages and Compiler Design'
    #                                 '/Laboratory/LabAssignment2/data/finite_automata.txt')
    #
