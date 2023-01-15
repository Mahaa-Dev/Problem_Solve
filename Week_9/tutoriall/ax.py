import math


def switch():
    a = int(input("enter first number: "))
    b = int(input("enter second number : "))
    ch = int(input("enter 1 for sum.\n 2 for subtract.\n 3 for multiplication.\n 4 for division\.n 5 for truncated division\.n 6 for modulus.\n 7 for Exponentiation"))

    def sum():
        add = a+b
        print("sum =", add)

    def subtract():
        sub = a-b
        print("subtraction  =", sub)

    def multi():
        mul = a*b
        print("multiplication =", mul)

    def division():
        div = a/b
        print("division =", '{{:.2f}'.format(division))

    def trunc():
        tru = a//b
        print("truncated division =", '{{:.2f}'.format(trunc))

    def modulus():
        mod = a % b
        r = ".2f}".format(mod)
        print("modulus =", r)

    def expo():
        epx = math.pow(a, b)
        print("exponentiation =", '{{:.2f}'.format(expo))


dictionary = {
    1: sum,
    2: subtract,
    3: multi,
    4: division,
    5: trunc,
    6: modulus,
    7: exo}
dictionary.get(ch)()
switch()
