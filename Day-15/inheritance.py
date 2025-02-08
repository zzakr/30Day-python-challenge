class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())
