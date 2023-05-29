class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(id(self))


dog1 = Dog("Fido", 3)
dog2 = Dog("Tiger",5)
print(dog1.name)  # Output: "Fido"
print(dog1.age)  # Output: 3
print(id(dog2))
print(id(dog1))

