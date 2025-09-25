# library: Employee, client, book,seat/tables,orders,payments,discounts
from datetime import datetime
from constans import SeatsStatus


# Employee:id,name surname ,email ,phone ,address,salary,role,status
# client: id ,name,surname,email,address ,status
# Book: id, title  author  price  quantity  status
# seat/table: id  number  status
# order: id  client_id  book_id  amount  status
# payment : id  client_id , order_id  amount  status
# discount : id  client_id  order_id  percentage  status

# Controller: Communication between the library objects
# main module

class BaseClass:
    def __init__(self):
        self._created_at: datetime = datetime.now()
        self._updated_at: datetime = None
        self._removed_at: datetime = None  # soft remove
        pass


class Employee(BaseClass):
    def __init__(self, ID, name, surname, email, phone, address, salary, role, status):
        super().__init__()
        self.ID = ID
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.address = address
        self.salary = salary
        self.role = role
        self.status = status


class Client(Employee,BaseClass):

    def __init__(self, ID, name, surname, email, address, status):
        BaseClass.__init__(self)
        Employee.__init__(ID, name, surname, email, address, status)


class Book(BaseClass):
    def __init__(self, BID, title, author, price, quantity, status):
        BaseClass.__init__(self)
        self.BID = BID
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.status = status

    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return f" ({self.title})"
class Seat_Table(BaseClass):
    def __init__(self, ID, number, status):
        BaseClass.__init__(self)
        self.ID = ID
        self.number = number
        self.status = status


class Order(BaseClass):
    def __init__(self, ID, client_id, book_id, amount, status):
        BaseClass.__init__(self)
        self.ID = ID
        self.client_id = client_id
        self.book_id = book_id
        self.amount = amount
        self.status = status


class Payment(BaseClass):
    def __init__(self, ID, client_id, order_id, amount, status):
        BaseClass.__init__(self)
        self.ID = ID
        self.client_id = client_id
        self.oreder_id = order_id
        self.amount = amount
        self.status = status


class Discount(BaseClass):
    def __init__(self, ID, client_id, order_id, percentage, status):
        BaseClass.__init__(self)
        self.ID = ID
        self.client_id = client_id
        self.order_id = order_id
        self.percentage = percentage
        self.status = status

#
# def main():
#     if seat.status==SeatsStatus.AVAILABLE:
#         print("seat is available")
#     else:
#         print("seat is not available")
#     pass
