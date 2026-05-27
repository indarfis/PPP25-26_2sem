from math import radians, cos, sin


def tr_translate(dx, dy):

    def transform(poly):
        return tuple(
            (x + dx, y + dy)
            for x, y in poly
        )

    return transform


def tr_rotate(angle):

    a = radians(angle)

    def transform(poly):

        return tuple(
            (
                x * cos(a) - y * sin(a),
                x * sin(a) + y * cos(a)
            )
            for x, y in poly
        )

    return transform


def tr_symmetry(axis='x'):

    def transform(poly):

        if axis == 'x':
            return tuple((x, -y) for x, y in poly)

        if axis == 'y':
            return tuple((-x, y) for x, y in poly)

        return poly

    return transform


def tr_homothety(k):

    def transform(poly):
        return tuple(
            (x * k, y * k)
            for x, y in poly
        )

    return transform
