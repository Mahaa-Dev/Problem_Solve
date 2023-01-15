import random


def b():
    num = int(input("Enter"))
    bnum = random.randint(1, 100)
    if num == bnum:
        print("Match")
    elif num > bnum:
        print("Greater")
    else:
        print("smaleer")


b()
