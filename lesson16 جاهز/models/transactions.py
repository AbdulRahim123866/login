from models.models import BaseClass


class Discount(BaseClass):
  def __init__(self, discount_id, client, order, percentage, status=None):
    super().__init__()
    self._discount_id = discount_id
    self._client = client
    self._order = order
    self._percentage = percentage
    # self._status = status

  def apply_discount(self, amount):
    return amount * (1 - self._percentage / 100)

class Order(BaseClass):
    def __init__(self, order_id, client, book, price, status):
        super().__init__()
        self._order_id=order_id
        self._client=client
        self._book=book
        # self._quantity = quantity
        self._price = price
        self._status = status

    # def calculate total


class Payment(BaseClass):
  def __init__(self, payment_id, client, order, amount, status):
    super().__init__()
    self._payment_id = payment_id
    self._client = client
    self._order = order
    self._amount = amount
    self._status = status