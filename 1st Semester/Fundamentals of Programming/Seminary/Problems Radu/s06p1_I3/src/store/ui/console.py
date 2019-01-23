"""
@author: radu


"""
import traceback

from domain.validators import StoreException
import MyUtil


class Console(object):
    def __init__(self, product_controller, order_controller):
        self.__product_controller = product_controller
        self.__order_controller = order_controller

    def run_console(self):
        # TODO implement an menu or cmd based console

        self.__init_data()

        print("all products:")
        self.__print_all_products()

        print("all orders:")
        self.__print_all_orders()

        print("products filtered by name (name containing the string 'p'):")
        MyUtil.print_list(self.__product_controller.filter_products_by_name("p"))

    def __print_all_products(self):
        MyUtil.print_list(self.__product_controller.get_all())

    def __print_all_orders(self):
        MyUtil.print_list(self.__order_controller.get_all())

    def __init_data(self):
        try:
            self.__product_controller.add_product(1, "p1", 100)
            self.__product_controller.add_product(2, "p2", 200)
            self.__product_controller.add_product(3, "bla", 300)

            self.__order_controller.add_order(1, 1, 2)
            self.__order_controller.add_order(2, 1, 3)
            self.__order_controller.add_order(3, 2, 4)

        except StoreException as se:
            print("exception when initializing data: ", se)
            traceback.print_exc()
