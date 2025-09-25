import random
import re


def password_generator(length,contain_digits:bool=True,contain_char:bool=True,contain_sympols:bool=True):
    inventory=""

    if contain_digits:
        inventory+="0123456789"
    if contain_char:
        inventory += "".join([chr(i) for i in range(65,65+26)])
        inventory += "".join([chr(i) for i in range(97, 97 + 26)])

    if contain_sympols:
        inventory+="!@#$%^&*."
    return "".join(random.choices(inventory,k=length))


def password_validator(password:str,length_threshold=8,contain_mix_case:bool=True,contain_sympols:bool=True,contain_digits:bool=True):

    if len(password)<=length_threshold:
        return "Password must be more than 8 characters."
    if contain_mix_case:
        if password.swapcase()==password.lower() or password.swapcase()==password.upper():
            return "Password must contain mixed latter's cases."

    pattern=r".*[0-9]+.*"
    if contain_digits and not re.match(pattern,password):
        return "Passwprd must contain digits"
    sympols=".*[!@#$%^&*.]+.*"
    if contain_sympols and not re.match(sympols,password):
        return "Passwprd must contain sympol"

    pattern=r"[\w\d.]+@[\w\d]+.\w+"
    if re.match(pattern,password):
        return "Password cant match your email"
    return True










print(password_generator(length=15))
print(password_validator("thI23$hbfdbfd"))