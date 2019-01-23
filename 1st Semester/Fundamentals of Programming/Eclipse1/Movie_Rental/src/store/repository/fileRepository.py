"""
from src.store.domain.entities import Client
from src.store.repository.repository import Repository


class ClientFileRepository(Repository):
    def __init__(self, validator_class, file_name):
        super().__init__(validator_class)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        # TODO handle exceptions - file not found, corrupted file etc.
        with open(self.__file_name) as f:
            for line in f:
                # there is one product/line, the attributes are separated by comas.
                attributes = line.split(",")
                client = Client(int(attributes[0]), attributes[1])
                super().save(client)

    def save(self, client):
        super().save(client)

        self.__save_to_file(client)

    def __save_to_file(self, client):
        with open(self.__file_name, "a") as f:
            f.write("\n" + str(client.entity_id) + "," + client.name)

class OrderFileRepository(Repository):
    pass

"""