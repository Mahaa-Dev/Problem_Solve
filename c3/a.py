try:
    num = int(input())
    print(num * 10)
    
except EOFError as er:
    print(er)