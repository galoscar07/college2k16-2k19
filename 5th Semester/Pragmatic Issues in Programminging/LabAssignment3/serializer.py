import operator
import types
path = []
path_list = []


class JsonSerializer:
    def __init__(self):
        self.final_result = None

    def parse_dict(self, dictionary, final_dictionary):
        global path
        for key, value in dictionary.items():
            if isinstance(value, str):
                path.append(key)
                new_value = self.serialize_str(value)
                self.set_by_path(final_dictionary, path, new_value)
                path.pop()
            elif isinstance(value, int):
                path.append(key)
                new_value = self.serialize_int(value)
                self.set_by_path(final_dictionary, path, new_value)
                path.pop()
            elif isinstance(value, bool):
                path.append(key)
                new_value = self.serialize_bool(value)
                self.set_by_path(final_dictionary, path, new_value)
                path.pop()
            elif isinstance(value, types.NoneType):
                path.append(key)
                new_value = self.serialize_none()
                self.set_by_path(final_dictionary, path, new_value)
                path.pop()
            elif isinstance(value, list):
                path.append(key)
                new_value = self.serialize_list(value)
                self.set_by_path(final_dictionary, path, new_value)
                path.pop()
            elif isinstance(value, dict):
                path.append(key)
                self.parse_dict(value, final_dictionary)
                path.pop()
            else:
                path.append(key)
                new_value = self.serialize_class(value)
                self.set_by_path(final_dictionary, path, new_value)
                path.pop()

    def parse_list(self, list_to_parse, final_list):
        global path_list
        count = 0
        for elem in list_to_parse:
            if isinstance(elem, str):
                path_list.append(count)
                new_value = self.serialize_str(elem)
                self.set_by_path(final_list, path_list, new_value)
                path_list.pop()
            elif isinstance(elem, int):
                path_list.append(count)
                new_value = self.serialize_int(elem)
                self.set_by_path(final_list, path_list, new_value)
                path_list.pop()
            elif isinstance(elem, bool):
                path_list.append(count)
                new_value = self.serialize_bool(elem)
                self.set_by_path(final_list, path_list, new_value)
                path_list.pop()
            elif isinstance(elem, types.NoneType):
                path_list.append(count)
                new_value = self.serialize_none()
                self.set_by_path(final_list, path_list, new_value)
                path_list.pop()
            elif isinstance(elem, dict):
                path_list.append(count)
                new_dict = {}
                self.parse_dict(elem, new_dict)
                self.set_by_path(final_list, path_list, new_dict)
                path_list.pop()
            else:
                path_list.append(count)
                new_value = self.serialize_class(elem)
                self.set_by_path(final_list, path_list, new_value)
                path_list.pop()
            count += 1

    @staticmethod
    def get_by_path(root, items):
        """
        Access a nested object in root by item sequence.
        """
        return reduce(operator.getitem, items, root)

    def set_by_path(self, root, items, value):
        """
        Set a value in a nested object in root by item sequence.
        """
        self.get_by_path(root, items[:-1])[items[-1]] = value

    @staticmethod
    def serialize_dict(obj):
        return str(obj)

    @staticmethod
    def serialize_list(obj):
        return str(obj)

    @staticmethod
    def serialize_int(obj):
        return obj

    @staticmethod
    def serialize_str(obj):
        return str(obj)

    @staticmethod
    def serialize_bool(obj):
        return str(obj).replace('T', 't').replace('F', 'f')

    @staticmethod
    def serialize_none():
        return 'null'

    def serialize_class(self, obj):
        result = obj.__dict__
        for key, value in result.items():
            if isinstance(value, dict):
                result[key] = self.serialize_dict(value)
            elif isinstance(value, list):
                result[key] = self.serialize_list(value)
            elif isinstance(value, str):
                result[key] = self.serialize_str(value)
            elif isinstance(value, int):
                result[key] = self.serialize_int(value)
            elif isinstance(value, types.NoneType):
                result[key] = self.serialize_none()
            elif isinstance(value, bool):
                result[key] = self.serialize_bool(value)
        return result

    def dump(self, obj):
        if isinstance(obj, dict):
            self.final_result = obj
            self.parse_dict(obj, self.final_result)
            self.final_result = self.serialize_dict(self.final_result)
            return self.final_result
        if isinstance(obj, list):
            self.final_result = obj
            self.parse_list(obj, self.final_result)
            self.final_result = self.serialize_list(self.final_result)
            return self.final_result
        if isinstance(obj, int):
            return self.serialize_int(obj)
        if isinstance(obj, str):
            return self.serialize_str(obj)
        if isinstance(obj, bool):
            return self.serialize_bool(obj)
        if obj is None:
            return self.serialize_none()
        if isinstance(obj, object):
            return self.serialize_class(obj)