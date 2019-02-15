class StoreException(Exception):
    pass

class ChocolateValidatorException(StoreException):
    pass

class ChocolateValidators(object):

    @staticmethod
    def validator(chocolate):
        if not type(chocolate.entityId) is int:
            raise ChocolateValidatorException("Id must be an int")
        if chocolate.quant < 0:
            raise ChocolateValidatorException("Quant must not be smaller than 0")