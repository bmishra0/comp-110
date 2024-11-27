from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """construct a new Point object."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return a string representation for people."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Return a string representation for python evaluation."""
        return f"Point({self.x}, {self.y})"

    def distance(self, other: Point) -> float:
        """Distance b/w self and other."""
        delta_x: float = (self.x - other.x) ** 2
        delta_y: float = (self.y - other.y) ** 2
        return (delta_x + delta_y) ** 0.5
