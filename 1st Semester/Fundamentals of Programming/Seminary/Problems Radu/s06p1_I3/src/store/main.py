"""
@author: radu

ProductStore

Write an application that manages the products and orders from a product store.
Product (product_id, name, price)
Order (order_id, product_id, quantity)

The application should allow to:

F1: add new products
F2: delete products
F3: update products
F4: print all products

F5: make an order
F6: delete an order
F7: update an order
F8: print all orders

F9: filter products (e.g: print all products whose name contain a given string)

F10: compute the cost of all orders
F11: filter orders (e.g:return all orders (crt., product name, quantity, cost) with the cost greater than 2)

F12_: validators and exceptions (ProductValidator)

F13_: class Order with properties

F14_: file repository

F15: find the product that was ordered most times.

F16: sort orders (product name, quantity, cost) descending after the cost (i.e., order cost) and alphabetically
after product name.

F17_: add __eq__ and __ne__
F18_: use validators (ProductValidator)

F19_: unittest

----------------------------------------------------------------------------------------------
I1: F1, F4
I2: F12_, F17_, F18_, F9
I3: F13_, F5, F8

I4: F10

I5: F11
I6: F15
I7: F16
I8: F19_
I9: F14_
I10: F2, F3, F6, F7
"""
import traceback

from controller.order_controller import OrderController
from controller.product_controller import ProductController
from domain.validators import ProductValidator, OrderValidator
from repository.repo import Repository
from ui.console import Console

if __name__ == "__main__":
    try:
        product_repository = Repository(ProductValidator)
        product_controller = ProductController(product_repository)

        order_repository=Repository(OrderValidator)
        order_controller=OrderController(order_repository, product_repository)

        console = Console(product_controller, order_controller)

        console.run_console()

    except Exception as ex:
        print("exception: ", ex)
        traceback.print_exc()

    print("bye")
