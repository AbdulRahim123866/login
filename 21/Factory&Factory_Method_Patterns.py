# #Simple Method
#
# class Animal:
#     def speak(self):pass
#
# class Dog(Animal):
#     def speak(self):return "Woof!"
# class Cat(Animal):
#     def speak(self):return "Meow!"
#
# class AnimalFactory:
#     def creat_animal(self,type):
#         if type=="dog":return Dog()
#         elif type=="cat":return Cat()
#         else:raise ValueError("Unknown animal")
#
# #Usage
# factory=AnimalFactory()
# dog=factory.creat_animal("dog")
# print(dog.speak())

#__________________________________________________________

#Factory Method
# from abc import ABC,abstractmethod
#
# class Creator(ABC):
#     @abstractmethod
#     def factory_method(self):
#         pass
#
#     def operation(self):
#         product=self.factory_method()
#         return f"Creatot:{product.operation()}"
# class ConcreteBuilderA():
#     def Concret(self):
#         pass
#
# class ConcreteCreatorA(Creator):
#     def factory_method(self):
#         return ConcreteBuilderA()
#
#
#
#
#_______________________________________________________
#
# class DogFactory:
#     @staticmethod
#     def create():
#         return Dog()
#
#
# class CatFactory:
#     @staticmethod
#     def create():
#         return Cat()
# class AnimalFactory:
#     factories={
#         "dog":DogFactory,
#         "cat":CatFactory,
#     }
#     @staticmethod
#     def creat_animal(animal_type:str)->Animal:
#         factory=AnimalFactory.factories.get(animal_type)
#         if not factory:
#             raise ValueError("unknown animal type")
#         return factory.create()
# if __name__=="__main__":
#     animal1=AnimalFactory.creat_animal("cat")
#     print(animal1.speak())


# class Dog:
#     def speak(self):
#         return "woff!"
# class Cat:
#     def speak(self):
#         return "Meaoo!"
# class AnimalFactory:
#     @staticmethod
#     def creat_animal(animal_type):
#         if animal_type in ["dog","Dog"]:
#             return Dog()
#         elif animal_type in ["cat","Cat"]:
#             return Cat()
#         else:
#             raise ValueError("Unknown animal type")
#
# animal=AnimalFactory.creat_animal("Dog")
# print(animal.speak())
# animal=AnimalFactory.creat_animal("cat")
# print(animal.speak())