import functools
import random
import time



# def loop_and_mean(func,itera=1):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         lst=[]
#         for i in range(itera):
#             value = func(*args, **kwargs)
#             lst.append(value)
#
#         return sum(lst)/len(lst)
#     return wrapper
#
# def return_random():
#     return random.randint(0,100)
#
#
# return_random=loop_and_mean(return_random,1000)
# print(return_random())

def timer(func):#fun صار ثابت دائما باشر على ال this_is_a_printer
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print(f"Took {end - start}'s to execute")
    return wrapper

@timer
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

print(is_prime(277))

import time

def timer(func):
    def wrapper(*args, **kwargs):  # تقبل أي عدد من المعاملات
        start = time.time()
        result = func(*args, **kwargs)  # نمرر المعاملات للدالة الأصلية
        end = time.time()
        print(f"Took {end - start}'s to execute")
        return result  # نعيد نتيجة الدالة الأصلية
    return wrapper

@timer
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(277))