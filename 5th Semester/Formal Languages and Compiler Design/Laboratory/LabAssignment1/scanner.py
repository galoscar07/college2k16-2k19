# bin
import sys
import os
from os import path
from random import randint

from binarySearchTree import BinarySearchTree

"""
1b) arbitrary length, no more that 250 characters
2a) unique symbol table for identifiers and constants
3b) Symbol table on lexicographically binary tree
"""


class Scanner(object):
    """
    Class that acts like a parser
        :param file_name - the source of the toy language
    """

    def __init__(self, file_name):
        """
        Constructor for the scanner, takes as a parameter the file name consisting of the source code
        that we want our lexer to tokenize
        :param file_name: the file that contain the source code of the toy language
        """
        # file refers to the toy language source code
        self.file_name = file_name
        # file to store the program internal form
        self.output_file_name = path.splitext(path.basename(file_name))[0] + '_pif.txt'
        # clear file if already exists
        open(self.output_file_name, 'w').close()
        # file to store the identifiers tables        # file to store the constants table
        self.output_ident_constants_table = path.splitext(path.basename(file_name))[0] + '_ident_const_table.txt'
        # lexicographically binary tree for all the program symbols
        self.symbol_table = BinarySearchTree()
        # lexicographically binary tree for storing the identifiers and constants, as pair
        # constant/identifier -> integer id
        self.identifiers_constants_table = BinarySearchTree()
        # load all the toy language symbols
        self.populate_symbol_table()

    def populate_symbol_table(self):
        """
        Method that loads from the memory disk into memory the symbol table
        :except: IOError: the symbol file was not found
                 OSError: the file is empty
        """
        try:
            file_path = 'symbols.dat'
            # open the file
            f = open(file_path)
            # check if the file is empty
            if os.stat(file_path).st_size == 0:
                raise OSError
            # iterate through its lines
            for line in f.readlines():
                # get the symbol and it's id
                (symbol, sid) = line.split()
                # add them to the symbol table
                self.symbol_table.set_pair_key_value(symbol, sid)
        except IOError as e:
            # in case there is no such file, fail fast!
            print('ERROR: Symbols file not found. Except message %s' % e)
            sys.exit()
        except OSError:
            # in case the symbol table is empty, fail fast!
            print('ERROR: Symbols file is empty.')
            sys.exit()

    @staticmethod
    def random_not_in_values(values):
        """
        Method that returns a random integer that is not in the values array
        :param values: is the values array
        :return: a random integer number
        """
        # return a random value between 1 an 100000
        rand = randint(1, 100000)
        # while that value already exists in the array values
        while rand in values:
            # generate a new one
            rand = randint(1, 100000)
        # return the number generated
        return rand

    def append_to_output(self, buff):
        """
        Method append buff to the file output_file_name
        :param buff: the data that needs to be added into the file
        :return: None
        """
        # open file
        with open(self.output_file_name, 'a') as f:
            # write the string buff as a new line
            f.write(buff)

    def write_tables(self):
        """
        Method write the identifier/constants tables
        :return: None
        """
        # open file for identifiers table
        with open(self.output_ident_constants_table, 'w') as f:
            # make a header for the table
            # iterate through the identifier/constants table
            for key, value in self.identifiers_constants_table.get_key_value_dict().items():
                # write the pair on a new line
                f.write('%s %s \n' % (key, value))

    def add_token(self, _token):
        """
        Method the decide if a _token is a symbol or an identifier
        :param _token: a symbol or an identifier
        """
        # if the token is in the symbols table, then it's a symbol
        if _token in self.symbol_table.get_key_value_dict():
            return self.add_symbol(_token)
        # else, it must be an identifier
        else:
            return self.add_identifier(_token)

    def add_symbol(self, _symbol):
        """
        Method that prints the symbol to the program internal form file output
        :param _symbol: that symbol that is going to be printed
        :return: True if the symbol was printed, False if the symbol is not a valid one
        """
        # if the symbol is in the symbol table
        if _symbol in self.symbol_table.get_key_value_dict():
            # print it
            self.append_to_output(str(self.symbol_table.get_key_value_dict()[_symbol]) + " 0\n")
            return True
        else:
            # return false because _symbol is not a valid symbol, and then throw an error
            return False

    # method prints identifier and it's id to the output file
    def add_identifier(self, _id):
        """
        Method that prints identifier and it's id to the output file
        :param _id: the identifier that is going to be printed
        :return: True if the identifier was added
        """
        # assign a new, unused integer id for the current identifier
        if _id not in self.identifiers_constants_table.get_key_value_dict():
            self.identifiers_constants_table.set_pair_key_value(
                _id, Scanner.random_not_in_values(
                    self.identifiers_constants_table.get_values()
                )
            )
        # print to program internal form output file
        self.append_to_output(
            self.symbol_table.get('identifier') + " " + str(self.identifiers_constants_table.get(_id)) + "\n")
        return True

    # method adds a constant to the table and prints it to the output file
    def add_constant(self, _val):
        """
        Method that adds a constant to the table and prints it to the output file
        :param _val: the constant that is going to be added
        """
        # assign a new, unused integer id for the current identifier
        if _val not in self.identifiers_constants_table.get_key_value_dict():
            self.identifiers_constants_table.set_pair_key_value(
                _val, Scanner.random_not_in_values(
                    self.identifiers_constants_table.get_values()
                )
            )
        # print to the program internl form output file
        self.append_to_output(
            self.symbol_table.get('constant') + " " + str(self.identifiers_constants_table.get(_val)) + "\n")
        return True

    def get_next_char(self):
        """
        Generator method that returns all the characters line by line
        :return: generator formed of line, column and character
        :except: IOError: the source file was not found
        """
        try:
            # open the file for reading
            f = open(self.file_name, 'r')
            # read all the lines
            lines = f.readlines()
            # iterate through lines
            for line_index, line in enumerate(lines):
                # iterate through columns
                for column_index, ch in enumerate(line):
                    # yield the line_index, column_index and the current character
                    yield [line_index, column_index, ch]
        # if the file wasn't found print the error and fail fast
        except IOError:
            print('ERROR: Source file was not found')
            sys.exit()

    def tokenize(self):
        """
        Method that tokenize the source file
        :return:
        """
        # get the generator
        char_iterator = self.get_next_char()
        try:
            # get the next values from the generator
            (i, j, ch) = next(char_iterator)
            # we iterate while we get a StopIteration exception
            while True:
                if ch == ".":
                    raise StopIteration
                # in case we have an alphabet character (a, b, .. z, A, B, .. Z)
                if ch.isalpha():
                    # variable to store the current identifier
                    _id = ""
                    # we iterate with the iterator while we have valid identifier characters
                    while ch.isalpha() or ch.isdigit():
                        # append the current character to _id
                        _id += ch
                        # get the next character
                        (i, j, ch) = next(char_iterator)
                    # at the end, if the lenght of the iterator is more than the max allowed lenght
                    # throw an error, and fail fast
                    if len(_id) > 250:
                        print("ERROR: Identifier has too many characters. (line, col) = (%d, %d)" % (i, j))
                        sys.exit()
                    # add the token to the interal bts
                    self.add_token(_id)
                    _id = ""
                # in case we have a digit (0-9)
                elif ch.isdigit():
                    # variable stores the current constant
                    _val = ""
                    if ch == '0':
                        print('ERROR: Constants should not start with 0 digit')
                        sys.exit()
                    # while there is a digit
                    while ch.isdigit():
                        # append the character to the constant
                        _val += ch
                        # get next character
                        (i, j, ch) = next(char_iterator)
                    if ch.isalpha():
                        print('ERROR: Identifier should not start with digits. (line, col) = (%d, %d)' % (i, j))
                        sys.exit()
                    # add the constant to the program internal form and to the internal bts
                    self.add_constant(_val)
                # ignore whitespace characters
                elif ch.isspace():
                    # get the next character
                    (i, j, ch) = next(char_iterator)
                elif ch == "'":
                    (i, j, ch) = next(char_iterator)
                    if ch.isdigit() or ch.isalpha():
                        string = "'" + ch + "'"
                        self.add_constant(string)
                    else:
                        print('ERROR: Char should only be formed out of digits or letters. (line, column) = (%d, %d)'
                              % (i, j))
                        sys.exit()
                    (i, j, ch) = next(char_iterator)
                    if ch != "'":
                        print('ERROR: Char should only have one character. (line, col) = (%d, %d)' % (i, j))
                        sys.exit()
                    (i, j, ch) = next(char_iterator)
                # else, we may have a symbol or an invalid identifier
                else:
                    # get the first character and store it in the _id variable
                    _id = ch
                    # try to get the second one for cases like >=, <=, == and !=
                    try:
                        # store last character
                        last = ch
                        # get the next character
                        (i, j, ch) = next(char_iterator)
                        # if we are in one of the cases >=, <=, == or !=, we update the variable
                        if (last == '>' or last == '<' or last == '=' or last == '!') and ch == '=':
                            _id = _id + ch
                    except StopIteration:
                        # no other character left to get, we simply pass cause we may have }
                        pass
                    # if we couldn't add the symbol, we throw an error because it is an unexpected
                    # symbol identifier
                    if not self.add_symbol(_id):
                        print("ERROR: Syntax Error detected at (line, col) = (%d, %d)" % (i, j))
                        print("ERROR: Unexpected token '%s'" % _id)
                        sys.exit()
        # in case we reached the end of the iteration
        except StopIteration:
            self.write_tables()
            print("> finish")


# method scans and tokenize the filename source code
def scan(filename):
    """
    Method that receive as parameter a filenam and tokenize the file source code
    :param filename: The source that is going to be tokenized
    :return: None
    :except: If there is any exception
    """
    # create the scaner
    s = Scanner(filename)
    # call the tokenize method
    s.tokenize()


# if name is main
if __name__ == '__main__':
    # get the first argument of the args
    # log it
    print("> scanning " + str(sys.argv[1]) + "...")
    # scan that filename
    scan(sys.argv[1])

