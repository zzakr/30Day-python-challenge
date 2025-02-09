class Vehicle:
    def move(self):
        return "I am moving"

class Car(Vehicle):
    def move(self):
        return "I drive on roads"

car = Car()
print(car.move())  # I drive on roads
