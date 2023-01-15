positive_count = 0
negative_count = 0

while True:
    user_input = int(input("Enter an integer (0 to exit): "))
    if user_input == 0:
        break
    elif user_input > 0:
        positive_count += 1
    else:
        negative_count += 1

print("Positive integers entered:", positive_count)
print("Negative integers entered:", negative_count)
