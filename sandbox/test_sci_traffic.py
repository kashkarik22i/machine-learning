import scipy as sp

from util.common import *
from util.eval import *
from train.polinomial import *
from util.data import *
from plot.scatter import *

# data
tsv = read_tsv('./data/web_traffic.tsv')

# split
train, dev, test = split_into(tsv, train=0.8, dev=0)
train_xs, train_ys = remove_nans(train[:, 0], train[:, 1])
test_xs, test_ys = remove_nans(test[:, 0], test[:, 1])


# training
f1 = fit_polinom(train_xs, train_ys, 1)
f2 = fit_polinom(train_xs, train_ys, 2)
f3 = fit_polinom(train_xs, train_ys, 3)
f4 = fit_polinom(train_xs, train_ys, 4)


# testing
print(squares_error(f1, test_xs, test_ys))
print(squares_error(f2, test_xs, test_ys))
print(squares_error(f3, test_xs, test_ys))
print(squares_error(f4, test_xs, test_ys))

print(get_func_revert(f1, 30, 20))
print(get_func_revert(f2, 30, 20))
print(get_func_revert(f3, 30, 20))
print(get_func_revert(f4, 30, 20))

# displaying
xmin = sp.amin(test_xs)
xmax = sp.amax(test_xs)
plt = plot_simple_scatter(test_xs, test_ys)
add_function(plt, f1, xmin, xmax)
add_function(plt, f2, xmin, xmax)
add_function(plt, f3, xmin, xmax)
add_function(plt, f4, xmin, xmax)
plt.show()
