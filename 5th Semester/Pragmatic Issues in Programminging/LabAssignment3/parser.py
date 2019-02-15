JSON_COMMA = ','
JSON_COLON = ':'
JSON_LEFTBRACKET = '['
JSON_RIGHTBRACKET = ']'
JSON_LEFTBRACE = '{'
JSON_RIGHTBRACE = '}'
JSON_QUOTE = '"'
JSON_WHITESPACE = [' ']
JSON_SYNTAX = [JSON_COMMA, JSON_COLON, JSON_LEFTBRACKET, JSON_RIGHTBRACKET,
               JSON_LEFTBRACE, JSON_RIGHTBRACE]

FALSE_LEN = len('false')
TRUE_LEN = len('true')
NULL_LEN = len('null')


class JsonParser(object):
    def __init__(self):
        pass

    @staticmethod
    def lex_string(string):
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
        # If we didn't stop until the string is done the last quote i missing
        raise Exception('Expected end-of-string quote')

    @staticmethod
    def lex_number(string):
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
        # we keep the same logic as above but now instead of true or false we use the null variable
        string_len = len(string)

        if string_len >= NULL_LEN and \
                string[:NULL_LEN] == 'null':
            return True, string[NULL_LEN]

        return None, string

    def lex(self, string):
        # We start parsing the string and break it into tokens
        tokens = []
        # Until the string is done we parse it
        while len(string):
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
                raise Exception('Unexpected character: {}'.format(c))

        return tokens

    def parse_array(self, tokens):
        json_array = []

        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]

        while True:
            json, tokens = self.parse(tokens)
            json_array.append(json)

            t = tokens[0]
            if t == JSON_RIGHTBRACKET:
                return json_array, tokens[1:]
            elif t != JSON_COMMA:
                raise Exception('Expected comma after object in array')
            else:
                tokens = tokens[1:]

        raise Exception('Expected end-of-array bracket')

    def parse_object(self, tokens):
        json_object = {}

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            return json_object, tokens[1:]

        while True:
            json_key = tokens[0]
            if type(json_key) is str:
                tokens = tokens[1:]
            else:
                raise Exception('Expected string key, got: {}'.format(json_key))

            if tokens[0] != JSON_COLON:
                raise Exception('Expected colon after key in object, got: {}'.format(t))

            json_value, tokens = self.parse(tokens[1:])

            json_object[json_key] = json_value

            t = tokens[0]
            if t == JSON_RIGHTBRACE:
                return json_object, tokens[1:]
            elif t != JSON_COMMA:
                raise Exception('Expected comma after pair in object, got: {}'.format(t))

            tokens = tokens[1:]

        raise Exception('Expected end-of-object bracket')

    def parse(self, tokens, is_root=False):
        # we take the first token
        t = tokens[0]

        if is_root and t != JSON_LEFTBRACE:
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
        # here we check if the string that we receive is a text file or a usual string
        if '.txt' in string:
            return self.from_file(string)
        else:
            return self.from_string(string)

    def from_string(self, string):
        tokens = self.lex(string)
        return self.parse(tokens, is_root=True)[0]

    def from_file(self, filename):
        f = open(filename, 'r')
        string = f.read()
        tokens = self.lex(string)
        return self.parse(tokens, is_root=True)[0]