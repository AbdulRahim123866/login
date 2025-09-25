from models.models import BaseClass


class Seat(BaseClass):
  def __init__(self, seat_id, number, status):
    super().__init__()
    self._seat_id = seat_id
    self._number = number
    self._status = status

class Book(BaseClass):
  def __init__(self, book_id, title, author, price, quantity,):
    super().__init__()
    self._book_id = book_id
    self._title = title
    self._author = author
    self._price = price
    self._quantity = quantity
    # self._status = status

  def is_available(self):
    return self._quantity > 0
