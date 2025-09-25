import sys
from dataclasses import dataclass


# @dataclass(frozen=True)#make immutable
# class Point:
#     x:float
#     y:float
#
#     def distance_from_origin(self):
#         return (self.x**2+self.y**2)**0.5
#
#
# #Usage
# p=Point(3,4)
# print(p.distance_from_origin())#5.0
# #p.x=10 #Raises FrozenInstanceError
#
# sys.exit(0)


# class ImmutablePerson:
#     def __init__(self,name,age):
#         self._age=age
#         self._name=name
#
#     @property
#     def name(self):return self._name
#
#     @property
#     def age(self):return self._age
#
#     def set_name(self, name):
#         return ImmutablePerson(name,self.age)
#
#     def set_age(self,age):
#         return ImmutablePerson(self.name,age)
#
#
# a=ImmutablePerson("Ahmad",20)
# print(a)
# print(a.age)
# b=a
# print(b)
# a=a.set_age(30)
# print(a)


class Money:
    def __init__(self,amount,currency):
        self._amount=amount
        self._currency=currency
    @property
    def amount(self):
        return self._amount
    @property
    def currency(self):
        return self._currency

    def add(self,value):
        return Money(self._amount+value,self._currency)

    def __str__(self):
        return f"{self._amount} {self._currency}"


salary=Money(1000,"USD")

print(salary)

salary=salary.add(50)
print(salary)