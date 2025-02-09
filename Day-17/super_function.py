class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def introduce(self):
        return f"{super().introduce()} I work as a {self.position}."

emp = Employee("Alice", "Software Developer")
print(emp.introduce())
