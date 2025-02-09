def print_info(entity):
    print(entity.info())

class Car:
    def info(self):
        return "I'm a Car."

class Bike:
    def info(self):
        return "I'm a Bike."

print_info(Car())  # I'm a Car.
print_info(Bike())  # I'm a Bike.
