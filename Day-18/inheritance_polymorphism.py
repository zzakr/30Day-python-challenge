class Shape:
    def area(self):
        return "Calculating area..."

class Square(Shape):
    def area(self):
        return "Area = side * side"

class Circle(Shape):
    def area(self):
        return "Area = π * r²"

shapes = [Square(), Circle()]

for shape in shapes:
    print(shape.area())
