from itertools import zip_longest


def zip_polygons(*iters):

    for polys in zip(*iters):

        yield tuple(
            point
            for poly in polys
            for point in poly
        )


def zip_tuple(*iters):
    return zip(*iters)


def count_2D(polygons):

    return sum(
        len(poly)
        for poly in polygons
    )
