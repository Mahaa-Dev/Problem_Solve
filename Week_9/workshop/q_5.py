from random import shuffle

# Creating a list of cars
cars = ["Mercedes", "BMW", "Audi", "Ford", "Toyota"]

# Adding some cars to the list
cars.append("Honda")
cars.append("Hyundai")

# Removing some cars from the list
cars.remove("Mercedes")
cars.remove("BMW")

# Shuffle the cars before displaying the list
shuffle(cars)
print(cars)
