from parser import JsonParser
from serializer import JsonSerializer
"""
Design and implement a simple JSON parser and serializer (basic support, may be limited to non-negative integers up to 
2^31, strings with ASCII only characters and no escape sequences, null, true, false, lists and objects; alternatively, 
take another similar small project). However, make it able to work with either strings or files.

Create the classes and functions in accordance with Single Responsibility Principle (SRP). Discuss possible choices.
Choose good names (clear and in accordance with usual library styles). Discuss alternative names.
Identify and document corner cases.
"""


class MyClass(object):
    def __init__(self):
        self.string = 'asd'
        self.dictionary = {'asd': 123, 'a': 'asd'}
        self.list = [1, 2, 3]


if __name__ == '__main__':
    print('Parser')
    parser = JsonParser()
    print('Parse From String')
    parse_from_string = parser.loads('{"foo":{"bar":[1,2,3]}}')
    print(type(parse_from_string))
    print(parse_from_string)

    print('Parse From File')
    parse_from_file = parser.loads('example_json.txt')
    print(type(parse_from_file))
    print(parse_from_file)

    print('Serializer')
    my_class = MyClass()
    serializer = JsonSerializer()
    print('Example dict')
    print(serializer.dump({'asd': 123, 'ana': {'asd': 'asd', 'myclass': my_class}, 'ce': 1, 'list': [1, 2, 3]}))
    print('Example list')
    print(serializer.dump(['asd', 1, 2, 3, 'aaaa', my_class, {'asd': 'asd'}]))
    print('Example int')
    print(serializer.dump(1))
    print('Example str')
    print(serializer.dump('Ana are mere'))
    print('Example class')
    print(serializer.dump(my_class))
    print('Example bool')
    print(serializer.dump(True))
    print('Example null')
    print(serializer.dump(None))
