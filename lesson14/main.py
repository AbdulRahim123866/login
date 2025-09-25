# Encapsulation: protect the content # validation
# 1- use access modifiers
# 1- public - default
# 2- private -
# 3- protected - by convention - using inheritance
# 2- define private getter and setters
# validation
# 3- define as properties
# use as regular # normalization

# Composition # has a

# Abstraction
# Inheritance # is a
# Override
# Polymorphism


class Wheels:
    def __init__(self, brand, age, size):
        self.__brand = brand
        self.__age = age
        self.__size = size

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < self.__age:
            raise ValueError("Age cant decrease.")

        if age <= 0:
            raise ValueError("Age cant be below 0.")

        self.__age = age


class Car:
    def __init__(self, name, age, wheels: list[Wheels] = None):
        self.__name = name
        self.__age = age
        self.__wheels = wheels.copy() if wheels else []  # object from another class as attribute for this class # composition
        # self._age = age
        # self.run()

    @property
    def wheels(self):
        return self.__wheels.copy()

    @wheels.setter
    def age(self, wheels):
        self.__wheels = wheels.copy()


    def add_wheel(self, wheel):
        if type(wheel) is not Wheels:
            raise ValueError(f"A wheel must be from Wheels Class, you provided {type(wheel)}.")
        self.__wheels.append(wheel)


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < self.__age:
            raise ValueError("Age cant decrease.")

        if age <= 0:
            raise ValueError("Age cant be below 0.")

        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def run(self, ):
        pass

    def eat(self, food):
        # print(self._age)
        print(f"{self.name} is eating {food}.")


def SportyCar(Car):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c1 = Car(name="BMW", age=5, wheels=[
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 4, 7),
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
    ])
    c2 = Car(name="BMW2", age=5, wheels=[
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
    ])
    c3 = Car(name="BMW3", age=5, wheels=[
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
        Wheels('Yokohama', 2, 15),
    ])

    for i in [c1, c2, c3]:
        # wheels = i.wheels
        print(f"The car {i.name} has {len(i.wheels)} wheels with ages {[k.age for k in i.wheels]}")
        # wheels.append(Wheels('BBD', 0, 16))
        i.add_wheel(Wheels('BBD', 0, 16))

    print(c1.wheels)
    print(c2.wheels)
    print(c3.wheels)
    # print(c1.wheels)
    # p2 = Person(name="Ahmad", age=22)
    # p1.eat( food="Knafa")
    # p1.name = "Hamada"
    # p1.eat(food="Knafa")
    # p1.__age = -100
    # print(p1._age)

    # p1.age = 20
    # print(p1.age)
    # print(p1.name)

    # Name mangling
    # p1._Person__age = 10
    # print(p1.get_age())

    # you can define object attribute
    # p1.hunter = True
    # print(vars(p1))
    # print(vars(p2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
