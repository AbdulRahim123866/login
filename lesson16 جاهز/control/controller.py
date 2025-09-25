from random import randint, choice

from models.consts import BookStatus, EmployeeRole
from models.invetory import Book
from models.persona import Employee
from models.transactions import Order, Discount, Payment

inventory = [
  Book(**{
    "book_id": i,
    "title": f"Book {i}",
    "author": f"Author {i}",
    "price": randint(2, 25),
    "quantity": 10,
    # "status": choice([BookStatus.USED, BookStatus.NEW])
  }) for i in range(100)

]
print(inventory)


class Library:
  def __init__(self):
    self.inventory = inventory
    self.employee = Employee(
      _id="asf51", name="Ahmad Dada", surname="AbuDa", email="ahmad.852@gmail.com", phone="079852258552",
      address="", salary=5000, role=EmployeeRole.REGULAR, status="active"
    )

  def list_books(self):
    return {book._title: book for book in self.inventory if book._quantity > 0}

  def place_order(self, client, books: list[str]):
    available = self.list_books()

    requested = []
    total_price = 0
    for name in books:
      if name in available.keys():
        requested.append(available[name])
        available[name]._quantity -= 1
        total_price += available[name]._price


    # discount = Discount(discount_id="20254410", ) quantitiy=len(requested),

    order = Order(order_id="ord1521", client=client, book=requested, price=total_price, status="pending")
    return order


  def pay_for_order(self, order,):
    discount = Discount(discount_id="20254410", client=order._client, order=order, percentage=10)

    order._price = discount.apply_discount(order._price)

    payment = Payment(payment_id="pay1521", client=order._client, order=order, amount=order._price, status="pending")
    return payment

