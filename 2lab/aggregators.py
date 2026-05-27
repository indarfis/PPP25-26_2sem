from functools import reduce
from math import dist

from utils import *


def agr_origin_nearest(polygons):

    def nearest_vertex(poly):
        return min(
            poly,
            key=lambda p: dist((0, 0), p)
        )

    return reduce(
        lambda acc, p:
        min(
            acc,
            nearest_vertex(p),
            key=lambda x: dist((0, 0), x)
        ),
        polygons,
        (float('inf'), float('inf'))
    )


def agr_max_side(polygons):

    return reduce(
        lambda acc, p:
        max(acc, longest_side(p)),
        polygons,
        0
    )


def agr_min_area(polygons):

    return reduce(
        lambda acc, p:
        min(acc, polygon_area(p)),
        polygons,
        float('inf')
    )


def agr_perimeter(polygons):

    return reduce(
        lambda acc, p:
        acc + polygon_perimeter(p),
        polygons,
        0
    )


def agr_area(polygons):

    return reduce(
        lambda acc, p:
        acc + polygon_area(p),
        polygons,
        0
    )
