def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


res = factorial(14)
print(res)
