import random
from random import randint

number=randint(0,1000)
print(number)
for i in range(5):
    guess=int(input(f"guess the random integer you have {5-i} tryes"))
    if guess==number:
        print("success")
        break
    elif guess>number+100 or guess<number-100:
        print('far')
    elif number - 50 <= guess <= number + 50:
        print("close")

    else:
        print("not quite")
