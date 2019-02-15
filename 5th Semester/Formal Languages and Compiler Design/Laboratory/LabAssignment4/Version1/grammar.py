from production import ProductionSet


class Grammar(object):
    """
    The class that will represents a grammar. eg: G([A,B,C,S], [a,b,c,d], [S->aB, B->c], S)
    """
    def __init__(self):
        self.terminals = []
        self.non_terminals = []
        self.initial_symbol = ''

        # type ProductionSet
        self.productions = []

    def set_terminals(self, terminal_list):
        # setter fot the terminal attribute
        self.terminals = terminal_list

    def set_non_terminals(self, non_terminals_list):
        # setter fot the non_terminals attribute
        self.non_terminals = non_terminals_list

    def set_initial_symbol(self, initial_symbol):
        # setter for the initial symbol
        self.initial_symbol = initial_symbol

    def set_production(self, productions_list):
        # setter for the production list
        self.productions = productions_list

    def is_terminal(self, item_to_be_checked):
        return item_to_be_checked in self.terminals

    def is_non_terminal(self, item_to_be_checked):
        return item_to_be_checked in self.non_terminals

    def get_new_product_set_for_non_terminal(self, non_terminal):
        for production in self.productions:
            if production.non_terminal == non_terminal:
                production_set = ProductionSet()
                production_set.non_terminal = production.non_terminal
                production_set.current_production = -1
                production_set.production_list = [item for item in production.production_list]
                return production_set

    def get_product_set_for_non_terminal(self, non_terminal):
        for production in self.productions:
            if production.non_terminal == non_terminal:
                return production
