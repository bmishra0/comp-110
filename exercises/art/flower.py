"""Turtle Art!"""

from .turtle import Turtle
from math import pi

__template__ = "https://24ss2.comp110.com/static/turtle"


def main() -> Turtle:
    t: Turtle = Turtle()
    t.setSpeed(0.25)

    length: float = 150.0
    while length > 0:
        t.left(pi / 2.0 - pi / 8.0)
        t.forward(length)
        length -= 2.0

    return t
