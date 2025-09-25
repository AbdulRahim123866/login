def do():
    print("i am doing something")



#default parameters
#the only way for function overloading is by default parameters
#The function must produce different output based on the values provided for the differant inputs/parameters
#the function must produce different output based on the values provided for the differant inputs/parameters
def do(works=None):
    if isinstance(works,str):
        works=[works]
    elif isinstance(works,list):
        pass
    else:
        raise TypeError(f"do ()  dont support type: {type(works)}")

    if not works:
        works=["something"]