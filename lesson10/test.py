# # from main import x#sub import
# import main#import كامل
# import main as m
# print(main.x)
# # print(x)
# print(m.x)
import time

#
# #closure
# def wrapper(company):
#     #company: closure
#     def inner2(employee):
#         print(f"{employee} is working at {company}")
#     return inner2
#
# do=wrapper("Google")#do صارت عبارة عن function بحد ذاتها
#
# do("yazeed")
# do("Reachil")
# do("Ahmad")

#Decoration: design pattern : wrapper

def timer(func):#fun صار ثابت دائما باشر على ال this_is_a_printer
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print(f"Took {end - start}'s to execute")
    return wrapper


@timer
def this_is_a_printer():
    for i in range(1000):
        print("This is a printer")



#this_is_a_printer=timer(this_is_a_printer)
this_is_a_printer()


def summ(a,b):
    return a+b

print(summ(1,2))#invocation
abc=summ#call by reference
print(abc(1,2))