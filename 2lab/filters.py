from utils import *


def flt_convex_polygon():

    def predicate(poly):
        return is_convex(poly)

    return predicate


def flt_angle_point(point):

    def predicate(poly):
        return point in poly

    return predicate


def flt_square(max_area):

    def predicate(poly):
        return polygon_area(poly) < max_area

    return predicate


def flt_short_side(max_len):

    def predicate(poly):
        return shortest_side(poly) < max_len

    return predicate


def flt_point_inside(point):

    def predicate(poly):
        return point_inside_polygon(point, poly)

    return predicate


def flt_polygon_angles_inside(other_poly):

    def predicate(poly):

        return any(
            point_inside_polygon(p, poly)
            for p in other_poly
        )

    return predicate
