import math 

from Shape.point import Point
from Shape.triangle import define_triangle
from Shape.rectangle import Rectangle
from Shape.square import Square

# Código para probar las clases
triangle_points = [Point(0, 0), Point(4, 0), Point(2, math.sqrt(12))]
triangle = define_triangle(triangle_points)
print(f"The type of triangle is: {type(triangle).__name__}")
print(f"The area of the triangle is: {triangle.compute_area()}")

rectangle_points = [Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)]
rectangle = Rectangle(rectangle_points)
print(f"The area of the rectangle is: {rectangle.compute_area()}")

square_points = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
square = Square(square_points)
print(f"The area of the square is: {square.compute_area()}")