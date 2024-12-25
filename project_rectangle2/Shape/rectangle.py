from Shape.point import Point
from Shape.base import Shape

# Class to represent a rectangle
class Rectangle(Shape):
    def __init__(self, points: list[Point]) -> None:
        if len(points) != 4:
            raise ValueError("A rectangle must have exactly 4 points")
        super().__init__(points)
        if not self._is_rectangle():
            raise ValueError("The points do not form a rectangle")

    def _is_rectangle(self) -> bool:
        angles = self.compute_angles()
        tolerance = 1e-9
        return all(abs(angle - 90) < tolerance for angle in angles)

    def compute_area(self) -> float:
        return self.edges[0] * self.edges[1]
