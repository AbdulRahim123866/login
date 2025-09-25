#scopes
#clousers

#
# if 5>7:
#     x=10
#
# print(x)#هون هو شايفها بس ما تعرف عليها كقيمة فعرفها undefined
#
# def main():
#     z=10
#     print('welcome to the game ')
#     print("please select the game mode")
#     print("1. Single player ")
#     print("2. Multi Player")
#
# # print(z)#هون هو مو شايفها اصلا مو مبينة معه بالمرة


def wrapper():
    x=10#enclosing
    def inner2():
        x=7#enclosing
        print(x)
        def inner3():
            nonlocal x
            x = 5  # enclosing
            print(x)
            def inner4():
                x = 55  # local
                print(x)
            inner4()
            print(x)
        inner3()
        print(x)
    inner2()
    print(x)
    return x

print(wrapper())