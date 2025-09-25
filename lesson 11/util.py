import functools


def timer(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        print("before")
        value=func(*args,**kwargs)
        print(value)
        print("after")
        return value
    return wrapper_decorator


def do_twice(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        value = func(*args, **kwargs)
        value=func(*args,**kwargs)
        return value
    return wrapper_decorator


@timer
@do_twice
def do_something():
    for i in range(100):
        print(i,end=" ")
    print()

# do_something=timer(do_something)
# do_something=timer(do_twice(do_something))
# print(do_something())
do_something()