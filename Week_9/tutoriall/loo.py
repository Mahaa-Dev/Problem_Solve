def temp(celcius):
    if celcius > 38:
        print("Fever")
    elif celcius < 38 and celcius > 37.5:
        print("Normal temperature")
    else:
        print("low temperature")


tm = float(input("Enter temperature"))
temp(tm)
