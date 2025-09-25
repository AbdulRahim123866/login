class HICFG:
    FILE="ABC"#no class variables in python
    pass



#class variable is a shared value between all objects and the class
#class methods is a shared value between all objects and the class | cant be used within object methods
#when object change on it , it change on the class level

#total new attribute

c=HICFG()
print(c.FILE)
print(HICFG.FILE)
c.FILE=c.FILE+"hug"

print(c.FILE)
print(HICFG.FILE)

class A:
    def __init__(self):
        self.__age=0
    def _common(self):
        print(self.__name)
    pass


class API :
    URL="ABC"
    @classmethod
    def do(cls):
        cls.FILE=5
        print(cls.FILE)

