import sqlite3

from parser import JsonParser
from serializer import JsonSerializer

"""
Example to test:
1
'{"DTLE":{"bar":[1,2,3]}}'
'{"a": "); drop table user; --"}'
"""


class SnippetApp(object):
    """
    Class that will run the menu for the mini-app that we have

    Attributes:
        filename - is the file name where the database is stored

    Methods:
        __init__ - Constructor for the class, it will initialize the parser and the serializer, it will also save the
                   save the file name as a attribute and will initialize a class variable conn as a None value
        create_connection - Method that will create the connection with the database
        create_table_snippets - Method that will create the table for the database
        _menu - Function that created the menu to be printed
        run_app - Function that will keep the application alive
        add_to_database - Function that wll prove the functionality for the serializer and the parser and will also save
                          into the database a string representing the json
        save_in_the_database - The function that will actually save into the database
        print_all_from_database - Function that will return a list with all the elements from the database
    """
    def __init__(self, filename):
        """
        Constructor for the class, it will initialize the parser and the serializer, it will also save the
                   save the file name as a attribute and will initialize a class variable conn as a None value
        :param filename: The name of the file where the database is stored
        """
        self.filename = filename
        self.parser = JsonParser()
        self.serializer = JsonSerializer()
        self.conn = None

    def create_connection(self):
        """
        Method that will create the connection with the database
        :return: The connector or None if there were any errors
        """
        try:
            conn = sqlite3.connect(self.filename)
            conn.isolation_level = None
            return conn
        except sqlite3.Error as e:
            print(e)

        return None

    def create_table_snippets(self):
        """
        Method that will create the table for the database
        :return: nothing
        """
        try:
            sql = 'CREATE TABLE snippets ( snippet_id integer PRIMARY KEY, string text NOT NULL);'
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except sqlite3.OperationalError:
            pass

    @staticmethod
    def _menu():
        """
        Function that created the menu to be printed
        :return: a string representing the menu from the app
        """
        string = "1. Add a new snippet to the database\n"
        string += "2. Print all the data from the database\n"
        string += "0. Exit\n"
        return string

    def run_app(self):
        """
        Function that will keep the application alive
        :return: nothing
        """
        try:
            self.conn = self.create_connection()
            self.create_table_snippets()
        except Exception as e:
            print("Something went wrong when connecting to database")

        while True:
            try:
                print(self._menu())
                keyboard_input = input("Please tell me what to do: ")
                try:
                    keyboard_input = int(keyboard_input)
                except ValueError:
                    print('Please enter only correct values!')
                if keyboard_input == 0:
                    break
                elif keyboard_input == 1:
                    self.add_to_database()
                elif keyboard_input == 2:
                    print(self.print_all_from_database())
                else:
                    print('Not a correct value. Please enter only correct values!')
                    continue
            except Exception as e:
                print(e)

    def add_to_database(self):
        """
        Function that wll prove the functionality for the serializer and the parser and will also save
                          into the database a string representing the json
        :return: nothing
        """
        print('Give me a string from the keyboard; I will parse it and then the parse result I will serialize it and '
              'save the string in the database.\n')
        keyboard_input = str(input("Give me the string: "))
        saved_string = keyboard_input
        print('Parser:\n')
        result = self.parser.loads(keyboard_input)
        print("The result type is: %s; and the actual result is: %s" % (type(result), result))
        print('Serializer')
        result = self.serializer.dump(result)
        print("The result type is: %s; and the actual result is: %s" % (type(result), result))
        print('Now saving in the database ...')
        self.save_in_the_database(saved_string)
        print('Saved!')

    def save_in_the_database(self, string_to_be_saved):
        """
        The function that will actually save into the database
        :param string_to_be_saved: The string that will be saved into the database
        :return: the id of the last row edited
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('BEGIN')
            # Due to this way of saving into the database there can't be any sql injections
            cursor.execute('INSERT INTO snippets(string) VALUES (?)', [string_to_be_saved])
            cursor.execute('COMMIT')
        except sqlite3.Error as e:
            raise Exception(e)

    def print_all_from_database(self):
        """
        Function that will return a list with all the elements from the database
        :return: a list with all the elements in the database
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute('BEGIN')
            cursor.execute('SELECT * FROM snippets;')
            list = cursor.fetchall()
            cursor.execute('COMMIT')
        except sqlite3.Error as e:
            raise Exception(e)

        return list
