total = 0

while True:
    user_input = int(input("Enter a positive integer (0 to exit): "))
    if user_input == 0:
        break
    elif user_input > 100:
        print("Number greater than 100. Not added to total.")
        continue
    total += user_input

print("Total:", total)
