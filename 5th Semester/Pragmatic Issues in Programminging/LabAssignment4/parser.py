from const import JSON_QUOTE, TRUE_LEN, FALSE_LEN, NULL_LEN, JSON_WHITESPACE, JSON_SYNTAX, JSON_RIGHTBRACKET, \
    JSON_COMMA, JSON_RIGHTBRACE, JSON_COLON, JSON_LEFTBRACE, JSON_LEFTBRACKET
import logging

# set up the logger
log = logging.getLogger("logger")


class JsonParser(object):
    """
    A class used to parse strings and returns a Json

    Attributes:
        None attributes are required in order to initialize the class

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
    def __init__(self):
        pass

    @staticmethod
    def lex_string(string):
        """
        Method that parse a string from a quote until the next quote and return the string between the quote
        and return None if there isn't any quote.
        :param string: the string that is parsed
        :return: the string if any was found else return None
        :exception: Raise an exception if there isn't any end of the string
        """
        # initialize the variable in which we will store the string
        json_string = ''
        # if the string starts with a quote which is the sign that is a string
        if string[0] == JSON_QUOTE:
            # we copy it into the same variable without the first quote
            string = string[1:]
        else:
            # else this is not a string and we return None
            return None, string
        # we go through every character in the string
        for c in string:
            # if it is a quote - sign that we should stop
            if c == JSON_QUOTE:
                # return the formed string
                return json_string, string[len(json_string) + 1:]
            else:
                # continue to add to the final string
                json_string += c
        # If we didn't stop until the string is done the last quote is missing
        log.error("Expected end-of-string quote")
        raise Exception('Expected end-of-string quote')

    @staticmethod
    def lex_number(string):
        """
        Method that parse a string to find a number. If a number was found it is returned else return None. The method
        will only search for integers numbers
        :param string: The string that we are parsing
        :return: A pair made out of the number and the rest of the string that have to be parsed or a pair made out of
                None and the rest of the string that have to be parsed
        """
        # initialize the variable in which we will store the number
        json_number = ''
        # create a list with all the chars that can be in a number [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minus should not be
        # here and also comma cause we are looking for only non negative integers
        number_characters = [str(d) for d in range(0, 10)]
        # we parse every char in the string
        for c in string:
            # if it is a part of our list
            if c in number_characters:
                # then we add it into our final number
                json_number += c
            else:
                # then something is wrong and we go again with the process
                break
        # we copy what is left from the string
        rest = string[len(json_number):]
        # if we didn't put anything in the number we return None
        if not len(json_number):
            return None, string
        # else we return the number as int
        return int(json_number), rest

    @staticmethod
    def lex_bool(string):
        """
        Method that parse a string to find a bool value (True or False). If a bool value was found it will be returned
        else it will return None
        :param string: The string in which we will search for those values
        :return: A pair made out of the value found True/False and the rest of the string or in case of failure the
                method will return a pair made out of None and the rest of the string
        """
        # we compute the length of the string
        string_len = len(string)
        # if the length if grater than the 4 and if the string contains the string true
        if string_len >= TRUE_LEN and string[:TRUE_LEN] == 'true':
            # we return true and the remaining string
            return True, string[TRUE_LEN:]
        # we keep the same logic for false
        elif string_len >= FALSE_LEN and string[:FALSE_LEN] == 'false':
            return False, string[FALSE_LEN:]
        # if it isn't one of the above we return None and the remaining string
        return None, string

    @staticmethod
    def lex_null(string):
        """
        Method that parse a string to find a null value. If a null value was found the method will return True
        else it will return None
        :param string: The string in which we will search for those values
        :return: A pair made out of the value True and the rest of the string or in case of failure the
                method will return a pair made out of None and the rest of the string
        """
        # we keep the same logic as above but now instead of true or false we use the null variable
        string_len = len(string)

        if string_len >= NULL_LEN and string[:NULL_LEN] == 'null':
            return True, string[NULL_LEN]

        return None, string

    def lex(self, string):
        """
        Method that parse a given string and return a list containing all the tokens of that list
        :param string: The string that we are going to parse
        :return: A list containing all the tokens founded in the string.
        :exception Raise an exception if an unexpected character was found
        """
        # We start parsing the string and break it into tokens
        tokens = []
        # Until the string is done we parse it
        while len(string):
            logging.info('Start the breaking into token process')
            # we try to figure out if it is a string
            json_string, string = self.lex_string(string)
            # if json_string is None that means that that char wasn't a string and we move on, and if it is not None, we
            # add it to the tokens cause it means we found a new element
            if json_string is not None:
                tokens.append(json_string)
                # restart the loop
                continue
            # we try to figure out if it is a number
            json_number, string = self.lex_number(string)
            # is json_number is None that means that we didn't find a number and we continue to search, if it is not
            # None that means we found a number and we append it to the list of tokens
            if json_number is not None:
                tokens.append(json_number)
                continue
            # we try to figure out if it is a bool
            json_bool, string = self.lex_bool(string)
            # if it is a bool we add it to the tokens else we continue
            if json_bool is not None:
                tokens.append(json_bool)
                continue
            # we try to figure out if it is a null variable
            json_null, string = self.lex_null(string)
            # if it is a null value we add it into the tokens else we continue
            if json_null is not None:
                tokens.append(None)
                continue
            # we take the next character
            c = string[0]

            if c in JSON_WHITESPACE:
                # Ignore whitespace
                string = string[1:]
            elif c in JSON_SYNTAX:
                # we check if it is one of the characters { } [ ] , : and if it is we append to the tokens
                tokens.append(c)
                string = string[1:]
            else:
                # if it wasn't any of the above we raise an error
                logging.error("Unexpected character: {}".format(c))
                raise Exception('Unexpected character: {}'.format(c))

        return tokens

    def parse_array(self, tokens):
        """
        Parse all the tokens between the [ ] symbols and create a list with them and return it
        :param tokens: The list with all the tokens
        :return: The function will return a pair containing a list and the rest of the tokens
        :except: - Expected comma after object in array
                 - Expected end-of-array bracket
        """
        # The list that will be returned
        json_array = []
        # take the first token
        t = tokens[0]
        # if it is a ] that we will return the list and the rest of the tokens
        if t == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]
        # while true we keep on searching for the ]
        while True:
            # we check if there isn't any other object, array or dictionary
            json, tokens = self.parse(tokens)
            # we append the result from the parse function
            json_array.append(json)

            # we take the next value from the tokens list
            t = tokens[0]
            # if it is a ] then we return
            if t == JSON_RIGHTBRACKET:
                return json_array, tokens[1:]
            # if it isn't a comma we raise an exception
            elif t != JSON_COMMA:
                logging.error('Expected comma after object in array')
                raise Exception('Expected comma after object in array')
            else:
                # we update the tokens list to skip the first value
                tokens = tokens[1:]

        # there isn't any ] so we raise an exception
        logging.error('Expected end-of-array bracket')
        raise Exception('Expected end-of-array bracket')

    def parse_object(self, tokens):
        """
        Parse all the tokens between the { } symbols and create a dictionary with them and return it
        :param tokens: The list with all the tokens
        :return: The function will return a pair containing a dictionary and the rest of the tokens
        :except: - Expected string key, got something else
                 - Expected colon after key in object, got something else
                 - Expected comma after pair in object, got something else
                 - Expected end-of-object bracket
        """
        # create the dictionary that is going to be returned
        json_object = {}

        # we take the first value from the tokens list
        t = tokens[0]
        # if the element is } then we finish the execution of the function and return
        if t == JSON_RIGHTBRACE:
            return json_object, tokens[1:]

        # while True we keep on searching for the }
        while True:
            # we take the first value from the tokens list
            json_key = tokens[0]
            # if the token is a string we update the token list and move on
            if type(json_key) is str:
                tokens = tokens[1:]
            else:
                # raise an error if the token isn't a string
                logging.error('Expected string key, got: {}'.format(json_key))
                raise Exception('Expected string key, got: {}'.format(json_key))

            # if there isn't a comma after the key raise an error
            if tokens[0] != JSON_COLON:
                logging.error('Expected colon after key in object, got: {}'.format(t))
                raise Exception('Expected colon after key in object, got: {}'.format(t))
            # take the next token which will be the value
            json_value, tokens = self.parse(tokens[1:])
            # in the result dictionary add the pair key, value
            json_object[json_key] = json_value

            # take the next token from the tokens list
            t = tokens[0]
            # if it is a } than we return the dictionary and the remaining of the tokens list
            if t == JSON_RIGHTBRACE:
                return json_object, tokens[1:]
            # after a key value pair we expect a comma if it isn't found one we will raise an error
            elif t != JSON_COMMA:
                logging.error('Expected comma after pair in object, got: {}'.format(t))
                raise Exception('Expected comma after pair in object, got: {}'.format(t))
            # update the tokens list to skip the first element
            tokens = tokens[1:]

        # raise an exception it we didn't found a }
        logging.error('Expected end-of-object bracket')
        raise Exception('Expected end-of-object bracket')

    def parse(self, tokens, is_root=False):
        """
        The method will parse through the token list and decide if the token is an object or a list or a dictionary and
        call the specific function for each
        :param tokens: if the tokens list
        :param is_root: flag that specify if the current token is root or not
        :return: the object
        :except: - Root must be an object
        """
        # we take the first token
        t = tokens[0]

        # Json always starts with a {
        if is_root and t != JSON_LEFTBRACE:
            logging.error('Root must be an object')
            raise Exception('Root must be an object')
        # if the token is a { then we parse the array
        if t == JSON_LEFTBRACKET:
            return self.parse_array(tokens[1:])
        # else we parse the object
        elif t == JSON_LEFTBRACE:
            return self.parse_object(tokens[1:])
        else:
            return t, tokens[1:]

    def loads(self, string):
        """
        Function check if the string given is a json or it is a file in which the json is.
        :param string: The given string
        :return: a object representing the json
        """
        # here we check if the string that we receive is a text file or a usual string
        log.info("Start the loads process")
        if '.txt' in string:
            return self.from_file(string)
        else:
            return self.from_string(string)

    def from_string(self, string):
        """
        The method will call functions for parsing the string and constructing the object
        :param string: The given string
        :return: an object representing the json
        """
        log.info("Loads the string %s" % string)
        tokens = self.lex(string)
        return self.parse(tokens, is_root=True)[0]

    def from_file(self, filename):
        """
        The method will open the file and read from it and call function for parsing the string and constructing
        the object
        :param filename: The given file fro which we will read the json
        :return: an object representing the json
        """
        f = open(filename, 'r')
        string = f.read()
        log.info("Loads the string %s from the file %s" % (string, filename))
        tokens = self.lex(string)
        return self.parse(tokens, is_root=True)[0]
