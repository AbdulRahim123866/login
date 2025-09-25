# # Library: Employees, Clients, Books, Seats/Tables, Orders, Pyments, Discounts
# from datetime import datetime
#
#
# # Employee: id, name, surname, email, phone, address, salary, role, status
# # Client: id, name, surname, email, phone, address, status
# # Book: id, title, author, price, quantity, status
# # Seat/Table: id, number, status
# # Order: id, client_id, book_id, quantity, price, status
# # Payment: id, client_id, order_id, amount, status
# # Discount: id, client_id, order_id, percentage, status
#
# # Controller: Commounication between the library objects
# # main module
#
# class BaseClass:
#     def __init__(self):
#         self._created_at: datetime = datetime.now()
#         self._updated_at: datetime = None
#         self._removed_at: datetime = None # soft remove
#
#         pass
#
#     # def __str__(self):
#     #     pass
#     #
#     # def __repr__(self):
#     #     pass
#
#     pass
#
# print(isinstance(A, object))
# print(issubclass(A, object))
#
# #
# # def main():
# #     if seat.status == SeatsStatus.AVAILABLE:
# #         print('Seat is available')
# #     else:
# #         print('Seat is not available')
# #
# #     pass
# #
# #
# #
# # if __name__ == '__main__':
# #     main()
#
from control.controller import Library
from models.persona import Client

# import views
# import numpy

# print(vars(views))
import sys
print(sys.path)
sys.path.append("")


if __name__ == '__main__':
    lib = Library()
    user1 = Client(_id="asf51", name="Mohammad Dada", surname="AbuDa", email="ahmad.852@gmail.com", phone="079852258552", address="", status="vip")
    # user2 = Client(_id="asf51", name="Mohammad Dada", surname="AbuDa", email="ahmad.852@gmail.com", phone="079852258552", address="", status="vip")
    # user3 = Client(_id="asf51", name="Mohammad Dada", surname="AbuDa", email="ahmad.852@gmail.com", phone="079852258552", address="", status="vip")
    # user4 = Client(_id="asf51", name="Mohammad Dada", surname="AbuDa", email="ahmad.852@gmail.com", phone="079852258552", address="", status="vip")

    print(user1.budget)
    print(lib.list_books())
    order = lib.place_order(user1, ["Book 1", "Book 2"])
    payment = lib.pay_for_order(order)
    user1.pay_for_order(payment)
    print(user1.budget)
