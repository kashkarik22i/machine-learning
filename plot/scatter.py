import matplotlib.pyplot as plt
from util.artificial import *

def plot_simple_scatter(xs, ys):
    plt.scatter(xs, ys, s=10)

    # name the plot
    title(plt, title="Data")

    # name axes
    labels(plt, xname="xs", yname="ys")

    autoscale(plt, tight=True)

    # add grid lines on the plot
    grid(plt, linestyle='-', color='0.75')

    return plt


def add_function(plt, f, start, end):
    xs = linespace(start, end, 1000)
    plt.plot(xs, f(xs), linewidth=4)


def labels(plt, xname, yname):
    plt.xlabel(xname)
    plt.ylabel(yname)


def autoscale(plt, tight):
    plt.autoscale(tight=tight)


def title(plt, title):
    plt.title(title)


def grid(plt, linestyle, color):
    plt.grid(True, linestyle=linestyle, color=color)
