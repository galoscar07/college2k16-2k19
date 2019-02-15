from unittest import TestCase

from parser import JsonParser


class TestParser(TestCase):
    """
     Methods:
        lex_string: Method that parse a string from a quote until the next quote and return the string between the quote
                    and return None if there isn't any quote.
        lex_number: Method that parse a string to find a number. If a number was found it is returned else return None
        lex_bool: Method that parse a string to find a bool value (True or False). If a bool value was found it will be
                  returned else it will return None
        lex_null: Method that parse a string to find a null value. If a null value was found the method will return True
                  else it will return None
        lex: Method that parse a given string and return a list containing all the tokens of that list
        parse_array: Parse all the tokens between the [ ] symbols and create a list with them and return it
        parse_object: Parse all the tokens between the { } symbols and create a dictionary with them and return it
        parse: The method will parse through the token list and decide if the token is an object or a list or a
               dictionary and call the specific function for each
        loads: Function check if the string given is a json or it is a file in which the json is.
        from_string: The method will call functions for parsing the string and constructing the object
        from_file: The method will open the file and read from it and call function for parsing the string and
                   constructing the object
    """
    def setUp(self):
        self.parser = JsonParser()

    def tests(self):
        parse_from_string = self.parser.loads('{"foo":{"bar":[1,2,3]}}')
        self.assertEqual(parse_from_string.get('foo').get('bar'), [1, 2, 3])

        parse_from_file = self.parser.loads('example_json.txt')
        self.assertEqual(parse_from_file.get('name'), 'John')
        self.assertEqual(parse_from_file.get('age'), 30)
        self.assertEqual(parse_from_file.get('city'), 'New York')
