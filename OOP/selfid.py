class MyClass:
    def __init__(self, name):
        self.name = name

    def print_id(self):
        print(id(self))


# Create an instance of the class
my_obj = MyClass("example")

# Print the identity of the instance
my_obj.print_id()

print(id(my_obj))
