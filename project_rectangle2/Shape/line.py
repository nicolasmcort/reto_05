from Shape.point import Point

# Class to represent a line
class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)