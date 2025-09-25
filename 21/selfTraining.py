# class Cofee:
#
#     def cost(self):
#         return 5
#
#
#
# class coffeDecorator:
#     def __init__(self,coffe):
#         self._cofee=coffe
#     def cost(self):
#         return self._cofee.cost()
#
#
# class Milkdecorator(coffeDecorator):
#     def cost(self):
#         return self._cofee.cost()+2
#
# class Chocolatdecorator(coffeDecorator):
#     def cost(self):
#         return self._cofee.cost()+3
#
#
# coffee=Cofee()
# print("Coffee:",coffee.cost())
# coffe_with_milk=Milkdecorator(coffee)
# print("Coffe with milk:",coffe_with_milk.cost())
# coffe_with_Chocolat=Chocolatdecorator(coffee)
# print("Coffe with Chocolat:",coffe_with_Chocolat.cost())
from typing import List, Any

import protocol


# class Text:
#     def render(self):
#         return "Hello, World!"
#
# class TextDecorator:
#     def __init__(self,text):
#         self._text=text
#     def render(self):
#         return self._text.render
#
#
#
#
# # إضافة Bold
# class BoldDecorator(TextDecorator):
#     def render(self):
#         return f"<b>{self._text.render()}</b>"
#
# # إضافة Italic
# class ItalicDecorator(TextDecorator):
#     def render(self):
#         return f"<i>{self._text.render()}</i>"
#
# # إضافة Underline
# class UnderlineDecorator(TextDecorator):
#     def render(self):
#         return f"<u>{self._text.render()}</u>"
#
#
# # الاستخدام
# text = Text()
# print(text.render())
# # Hello, World!
#
# bold_text = BoldDecorator(text)
# print(bold_text.render())
# # <b>Hello, World!</b>
#
# italic_bold_text = ItalicDecorator(bold_text)
# print(italic_bold_text.render())
# # <i><b>Hello, World!</b></i>
#
# final_text = UnderlineDecorator(italic_bold_text)
# print(final_text.render())
# # <u><i><b>Hello, World!</b></i></u>


# class MessageSender:
#     def textwrite(self):
#         return "hello world"
#
# class decorateMessage:
#     def __init__(self,text):
#         self._text=text
#
#     def textwrite(self,text):
#         return self._text.textwrite()
#
#
#
#
# class Compression(decorateMessage):
#     def textwrite(self):
#         return f"{self._text.textwrite()} compressed"
#
# class LoggedMessage(decorateMessage):
#     def textwrite(self):
#         return f"{self._text.textwrite()} logged"
#
# te=MessageSender()
# print(te.textwrite())
#
# compressed=Compression(te)
# print(compressed.textwrite())
#
# logged_and_compressed = LoggedMessage(compressed)
# print(logged_and_compressed.textwrite())


# #1-Strategy Interface
# class SortStrategy:
#     def sort(self,data:List[int])->List[int]:
#         pass
#
# #2-Concrete Strategies
# class BubbleSort(SortStrategy):
#     def sort(self,data:List[int]) ->List[int]:
#         print("bubble sorte")
#         return sorted(data)
#
#
# class QuickSort(SortStrategy):
#     def sort(self,data:List[int]) ->List[int]:
#         print("Quick sorte")
#         return sorted(data)
#
# #3-Context
# class SortContext:
#     def __init__(self,strategy:SortStrategy):
#         self._strategy=strategy
#
#     def set_strategy(self,strategy:SortStrategy):
#         self._strategy=strategy
#
#
#     def sort(self,data:List[int])->List[int]:
#         return self._strategy.sort(data)
#
#
# data=[14,5,3,9,2]
# context=SortContext(BubbleSort())
# print(context.sort(data))

#
# #1-Strategy Interface
# class TaxStrategy:
#     def calculte_tax(self,amount:float)->float:
#         pass
#
#
#
# #2-Concrete Strategies
# class USATax(TaxStrategy):
#     def calculate_tax(self,amount:float) ->float:
#         print("Calculating tax for USA")
#         return amount*0.07
#
# class EroupTax(TaxStrategy):
#     def calculate_tax(self,amount:float) ->float:
#         print("Calculating tax for Eroup")
#         return amount*0.2
#
# class NoTax(TaxStrategy):
#     def calculate_tax(self, amount: float) -> float:
#         print("No tax applied")
#         return 0.0
#
# #3-Context
# class Order:
#     def __init__(self,amount:float,tax_strategy:TaxStrategy):
#         self._tax_strategy=tax_strategy
#         self._amount=amount
#     def set_taxStrategy(self,tax_strategy:TaxStrategy):
#         self._tax_strategy=tax_strategy
#
#     def calculate_total(self):
#         tax=self._tax_strategy.calculate_tax(self._amount)
#         return self._amount+tax
#
# order=Order(200,NoTax())
# print(order.calculate_total())


#Product

# class Car:
#     def __init__(self,brand=None,weels=None,color=None,year=None):
#         self.brand=brand
#         self.weels=weels
#         self.color=color

#         self.year=year
#     def __str__(self):
#         return f"{self.brand}-{self.weels}-{self.color}-{self.year}"
#
#
# class CarBulider:
#     def __init__(self):
#         self._car=Car()
#     def set_brand(self,brand):
#         self._car.brand=brand
#         return self
#     def set_weels(self,weels):
#         self._car.weels=weels
#         return self
#     def set_color(self,color):
#         self._car.color=color
#         return self
#     def set_year(self,year):
#         self._car.year=year
#         return self
#
#     def bulid(self):
#         return self._car
#
# bulider=CarBulider()
# car=bulider.set_brand("BMW").set_weels("weels").set_year(2025).set_color("(white and black)").bulid()
# print(car)


# #Abstract Product
#
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
# class AnimalFactory:
#     def creat_animal(self):
#         raise NotImplementedError
#
# class DogFactory(AnimalFactory):
#     def creat_animal(self):
#         return Dog()
#
# class DogFactory(AnimalFactory):
#     def creat_animal(self):
#         return Cat()
#
# factory=DogFactory()
# animal=factory.creat_animal()
# print(animal.speak())



#Adapter


# #1-Target
# class MediaPlayer:
#     def play(self,filename:str):
#         pass
# #2-adaptee
#
# class VLCPlayer:
#     def play_vlc(self,filename:str):
#         print(f"playing VLC file:{filename}")
# class MP4Player:
#     def play_mp4(self,filename:str):
#         print(f"playing MP4 file:{filename}")
#
# #3-Adapter
# class MediaAdapter(MediaPlayer):
#     def __init__(self, player_type: str):
#         if player_type == "vlc":
#             self.player = VLCPlayer()
#         elif player_type == "mp4":
#             self.player = MP4Player()
#
#     def play(self, filename: str):
#         if isinstance(self.player, VLCPlayer):
#             self.player.play_vlc(filename)
#         elif isinstance(self.player, MP4Player):
#             self.player.play_mp4(filename)
#
# # def play_media(player_type: str, filename: str):
# #     player = MediaAdapter(player_type)
# #     player.play(filename)
# #
# class AudioPlayer(MediaPlayer):
#     def play(self, filename: str) -> None:
#         if filename.endswith(".mp3"):
#             print(f"Playing mp3 file: {filename}")
#         elif filename.endswith(".vlc"):
#             adapter = MediaAdapter("vlc")
#             adapter.play(filename)
#         elif filename.endswith(".mp4"):
#             adapter = MediaAdapter("mp4")
#             adapter.play(filename)
#         else:
#             print(f"Unsupported file format: {filename}")

from typing import List ,Protocol, Any

# class Observer(Protocol):
#     def update(self,data:Any)->None:
#         pass
#
# class EmailAlert(Observer):
#     def update(self,data:Any)->None:
#         print(f"EmailAlert: notified with:{data}")
#
#
# class SMSAlert(Observer):
#     def update(self,data:Any)->None:
#         print(f"SMSAlert: notified with:{data}")
#
# class Subject:
#     def __init__(self):
#         self._observers:List[Observer]=[]
#
#     def attach(self,observer:Observer)->None:
#         if observer not in self._observers:
#             self._observers.append(observer)
#     def deattach(self,observer:Observer)->None:
#         if observer  in self._observers:
#             self._observers.remove(observer)
#
#     def notify(self,data:Any)->None:
#         for obsrever in self._observers:
#             obsrever.update(data)
#
# if __name__=="__main__":
#     subject=Subject()
#     email_observer=EmailAlert()
#     sms_observer=SMSAlert()
#
#
#     subject.attach(email_observer)
#     subject.attach(sms_observer)
#     subject.notify("Temperature is above threshold")


# # Model
# class StudentModel:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, name):
#         self.students.append(name)
#
# # View
# class StudentView:
#     def show_students(self, students):
#         print("قائمة الطلاب:")
#         for student in students:
#             print(student)
#
# # Controller
# class StudentController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#     def add_student(self, name):
#         self.model.add_student(name)
#         self.view.show_students(self.model.students)
#
# # Usage
# model = StudentModel()
# view = StudentView()
# controller = StudentController(model, view)
#
# controller.add_student("أحمد")
# controller.add_student("سارة")

# class StudentModel:
#     def __init__(self):
#         self.students=[]
#     def add_student(self,new_student):
#         self.students.append(new_student)
#
# class ViewStudent:
#     def view(self,student):
#         print("قائمة الطلاب:")
#         for i in student:
#             print(i)
#
# class Controller:
#     def __init__(self,model,view):
#         self._model=model
#         self._view=view
#     def add_student(self,name):
#         self._model.add_student(name)
#         self._view.view(self._model.students)
#
#
#
# model = StudentModel()
# view = ViewStudent()
# controller = Controller(model, view)
#
# controller.add_student("أحمد")
# controller.add_student("سارة")