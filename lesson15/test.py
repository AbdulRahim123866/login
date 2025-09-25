# Inheritance # parent - child relationship - is a
# inherit the attributes and actions but not the values - on class level not object level
# take the "default values" from the parent if attribute is public
# cant inherit the private attributes

# Python support multi class inheritance
# in multi class inheritance will always inherit attributes from the first class
# in multi class inheritance we cant do multi super calls
# in multi class inheritance we cant work with polymorphism except for the first class
# in multi class inheritance you only inherit non-duplicate action
# in multi class inheritance except for the first class, treat all the others as interface
# Python dont have interfaces

# Abstract class - interfaces
# created to be inherited - cant be instantiated
# abstract class can have both abstract and concrete method
# abstract methods need to be inherited and implemented at concrete classes
# concrete class is the class that provide implementation for all abstract methods

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def drink(self):
        pass
        # print("I am drinking water")


class PredatorAnimals(Animal, ):
    def __init__(self, name, age, ):
        super().__init__(name, age)
        self._pet = False  # protected attribute - by convention
        self.__lazy = False

    # @abstractmethod
    def eat(self):
        print(f"I am too {self.__lazy} to hunt")

    # @abstractmethod
    # def drink(self):
    #     pass


class Flaying:
    def __init__(self):
        self.wings = 2

    def eat(self):
        print(f"I look for grass")

    def fling(self):
        print(f"I look for grass {self.wings}")


class Hook(PredatorAnimals, Flaying):

    def drink(self):
        pass

    def __init__(self, name, age):
        # super().__init__()
        super().__init__(name, age)
        # super(Flaying, self).__init__()
        # print(self.wings)


print(Hook.mro())

a = PredatorAnimals("Random", 2)

# # a2 = PredatorAnimals("Amass", 5)
# a3 = Hook("Tiffa", 3)
# a3.fling()

# print(type(a2) is PredatorAnimals) # on reference level
# print(isinstance(a2, PredatorAnimals)) # on object level
# print(issubclass(PredatorAnimals, Hook)) # on class level


# a3.eat()
# print(a._name)
# print(a2._pet)
# print(a3._pet)
#
# # print(a.__lazy)
# print(a2._PredatorAnimals__lazy)
# print(a3._PredatorAnimals__lazy)
# print(a3._Tiger__lazy)