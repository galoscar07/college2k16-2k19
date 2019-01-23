class StoreException(Exception):
    """
    This will store all exceptions
    """
    pass

class PersonException(StoreException):
    """
    This will store all the exception of the persons
    """
    pass

class PersonValidatorException(object):
    """
    This will store all the exception of the persons
    """
    @staticmethod
    def validator(entity):
        if not entity.imunization == "nonvaccinated":
            raise PersonException


