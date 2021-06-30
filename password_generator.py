import random, string
from colorama import init, Style, Back, Fore

init()

a = string.punctuation
b = string.ascii_letters
c = string.digits
d = a + b + c


def gen():
    while True:
        print('* Enter a value no more than "94" *')
        s = int(input('Required password length: '))
        p = "".join(random.sample(d, s))
        print('Password:', Back.RED + p, end='')
        print(Style.RESET_ALL)

gen()
