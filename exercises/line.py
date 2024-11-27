"""Defines a simple line class made of two points."""

from exercises.points import Point


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        """Initializes a Line with two point objects."""
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"Line from {self.start} to {self.end}"

    def length(self) -> float:
        """compute the length of a line."""
        return self.start.distance(self.end)
