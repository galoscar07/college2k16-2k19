"""
@author: radu


"""


class StatisticsController(object):
    def __init__(self, product_repository, order_repository):
        self.__product_repository = product_repository
        self.__order_repository = order_repository

    def compute_all_orders_cost(self):
        cost, all_orders = 0, self.__order_repository.get_all()
        for o in all_orders:
            product = self.__product_repository.find_by_id(o.product_id)
            cost = cost + product.price * o.quantity
        return cost
