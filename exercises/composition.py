"""Line from two point objects."""

from exercises.points import Point
from exercises.line import Line

origin: Point = Point(0.0, 0.0)
print(f"origin: {origin}")

up_5: Point = Point(5.0, 5.0)
print(f"up_5: {up_5}")

a_line: Line = Line(origin, up_5)
print(a_line)

print(f"a_line.length() is {a_line.length()}")
