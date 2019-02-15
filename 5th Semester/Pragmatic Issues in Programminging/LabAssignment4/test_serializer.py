from unittest import TestCase
from serializer import JsonSerializer


class MyClass(object):
    def __init__(self):
        self.string = 'asd'
        self.dictionary = {'asd': 123, 'a': 'asd'}
        self.list = [1, 2, 3]


class TestSerializer(TestCase):
    """
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
    def setUp(self):
        self.serializer = JsonSerializer()
        self.my_class = MyClass

    def tests(self):
        string = """{'list': [1, 2, 3], 'ana': {'myclass': {'list': [1, 2, 3], 'string': 'asd', 'dictionary': {'a': 
                    'asd', 'asd': 123}}, 'asd': [2, 3, 4]}, 'ce': 1, 'asd': 123}"""
        self.assertEqual(
            self.serializer.dump(
                {'asd': 123, 'ana': {'asd': [2, 3, 4], 'myclass': self.my_class}, 'ce': 1, 'list': [1, 2, 3]}), string)

        string = """['asd', 1, 2, 3, 'aaaa', '{'list': '[1, 2, 3]', 'string': 'asd', 
                    'dictionary': "{'a': 'asd', 'asd': 123}"}', {'asd': 'asd'}]"""
        self.assertEqual(
            self.serializer.dump(['asd', 1, 2, 3, 'aaaa', self.my_class, {'asd': 'asd'}]), string)

        self.assertEqual(self.serializer.dump(1), 1)

        self.assertEqual(self.serializer.dump('Ana are mere'), 'Ana are mere')

        string = """{'list': '[1, 2, 3]', 'string': 'asd', 'dictionary': "{'a': 'asd', 'asd': 123}"}"""
        self.assertEqual(self.serializer.dump(self.my_class), string)

        self.assertEqual(self.serializer.dump(True), 'True')
        self.assertEqual(self.serializer.dump(None), 'None')
