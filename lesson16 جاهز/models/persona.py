from models.models import BaseClass


class Person(BaseClass):
    def __init__(self, _id, name, surname, email, phone, address, status):
        super().__init__()
        self._id=_id
        self._name=name
        self.surname=surname
        self._email=email
        self._phone=phone
        self._address = address
        self._status = status # Tow statis active or not active

    def fullname(self):
        print(f" Full Name : {self.surname}")
        pass

    def is_active(self):
        return self._status == "Active"


class Employee(Person):
  def __init__(self, _id, name, surname, email, phone, address, salary, role, status):
    super().__init__(_id, name, surname, email, phone, address, status)  # inherit from parent
    self._salary = salary
    self._role = role
    pass

  def get_salary(self):
    return self._salary

  def promote(self, new_role):
    self._role = new_role

  def get_role(self):
    return self._role


# Todo check on methods and whats we can append in this class
class Client (Person) :
    def __init__(self, _id, name, surname, email, phone, address, status):
        super().__init__(_id, name, surname, email, phone, address, status)

        self.books=[]
        self.budget = 500
        pass

    def add_order(self,order):
        self.orders.append(order)
        pass

    def pay_for_order(self, payment):
      self.budget -= payment._amount
      return True