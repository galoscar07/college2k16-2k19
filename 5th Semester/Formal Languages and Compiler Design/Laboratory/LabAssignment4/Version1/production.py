class Production(object):
    def __init__(self):
        self.left_side = None
        self.right_side = None
        self.current_position = 0

    def __str__(self):
        # return the current production as a string; example S -> abA
        return self.left_side + ' > ' + self.right_side

    def __eq__(self, other):
        # check is 2 productions are equal, return True if 2 productions have same attributes, false otherwise
        if self.right_side == other.right_side and \
                self.left_side == other.right_side and \
                self.current_position == other.current_position:
            return True
        return False

    def __hash__(self):
        # return the hash of the production
        return hash(str(self))

    @staticmethod
    def init_from_production_string(production_string):
        # S -> abA where right side is S and left side is abA
        list_of_items = str(production_string).replace(' ', '').split('>')

        production = Production()
        production.left_side = list_of_items[0]
        production.right_side = list_of_items[1]

        return production

    def is_production_checked(self):
        # we check if the current position is bigger than the right side, aka the right side is parsed
        if self.current_position >= len(self.right_side):
            return True
        return False

    def get_current_atom(self):
        # if the right side of the current production is parsed return None
        if self.is_production_checked():
            return None

        # else return the current atom
        return self.right_side[self.current_position]


class ProductionSet(object):
    def __init__(self):
        self.production_list = []
        self.current_production = -1
        self.non_terminal = ''

    def get_next_production(self):
        self.current_production += 1
        if len(self.production_list) <= self.current_production:
            return None

        return self.production_list[self.current_production]

    def get_previous_production(self):
        self.current_production -= 1
        if self.current_production < 0:
            return None

        return self.production_list[self.current_production]

    def __str__(self):
        string = ''
        for item in self.production_list:
            string += str(item) + ' '
        return string

    def get_current(self):
        try:
            return self.production_list[self.current_production]
        except IndexError:
            return Production()
