from Shape.point import Point
from Shape.rectangle import Rectangle

# Subclass of the rectangle to represent a square
class Square(Rectangle):
    def __init__(self, points: list[Point]) -> None:
        super().__init__(points)
        if not self.is_regular():
            raise ValueError("A square must have 4 equal sides and right angles")
