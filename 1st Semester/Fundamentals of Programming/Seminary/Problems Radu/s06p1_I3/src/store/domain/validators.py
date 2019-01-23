"""
@author: radu


"""


class StoreException(Exception):
    pass


class ProductValidatorException(StoreException):
    pass


class ProductValidator(object):
    @staticmethod
    def validate(product):
        if not type(product.entity_id) is int:
            raise ProductValidatorException("id must be an int")

            # TODO other validations


class OrderValidatorException(StoreException):
    pass


class OrderValidator(object):
    @staticmethod
    def validate(order):
        if not type(order.quantity) is int or order.quantity < 0:
            raise OrderValidatorException("quantity must be an integer greater or equal to 0")

            # TODO other validations
