def filter_decorator(predicate):

    def decorator(func):

        def wrapper(*args, **kwargs):

            polygons = func(*args, **kwargs)

            return filter(predicate, polygons)

        return wrapper

    return decorator


def transform_decorator(transform):

    def decorator(func):

        def wrapper(*args, **kwargs):

            polygons = func(*args, **kwargs)

            return map(transform, polygons)

        return wrapper

    return decorator
