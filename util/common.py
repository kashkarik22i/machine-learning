import scipy as sp
from scipy.optimize import fsolve


def polinom_from_list(coefs):
    return sp.poly1d(coefs)


def get_func_revert(func, value, estimate):
    return fsolve(func - value, x0 = estimate)


def remove_nans(*arrays):
    any_nans = nans(arrays[0])
    for array in arrays[1:]:
        any_nans = sp.logical_or(nans(array), any_nans)
    return [array[~any_nans] for array in arrays]


def nans(xs):
    return sp.isnan(xs)


def split_into(data, train, dev):
    shuffled = sp.copy(data)
    sp.random.shuffle(shuffled)
    size = sp.shape(data)[0]
    first = int(size * train)
    second = int(size * (train + dev))
    return (shuffled[:first,:], shuffled[first:second,:],
            shuffled[second:,:])
