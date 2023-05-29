def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


try:
    num = int(input("Enter a number to calculate its factorial: "))
    print(factorial(num))
except ValueError as e:
    print(e)
