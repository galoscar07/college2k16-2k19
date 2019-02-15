import json
import logging

log = logging.getLogger('logger')


class JsonSerializer:
    """
    Class that will receive an object in order to serialize as a JSON formatted stream

    Attributes:
        None attributes are required in order to initialize the class

    Methods:
        __init__ - constructor of the class
        dump - method that will serialize the object
        to_json - method that will format a class to be able to be json-ed
        dumper - Function that will create the json with the build in function. if it isn't possible to create it with
                 the standard library it will return the object attributes as a dictionary
    """
    def __init__(self):
        """
        The constructor of the class
        """
        pass

    def dump(self, obj):
        """
        The function that will actually serialize objects
        :param obj: the given object
        :return: a string JSON formatted
        """
        try:
            json_to_be_returned = json.dumps(obj, default=self.dumper, indent=2)
            return json_to_be_returned
        except Exception as e:
            logging.error(e)

    def to_json(self):
        """
        Format a class to be able to be json-ed
        :return: A json containing the data
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def dumper(obj):
        """
        Function that will create the json with the build in function. if it isn't possible to create it with the
        standard library it will return the object attributes as a dictionary
        :param obj: the object that will be serialized
        :return: the serialized object
        """
        try:
            return obj.to_json()
        except AttributeError:
            logging.warning('Something went wrong and it will return the elements as a dictionary')
            return obj.__dict__
