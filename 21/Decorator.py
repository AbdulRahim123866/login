import sys

#
# class Component:
#     def operation(self):
#         pass
#
#
# class ConcreteComponent(Component):
#     def operation(self):
#         return "Basic operation"
#
#
# class Decorator(Component):
#     def __init__(self, component):
#         self._component = component
#
#     def operation(self):
#         return self._component.operation()
#
#
# class ConcreteDecorator(Decorator):
#     def operation(self):
#         return f"Enhanced {super().operation()}"
#
#
# # Usage
# component = ConcreteComponent()
# decorated = ConcreteDecorator(component)
# print(decorated.operation())  # Enhanced Basic operation


#-------------------------------------------------------------------------------------

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args,**kwargs):
#         print(1)
#         value=func(*args,**kwargs)
#         print(2)
#         return value
#     return wrapper_decorator
#
# @decorator
# def do_something():
#     print("i am playing ")
#
# do_something()
# sys.exit(0)
#
#


# class TextDecorator:
#     def __init__(self,text):
#         self._text=text
#
#     def render(self):
#         return self._text.render()
#
# class BoldDecorator(TextDecorator):
#     def render(self):
#         return f"<b>{super().render()}</b>"
#
# class ItalicDecorator(TextDecorator):
#     def render(self):
#         return f"<i>{super().render()}</i>"
#
# text=TextDecorator()
# decorated=ItalicDecorator(BoldDecorator(text))
# print(decorated.render())

import functools
import time


def class_decorator(cls):
    # Wrap __init__ to add pre/post logic
    orig_init = cls.__init__

    @functools.wraps(orig_init)
    def new_init(self, *args, **kwargs):
        print(f"Instantiating {cls.__name__} with {args} {kwargs}")
        orig_init(self, *args, **kwargs)
        print(f"Instance of {cls.__name__} created")

    cls.__init__ = new_init

    # Wrap all non-special methods
    for attr, val in cls.__dict__.items():
        if callable(val) and not attr.startswith("__"):
            @functools.wraps(val)
            def wrapper(self, *args, __val=val, **kwargs):
                start=time.time()
                print(f"Calling {cls.__name__}.{__val.__name__}({args}, {kwargs})")
                result = __val(self, *args, **kwargs)
                print(f"{cls.__name__}.{__val.__name__} returned {result}")
                print(f"Took {time.time()-start} to execute")
                return result
            setattr(cls, attr, wrapper)

    return cls

#Example
@class_decorator
class Sample:
    def __init__(self,value):
        self.value=value

    def double(self):
        time.sleep(2)
        return self.value*2

    def increment(self,x):
        return self.value+x


#Usage
obj=Sample(10)
obj.double()
# obj.increment(5)