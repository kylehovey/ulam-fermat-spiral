from sympy import divisor_count
from math import pi, sqrt
from cmath import exp
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.collections
from string import Template

def memoize(f):
    cache = {}
    def ret(a):
        if a not in cache:
            cache[a] = f(a)
        return cache[a]

    return ret

primeOmega = memoize(lambda n: divisor_count(n, 1) - 1)

def saveSpiral(filename, theta = pi * (3 - sqrt(5)), limit = 2000, window = 50):
    dots = array(map(
        lambda n: sqrt(n) * exp(1j * n * theta),
        range(1, limit)
    ))

    sizes = array(map(
        lambda n: exp(-(0.7 + max(1, primeOmega(n))/6)),
        range(1, limit)
    ))

    patches = [
        plt.Circle([u.real, u.imag], size) for u, size in zip(dots, sizes)
    ]

    fig, ax = plt.subplots()
    coll = matplotlib.collections.PatchCollection(patches, facecolors='black')
    ax.add_collection(coll)
    ax.set_aspect(1)

    plt.axis([-window, window, -window, window])
    plt.savefig(filename, dpi=500)

    return plt

if __name__ == "__main__":
    saveSpiral("main.png", limit=500, window=25)
