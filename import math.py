import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def get_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2) * (semi_perimeter - self.side3))
        return area
triangle = Triangle(3, 4, 5)
print(triangle.get_triangle_type())  
print(triangle.get_area()) 
equilateral_triangle = Triangle(5, 5, 5)
print(equilateral_triangle.get_triangle_type()) 
print(equilateral_triangle.get_area())  