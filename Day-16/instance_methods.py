class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", 3)
print(dog1.bark())  # Buddy says Woof!
