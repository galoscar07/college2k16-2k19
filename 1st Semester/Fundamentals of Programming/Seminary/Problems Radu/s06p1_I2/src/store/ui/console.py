"""
@author: radu


"""
import traceback

from store.domain.validators import StoreException
from util.common import MyUtil


class Console(object):
    def __init__(self, product_controller):
        self.__product_controller = product_controller

    def run_console(self):
        # TODO implement an menu or cmd based console

        self.__add_products()

        print("all products:")
        self.__print_all_products()

        print("products filtered by name (name containing the string 'p'):")
        MyUtil.print_list(self.__product_controller.filter_products_by_name("p"))

    def __print_all_products(self):
        MyUtil.print_list(self.__product_controller.get_all())

    def __add_products(self):
        try:
            self.__product_controller.add_product(1, "p1", 100)
            self.__product_controller.add_product(2, "p2", 200)
            self.__product_controller.add_product(3, "bla", 300)
        except StoreException as se:
            print("exception when adding products: ", se)
            traceback.print_exc()
