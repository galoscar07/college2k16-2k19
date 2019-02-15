import os
import sys

from Version2.consts import NORMAL_STATE, STOP_CONDITION, FINAL_STATE, ERROR_STATE, BACK_STATE
from Version2.grammar import Grammar
from Version2.production import ProductionSet, Production
from Version2.utils import Stack, is_input_completed


def parse(grammar, input_string):
    s = NORMAL_STATE
    n = len(input_string) - 1
    counter = 0
    alpha = Stack()
    alpha.push(STOP_CONDITION)
    beta = Stack()
    beta.push('S')
    while s != FINAL_STATE and s != ERROR_STATE:
        if s is NORMAL_STATE:
            if is_input_completed(beta) and counter >= n + 1:
                s = FINAL_STATE
                break
            elif counter >= n+1:
                s = BACK_STATE
                continue
            else:
                non_terminal = False
                is_depth_increased = False
                if beta.peek() in grammar.non_terminals:
                    non_terminal = True
                elif type(beta.peek()) is ProductionSet and beta.peek().get_current().left_side != '':
                    non_terminal = True
                elif type(beta.peek()) is ProductionSet and beta.peek().get_current().get_current_atom() in grammar.non_terminals:
                    is_depth_increased = True
                    non_terminal = True
                if non_terminal:
                    head_of_beta = beta.pop()
                    if head_of_beta in grammar.non_terminals:
                        alpha.push(head_of_beta)
                        production_set = grammar.get_new_product_set_for_non_terminal(head_of_beta)
                        if production_set.current_production == -1:
                            production_set.current_production = 0
                        if production_set.current_production < len(production_set.production_list):
                            production_set.production_list[production_set.current_production].left_side = ''
                        beta.push(production_set)
                    else:
                        if is_depth_increased:
                            alpha.push(head_of_beta.get_current().get_current_atom())
                            if head_of_beta.current_production < len(head_of_beta.production_list):
                                old_head_of_beta = head_of_beta
                                head_of_beta = grammar.get_new_product_set_for_non_terminal(old_head_of_beta.get_current().get_current_atom())
                                old_head_of_beta.production_list[old_head_of_beta.current_production].current_position += 1
                                beta.push(old_head_of_beta)
                        else:
                            alpha.push(head_of_beta.get_current().left_side)
                        if head_of_beta.current_production == -1:
                            head_of_beta.current_production = 0
                            head_of_beta.production_list[head_of_beta.current_production].left_side = ''
                        beta.push(head_of_beta)
                else:
                    terminal = False
                    if type(beta.peek()) is ProductionSet \
                            and beta.peek().get_current().get_current_atom() == input_string[counter] \
                            and not beta.peek().get_current().is_production_checked():
                        terminal = True
                    if terminal:
                        counter += 1
                        head_of_beta = beta.pop()
                        alpha.push(head_of_beta.get_current().get_current_atom())
                        if head_of_beta.current_production < len(head_of_beta.production_list):
                            head_of_beta.production_list[head_of_beta.current_production].current_position += 1
                        beta.push(head_of_beta)
                    else:
                        s = BACK_STATE
        else:
            if s == BACK_STATE:
                terminal = False
                if alpha.peek() in grammar.terminals:
                    terminal = True
                if terminal:
                    counter -= 1
                    alpha.pop()
                    head_of_beta = beta.pop()
                    if head_of_beta.current_production < len(head_of_beta.production_list):
                        head_of_beta.production_list[head_of_beta.current_production].current_position -= 1
                    beta.push(head_of_beta)
                else:
                    if beta.peek().get_next_production() is not None:
                        s = NORMAL_STATE
                        beta.peek().get_previous_production()
                        head_of_beta = beta.pop()
                        head_of_beta.production_list[head_of_beta.current_production].left_side = alpha.peek()
                        head_of_beta.get_next_production()
                        head_of_beta.production_list[head_of_beta.current_production].left_side = ''
                        beta.push(head_of_beta)
                    else:
                        if counter == 0 and alpha.peek() == 'S':
                            s = ERROR_STATE
                        else:
                            head_of_alpha = alpha.pop()
                            head_of_beta = beta.pop()
                            if head_of_alpha == head_of_beta.get_previous_production().get_current_atom():
                                if head_of_beta.current_production < len(head_of_beta.production_list):
                                    head_of_beta.production_list[head_of_beta.current_production].current_position -= 1
                            else:
                                if head_of_beta.current_production < len(head_of_beta.production_list):
                                    head_of_beta.production_list[head_of_beta.current_production].left_side = head_of_alpha
                            beta.push(head_of_beta)
    if s == ERROR_STATE:
        message = "EROARE"
        is_error = True
    else:
        message = "Secventa este acceptata"
        is_error = False
    return {'message': message, 'is_error': is_error, 'data': str(alpha)}


def get_non_terminal_list_and_symbol_table_dictionary(filename):
    symbol_table = {}
    non_terminals_list = []

    try:
        f = open(filename)
        if os.stat(filename).st_size == 0:
            raise IOError
        for line in f.readlines():
            (symbol, sid) = line.split()
            non_terminals_list.append(symbol)
            symbol_table[sid] = symbol
    except IOError as e:
        # in case there is no such file, fail fast!
        print('ERROR: Symbols file not found. Except message %s' % e)
        sys.exit()
    return non_terminals_list, symbol_table


def get_terminal_list_from_file(filename, sym_table):
    terminal_list = []
    try:
        f = open(filename)
        if os.stat(filename).st_size == 0:
            raise IOError
        for line in f.readlines():
            (terminal, tid) = line.split()
            terminal_list.append(terminal)
    except IOError:
        print('ERROR: Symbols file not found. Except message %s' % e)
        sys.exit()

    for i in range(len(terminal_list)):
        terminal_list[i] = sym_table[terminal_list[i]]

    return terminal_list


if __name__ == '__main__':
    print('Hello World!')
    print('Solution 2\n')
    non_terminals, sym_table = get_non_terminal_list_and_symbol_table_dictionary('/Users/galoscar/Documents/University&Shits/Formal Languages and Compiler Design/Laboratory/LabAssignment4/Version2/data/symbols.dat')
    # for elem in non_terminals:
    #     print(elem)
    # for key, value in sym_table.items():
    #     print('%s - %s' % (key, value))
    # era w nu terminal terminal in cazul asta ar fi a
    w = get_terminal_list_from_file('/Users/galoscar/Documents/University&Shits/Formal Languages and Compiler Design/Laboratory/LabAssignment4/Version2/data/example1_pif.txt', sym_table)
    # for elem in terminals:
    #     print(elem)

    rule_list = ['A>ab', 'S>cdA', 'A>a']
    production_list = [Production.init_from_production_string(rule) for rule in rule_list]
    production_list = sorted(production_list, key=lambda x: x.left_side)
    current_non_terminal = None
    production_set_list = []
    for i in range(len(production_list)):
        if current_non_terminal != production_list[i].left_side:
            if i > 0:
                production_set = ProductionSet()
                production_set.production_list = rules_for_non_terminal
                production_set.non_terminal = current_non_terminal
                production_set_list.append(production_set)
            current_non_terminal = production_list[i].left_side
            rules_for_non_terminal = [production_list[i]]
        else:
            rules_for_non_terminal.append(production_list[i])
    production_set = ProductionSet()
    production_set.production_list = rules_for_non_terminal
    production_set.non_terminal = current_non_terminal
    production_set_list.append(production_set)

    grammar = Grammar()
    grammar.set_initial_symbol('S')
    grammar.set_non_terminals(non_terminals)
    grammar.set_production(production_set_list)
    # grammar.set_terminals(terminals)

    print(parse(grammar, w))
