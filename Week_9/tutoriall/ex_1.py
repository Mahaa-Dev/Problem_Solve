a = b = 2
c = False
if not c:
    if b < a:
        b += 5
        a = b-1
    elif a < b:
        c = True
    else:
        if a+b < 4:
            c = False

    a = 11
    b = 2.2
print(a, b, c)
