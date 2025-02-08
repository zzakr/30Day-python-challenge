class Bird:
    def move(self):
        return "I fly"

class Fish:
    def move(self):
        return "I swim"

animals = [Bird(), Fish()]

for animal in animals:
    print(animal.move())
