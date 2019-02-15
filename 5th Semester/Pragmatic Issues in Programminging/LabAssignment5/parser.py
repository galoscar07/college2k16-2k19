import json
import logging

log = logging.getLogger('logger')


class JsonParser(object):
    """
        A class used to parse strings and returns a Json

        Attributes:
            None attributes are required in order to initialize the class

        Methods:
            __init__ - the default constructor
            loads - Function check if the string given is a json or it is a file in which the json is.
            from_string - The method will call functions for parsing the string and constructing the object
            from_file - The method will open the file and read from it and call function for parsing the string and
                        constructing the object

    """
    def __init__(self):
        """
        The default constructor
        """
        pass

    def loads(self, string):
        """
        Function check if the string given is a json or it is a file in which the json is.
        :param string: The given string
        :return: a object representing the json
        """
        # to make sure that all the operations have a strong exception guarantee we are going to have here a try except
        # Exception which will catch any exception
        try:
            if '.txt' in string:
                return self.from_file(string)
            else:
                return self.from_string(string)
        except Exception as e:
            log.error("An error has appeared: %s" % e)
            raise Exception(e)

    @staticmethod
    def from_string(string):
        """
        The method will call functions for parsing the string and constructing the object
        :param string: The given string
        :return: an object representing the json
        """
        # in order to complete this lab we are going to use the python lib json in which we have the function json.loads
        # which will automatically load a json from a string
        return json.loads(string)

    @staticmethod
    def from_file(filename):
        """
        The method will open the file and read from it and call function for parsing the string and constructing
        the object
        :param filename: The given file fro which we will read the json
        :return: an object representing the json
        """
        # in order to complete this lab we are going to use the python lib json in which we have the function json.loads
        # which will automatically load a json from a string
        f = open(filename, 'r')
        string = f.read()
        return json.loads(string)
