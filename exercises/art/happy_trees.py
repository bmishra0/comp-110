"""some happy, little trees!"""

from .turtle import Turtle
from math import pi
from random import random

__template__ = "https://24s.comp110.com/static/turtle"
DEGREE: float = -pi / 180.0


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    t: Turtle = Turtle()
    t.setSpeed(100)
    t.moveTo(x, y)
    branch(t, y * 0.15, 90 * DEGREE)
    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)
    if length > 3.0:
        branch(t, random_length(length), angle + random_angle())
        branch(t, random_length(length), angle - random_angle())
    t.turnTo(angle + pi)
    t.forward(length)


def random_length(length: float) -> float:
    random_value: float = random()
    factor: float = 0.20 * random_value
    return length * (0.6 + factor)


def random_angle() -> float:
    return (20.0 + 10.0 * random()) * DEGREE
