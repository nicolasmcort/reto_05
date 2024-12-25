import math
from Shape.point import Point
from Shape.line import Line 

# Base class for shapes
class Shape:
    def __init__(self, points: list[Point]) -> None:
        if len(points) < 3:
            raise ValueError("A polygon must have at least 3 points")
        self.points = points
        self.edges = [Line(points[i], points[(i + 1) % len(points)]).length for i in range(len(points))]

    def compute_perimeter(self) -> float:
        return sum(self.edges)

    def compute_angles(self) -> list[float]:
        angles = []
        for i in range(len(self.points)):
            p1 = self.points[i - 1]
            p2 = self.points[i]
            p3 = self.points[(i + 1) % len(self.points)]

            a = p1.compute_distance(p2)
            b = p2.compute_distance(p3)
            c = p1.compute_distance(p3)

            # Calculate angle using the Law of Cosines
            angle = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
            angles.append(math.degrees(angle))
        return angles

    def is_regular(self) -> bool:
        return len(set(self.edges)) == 1 and len(set(self.compute_angles())) == 1
