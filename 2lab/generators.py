from itertools import count
from math import cos, sin, pi


def gen_rectangle(width=2, height=1, step=4):

    for i in count():

        x = i * step

        yield (
            (x, 0),
            (x + width, 0),
            (x + width, height),
            (x, height)
        )


def gen_triangle(size=2, step=4):

    h = size * (3 ** 0.5) / 2

    for i in count():

        x = i * step

        yield (
            (x, 0),
            (x + size, 0),
            (x + size / 2, h)
        )


def gen_hexagon(radius=1, step=4):

    for i in count():

        cx = i * step

        yield tuple(
            (
                cx + radius * cos(2 * pi * k / 6),
                radius * sin(2 * pi * k / 6)
            )
            for k in range(6)
        )
