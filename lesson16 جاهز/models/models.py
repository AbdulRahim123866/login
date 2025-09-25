from datetime import datetime


# Employee: id, name, surname, email, phone, address, salary, role, status
# Client: id, name, surname, email, phone, address, status
# Book: id, title, author, price, quantity, status
# Seat/Table: id, number, status
# Order: id, client_id, book_id, quantity, price, status
# Payment: id, client_id, order_id, amount, status
# Discount: id, client_id, order_id, percentage, status
# DataQuality: name, date [YYYYMMDD], ...., status


class BaseClass:
  def __init__(self):
    self._updated_at: datetime = None
    self._removed_at: datetime = None
    self._created_at: datetime = datetime.now()

  # def __str__(self):
  #     return f"{self.bid}({self.title})"