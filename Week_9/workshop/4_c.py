credits = int(input("Enter the number of college credits earned: "))

if credits >= 90:
    print("Senior Status")
elif credits >= 60:
    print("Junior Status")
elif credits >= 30:
    print("Sophomore Status")
else:
    print("Freshman Status")
