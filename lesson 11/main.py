import random
import time


#
#
# # x=5
# def go_out(temp=22,*args,**kwargs):
#     # x=52
#     def adf():
#         pass
#     # print(args)
#     # print(type(args))
#     # print(kwargs)
#     # print(type(kwargs))
#     if temp>21:
#         return True
#     return True,False
#
# if __name__ == '__main__':
#     x=go_out
#     print(x(25))
#     print(x(15))#invocation
#
#     z=go_out(21)#EVALUATION - return value - assign value to variable
#     print(z)
# #هاي الحالة الوحيدة الشاذة اللي بتقدر تنادي فيها فنكشن جوا فنكشن



#reproducibility
#modularity - easy to use and easy to debug(easy to maintain)

#Comprehensionدائما اسرع بالتنفيذ- to build series and only with mutable
# lst=[]
# for i in range(0,11,2):
#     lst.append(2**i)
# print(lst)
# print([2**i for i in range(0,11,2)])
#
# lst=[]
# for i in range(5):
#     lst2=[]
#     for j in range(1,11,2):
#         lst2.append(2**j)
#     lst.append(lst2)
# print(lst)
#
# print([[2**j for j in range(1,11,2)] for i in range(5)])
#
#
#
#
# print(5 if 10>8 else 9)
#
# st="1233211288"
# print([i for i in st if int(i)%2==0])
#
#
# tpl=()# generator - on the fly - only once - very low on memory
#
#
# rng=range(5)
# print(rng)

#
# tpl=(i for i in range(10))# generator - on the fly - only once - very low on memory
# print(tpl)
# for i in tpl:
#     print(i)
# for i in tpl:
#     print(i)


# def wait_before_do():#ال function صار بحد ذاته generator
#     for i in range(10):
#         yield i
#
# x= wait_before_do()

# for i in x:
#     print(i)
# for i in x:
#     print(i)



# for i in wait_before_do():
#     print(i)
# for i in wait_before_do():
#     print(i)




# x= wait_before_do()
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(x)
# print(next(x))

ACCEPTED_NUMBER = []

def otp_generator(sleep=30, expiry=35):
    start = time.time()
    while True:
        number = "".join([str(random.randint(0, 9)) for _ in range(6)])
        ACCEPTED_NUMBER.append(number)
        yield number
        time.sleep(sleep)
        end = time.time()
        if end - start >= expiry:
            ACCEPTED_NUMBER.remove(number)

# for i in otp_generator():
#     print(i)
gen=otp_generator(sleep=30,expiry=35)
x=next(gen)
print(x)