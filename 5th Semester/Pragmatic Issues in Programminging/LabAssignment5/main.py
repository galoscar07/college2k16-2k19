import logging

from parser import JsonParser
from serializer import JsonSerializer
from snippet_app import SnippetApp

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
    logging.basicConfig(filename='LabAssignment4.log', level=logging.INFO)

    app = SnippetApp('/Users/galoscar/Documents/University&Shits/Pragmatic Issues in Programming/'
                     'LabAssignment5/pythonsqlite.db')
    app.run_app()
