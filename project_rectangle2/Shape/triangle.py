import math

from Shape.point import Point
from Shape.base import Shape

# Class to represent a triangle
class Triangle(Shape):
    def __init__(self, points: list[Point]) -> None:
        if len(points) != 3:
            raise ValueError("A triangle must have exactly 3 points")
        super().__init__(points)

    def compute_area(self) -> float:
        a, b, c = self.edges
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c)) # Heron's formula

# Subclasses of triangles
class Equilateral(Triangle):
    def __init__(self, points: list[Point]) -> None:
        super().__init__(points)

class Isosceles(Triangle):
    def __init__(self, points: list[Point]) -> None:
        super().__init__(points)

class Scalene(Triangle):
    def __init__(self, points: list[Point]) -> None:
        super().__init__(points)

class RightTriangle(Triangle):
    def __init__(self, points: list[Point]) -> None:
        super().__init__(points)

# Function to identify the type of triangle
def define_triangle(points: list[Point]) -> Triangle:
    triangle = Triangle(points)
    edges = sorted(triangle.edges)
    tolerance = 1e-9

    # Check if all three sides are equal with a tolerance to account for floating-point errors
    if all(abs(edge - edges[0]) < tolerance for edge in edges):
        return Equilateral(points)
    # Check if two sides are equal (isosceles triangle)
    elif len(set(edges)) == 2:
        return Isosceles(points)
    # Check if it's a right triangle using the Pythagorean theorem
    elif abs(edges[0]**2 + edges[1]**2 - edges[2]**2) < tolerance:
        return RightTriangle(points)
    else:
        return Scalene(points)
