from abc import ABC,abstractmethod
from typing import Any

#Override
#method follow object, function standalone
#Overload - no overloading in python
#Override - In inheritance to have two function with same name[and parameter list by convention] on two different level [parent,child]

#vOverload + Attributes -> Polymorphisim

#mro # execute the nearest

# class Animal:
#     def eat(self,):
#         if "meat" not in self._food:
#             print(f"cant eat {self._food} without meat")
#         print(f"eating {self._food}")
#         pass
#     pass


# class Praditor(Animal):
#     def __init__(self,food):
#         super().__init__()
#         self._food=food



class FileReader:
    def __init__(self,path):
        self._path=path
        self._file=None


    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass



class CSVFileReader(FileReader):
    def read(self,typ="t"):#هاي الحركة بتعني انك بتقدر توخذ داتا يا اما عن طريق listفيها مجموعة str او str مباشرة

        #Context Manager - Nothing that open and close uses it
        with open(self._path,f"r{typ}") as file:#هاي بجرد ما خلص السكوب لحاله بنداي flush , close
            file.read()



    # def write(self,data: Any[list[str],str],typ="t"):
    #     with open(self._path,f"w{typ}") as file:
    #         file.write(data)
    #         return True







def main():
    path="./my_data.csv"
    obj=CSVFileReader(path)
    pass
    Praditor("fish").eat()
Praditor("fish").eat()


if __name__=='__main__':
    lst=[Praditor("meat"),
         ]

    for animal in lst:
        animal.eat()

