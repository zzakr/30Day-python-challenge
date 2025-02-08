# Defining a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating an object
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())
