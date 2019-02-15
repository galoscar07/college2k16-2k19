import logging
import operator
import types
path = []
path_list = []

# set up the logger
log = logging.getLogger("logger")


class JsonSerializer:
    """
    Class that will receive an object in order to serialize as a JSON formatted stream

    Attributes:
        None attributes are required in order to initialize the class

    Methods:
        parse_dict: Recursive method that will parse a dictionary in depth; in case there is a nested dictionary
        parse_list: Recursive method that will parse a list in depth; in case there is a nested dictionary
        get_by_path: Access a nested object in root by item sequence.
        set_by_path: Set a value in a nested object in root by item sequence.
        serialize_dict: Return the dictionary as a string
        serialize_list: Return the list as a string
        serialize_int: Return the number as a string, also validating the number with the specific conditions
        serialize_str: Returns the string as a string after it has been validated with the specific conditions
        serialize_bool: Return the bool variable as a string
        serialize_none: Return a string value representing the None value
        serialize_class: Return a string containing the attributes of the specific class
        dump: The function that will actually serialize objects
    """
    def __init__(self):
        self.final_result = None

    def parse_dict(self, dictionary, final_dictionary):
        """
        Recursive method that will parse a dictionary in depth; in case there is a nested dictionary
        :param dictionary: The dictionary that we will parse
        :param final_dictionary: The dictionary that will be returned after values in it will be serialized
        :return: Nothing
        """
        # global variable path in which we will remember the path to the element that we currently are
        global path
        # parse items (key, value) from the dictionary
        for key, value in dictionary.items():
            # if the current value is a string
            if isinstance(value, str):
                # add the current key to the path list
                path.append(key)
                # serialize the str object
                new_value = self.serialize_str(value)
                # add it to the final dictionary
                self.set_by_path(final_dictionary, path, new_value)
                # pop the key from the path list
                path.pop()
            # if the current value is an int
            elif isinstance(value, int):
                # add the current key to the path list
                path.append(key)
                # serialize the int object
                new_value = self.serialize_number(value)
                # add it to the final dictionary
                self.set_by_path(final_dictionary, path, new_value)
                # pop the key from the path list
                path.pop()
            # if the current value is a bool
            elif isinstance(value, bool):
                # add the current key to the path list
                path.append(key)
                # serialize the bool value
                new_value = self.serialize_bool(value)
                # add it to the final dictionary
                self.set_by_path(final_dictionary, path, new_value)
                # pop the key from the path list
                path.pop()
            # if the current value is a None
            elif isinstance(value, types.NoneType):
                # add the current key to the path list
                path.append(key)
                # serialize the none value
                new_value = self.serialize_none()
                # add it to the final dictionary
                self.set_by_path(final_dictionary, path, new_value)
                # pop the key from the path list
                path.pop()
            # if the current value is a list
            elif isinstance(value, list):
                # add the current key to the path list
                path.append(key)
                new_list = value
                # serialize the bool value
                self.parse_list(value, new_list)
                # add it to the final dictionary
                self.set_by_path(final_dictionary, path, new_list)
                # pop the key from the path list
                path.pop()
            # if the current value is a dict
            elif isinstance(value, dict):
                # add the current key to the path list
                path.append(key)
                # parse the new dictionary
                self.parse_dict(value, final_dictionary)
                # pop the key from the path list
                path.pop()
            # if the current value is an object
            elif isinstance(value, object):
                # add the current key to the path list
                path.append(key)
                # serialize the object
                new_value = self.serialize_class(value).replace('"{', '{').replace('}"', '}')\
                    .replace("'[", '[').replace("]'", ']')
                # add it to the final dictionary
                self.set_by_path(final_dictionary, path, new_value)
                # pop the key from the path list
                path.pop()

    def parse_list(self, list_to_parse, final_list):
        """
        Recursive method that will parse a list in depth; in case there is a nested dictionary
        :param list_to_parse: the list that will be parsed
        :param final_list: the result list with the object from the list serialized
        :return: Nothing
        """
        # global variable that will remember the path to the current element in the list
        global path_list
        # variable to know on which element we are
        count = 0
        # parse the elements in the list
        for elem in list_to_parse:
            # if the current value is a string
            if isinstance(elem, str):
                # add the current position to the path list
                path_list.append(count)
                # serialize the string
                new_value = self.serialize_str(elem)
                # add it to the final list
                self.set_by_path(final_list, path_list, new_value)
                # pop the key from the path list
                path_list.pop()
            # if the current value is an int
            elif isinstance(elem, int):
                # add the current position to the path list
                path_list.append(count)
                # serialize the int
                new_value = self.serialize_number(elem)
                # add it to the final list
                self.set_by_path(final_list, path_list, new_value)
                # pop the key from the path list
                path_list.pop()
            # if the current value is a bool
            elif isinstance(elem, bool):
                # add the current position to the path list
                path_list.append(count)
                # serialize the bool value
                new_value = self.serialize_bool(elem)
                # add it to the final list
                self.set_by_path(final_list, path_list, new_value)
                # pop the key from the path list
                path_list.pop()
            # if the current value is None
            elif isinstance(elem, types.NoneType):
                # add the current position to the path list
                path_list.append(count)
                # serialize the None
                new_value = self.serialize_none()
                # add it to the final list
                self.set_by_path(final_list, path_list, new_value)
                # pop the key from the path list
                path_list.pop()
            # if the current value is a dict
            elif isinstance(elem, dict):
                # add the current position to the path list
                path_list.append(count)
                # create a new dictionary with the same values
                new_dict = elem
                # parse the dictionary in depth
                self.parse_dict(elem, new_dict)
                # make the changes in the current dictionary
                self.set_by_path(final_list, path_list, new_dict)
                # pop the key from the path list
                path_list.pop()
            # if the current value is a list
            elif isinstance(elem, list):
                # add the current position to the path list
                path.append(count)
                # serialize the list by parsing it in depth
                self.parse_list(elem, final_list)
                # pop the key from the path list
                path.pop()
            # if the current value is an object
            elif isinstance(elem, object):
                # add the current position to the path list
                path_list.append(count)
                # serialize the object
                new_value = self.serialize_class(elem)
                # add it to the final list
                self.set_by_path(final_list, path_list, new_value)
                # pop the key from the path list
                path_list.pop()
            # increase the value of the counting variable
            count += 1

    @staticmethod
    def get_by_path(root, items):
        """
        Access a nested object in root by item sequence.
        :param root: The object in which we will search
        :param items: The path to the location of the value
        :return: The value at the specific path
        """
        return reduce(operator.getitem, items, root)

    def set_by_path(self, root, items, value):
        """
        Set a value in a nested object in root by item sequence.
        :param root: The object in which we will make the change
        :param items: The path to the location of the value
        :param value: The new value of the element at the specific position
        :return: nothing
        """
        logging.warning('Could break index out of range')
        self.get_by_path(root, items[:-1])[items[-1]] = value

    @staticmethod
    def serialize_dict(obj):
        """
        Return the dictionary as a string
        :param obj: The given dictionary
        :return: a string representing the dictionary
        """
        return str(obj)

    @staticmethod
    def serialize_list(obj):
        """
        Return the list as a string
        :param obj: The given dictionary
        :return: a string representing the list
        """
        return str(obj)

    @staticmethod
    def serialize_number(obj):
        """
        Return the number as a string, also validating the number with the specific conditions
        :param obj: The given number
        :return: The number as a string
        :except: - Float is not permitted
                 - Negative number not supported
                 - Number can not be higher than grater than 2^31
        """
        # first we check if it is a float and if it is raise an error
        if type(obj) is float:
            logging.error('Float is not permitted')
            raise Exception('Float is not permitted')
        # check if the number is smaller than 0 and if it is raise an error
        elif obj < 0:
            logging.error('Negative number not supported')
            raise Exception('Negative number not supported')
        # check if the number is grater that 2^31 and if it is raise an error
        elif obj > pow(2, 31):
            logging.error('Number can not be higher than grater than 2^31')
            raise Exception('Number can not be higher than grater than 2^31')
        return obj

    @staticmethod
    def serialize_str(obj):
        """
        Returns the string as a string after it has been validated with the specific conditions
        :param obj: the string as a string
        :return: a string
        :except: - Can not enter non ascii characters
        """
        # check if the string contains non ascii characters and if it does raise an error
        if not all(ord(char) < 128 for char in obj):
            logging.error('Can not enter non ascii characters')
            raise Exception('Can not enter non ascii characters')
        return str(obj)

    @staticmethod
    def serialize_bool(obj):
        """
        Return the bool variable as a string
        :param obj: the bool value
        :return: a string representing the bool value
        """
        # change the bool to look like the ones in a JSON
        return str(obj).replace('T', 't').replace('F', 'f')

    @staticmethod
    def serialize_none():
        """
        Return a string value representing the None value
        :return: a string representing the specific JSON variable for a None case
        """
        return 'null'

    def serialize_class(self, obj):
        """
        Return a string containing the attributes of the specific class
        :param obj: if a class
        :return: a string having the key and value of all the attribute of the class
        """
        # the dictionary containing (name_of_the_attributes, value)
        result = obj.__dict__
        # go through every pair
        for key, value in result.items():
            # if the pair value is a dict then sanitize it
            if isinstance(value, dict):
                result[key] = self.serialize_dict(value)
            # if the pair value is a list then sanitize it
            elif isinstance(value, list):
                result[key] = self.serialize_list(value)
            # if the pair value is a str then sanitize it
            elif isinstance(value, str):
                result[key] = self.serialize_str(value)
            # if the pair value is a number then sanitize it
            elif isinstance(value, int):
                result[key] = self.serialize_number(value)
            # if the pair value is a None then sanitize it
            elif isinstance(value, types.NoneType):
                result[key] = self.serialize_none()
            # if the pair value is a bool then sanitize it
            elif isinstance(value, bool):
                result[key] = self.serialize_bool(value)
        # return a string
        return str(result)

    def dump(self, obj):
        """
        The function that will actually serialize objects
        :param obj: the given object
        :return: a string JSON formatted
        """
        logging.info('Start the dump process by deciding what type of object it is')
        # if the object is a dict then call the parsing of the dict method
        if isinstance(obj, dict):
            self.final_result = obj
            self.parse_dict(obj, self.final_result)
            self.final_result = self.serialize_dict(self.final_result)
            return self.final_result.replace('"{', '{').replace('}"', '}').replace("'[", '[').replace("]'", ']')
        # if the object is a list then call the parsing of the list method
        if isinstance(obj, list):
            self.final_result = obj
            self.parse_list(obj, self.final_result)
            self.final_result = self.serialize_list(self.final_result)
            return self.final_result.replace('\\', '')
        # if the object is a int then call the parsing of the int method
        if isinstance(obj, int):
            return self.serialize_number(obj)
        # if the object is a dict str call the parsing of the str method
        if isinstance(obj, str):
            return self.serialize_str(obj)
        # if the object is a bool then call the parsing of the bool method
        if isinstance(obj, bool):
            return self.serialize_bool(obj)
        # if the object is a None then call the parsing of the None method
        if obj is None:
            return self.serialize_none()
        # if the object is a class then call the parsing of the class method
        if isinstance(obj, object):
            return self.serialize_class(obj)