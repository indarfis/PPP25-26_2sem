from math import dist


def polygon_area(poly):
    s = 0

    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]

        s += x1 * y2 - x2 * y1

    return abs(s) / 2


def polygon_perimeter(poly):
    return sum(
        dist(
            poly[i],
            poly[(i + 1) % len(poly)]
        )
        for i in range(len(poly))
    )


def shortest_side(poly):
    return min(
        dist(
            poly[i],
            poly[(i + 1) % len(poly)]
        )
        for i in range(len(poly))
    )


def longest_side(poly):
    return max(
        dist(
            poly[i],
            poly[(i + 1) % len(poly)]
        )
        for i in range(len(poly))
    )


def point_inside_polygon(point, poly):

    x, y = point
    inside = False

    n = len(poly)

    for i in range(n):

        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        intersect = (
            ((y1 > y) != (y2 > y))
            and
            (
                x <
                (x2 - x1) * (y - y1)
                / (y2 - y1 + 1e-9)
                + x1
            )
        )

        if intersect:
            inside = not inside

    return inside


def is_convex(poly):

    n = len(poly)

    if n < 3:
        return False

    signs = []

    for i in range(n):

        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        x3, y3 = poly[(i + 2) % n]

        cross = (
            (x2 - x1) * (y3 - y2)
            -
            (y2 - y1) * (x3 - x2)
        )

        signs.append(cross > 0)

    return all(signs) or not any(signs)
