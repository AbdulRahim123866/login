
# function is an object
# reduce the number of repetition
# loops-repetition is not connected
# function repetition is not connected
# twist the execution flow - normal flow within the function itself
# function must be invoked/ called to be executed
# input - output -small program === modularity increase the quality




# def do_something():#parameters list - parameter= variable = argument
#     """this function will do something
#
#
#     :param a:
#     :return:#packing ,unpacking for tuple
#     """
#     print('do something')
#     print('do something')
#     print('do something')
#     print('do something')
#     print('do something')
#     return None#this is mandatory / it will be executed implecitly
#     # return #this is mandatory / it will be executed implecitly
#     # this is mandatory / it will be executed implecitly

# def summ(a,b,c:int=5,*args,**kwargs) -> int:#by conventional
    #positional / required
    #default
    #list of arguments
    #key word list of argument
    #validation
    # res =a+b+c
    # print(a,b,c)
    # return res
    # print(args)#immputable
    # print(type(args))
    # for i in args:
    #     print(i)
    #
    #
    # print(kwargs)
    # print(type(kwargs))
# def is_prime(a):
#     flage=True
#     for i in range(2,a):
#         if a%i==0:
#             flage=False
#             break
#     return a,flage
# def mod_and_print(lst: list):
#     lst.append(15)
#     print(lst)
def feb(a):
    base=0
    res=1
    for _ in range(1,a):
        base,res=res,(base+res)
    return res

if __name__ == '__main__':
    # print(do_something())
    # print(do_something)#برجع ال referance لانه ال  function هي اصلا object
    # dodo=do_something
    # x=summ(c=1,a=2,b=3)
    # x=summ(1,2,3,5,8,93,5,4,name='me',age=20)
    # print(x)
    # x= input('Enter a number: ')
    # for i in range(1,int(x)):
    #     print(f"{i} is prime = {is_prime(int(i))}")
    # lst2=[1,2,3,4]
    # print(lst2)
    # mod_and_print(lst2)
    # print(lst2)#it is changed because it is mutable
    print(feb(9))



