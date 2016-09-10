import scipy as sp


def squares_error(f, x, y):
    return sp.sum((f(x) - y) ** 2)
