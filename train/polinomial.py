import scipy as sp

from util.common import polinom_from_list


def fit_polinom(xs, ys, degree):
    return polinom_from_list(fit_polinom_coefs(xs, ys, degree))


def fit_polinom_coefs(xs, ys, degree):
    return sp.polyfit(xs, ys, degree)


def fit_polinom_coefs_extras(xs, ys, degree):
    return sp.polyfit(xs, ys, degree, full=True)
