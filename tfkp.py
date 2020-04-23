import numpy as np
from matplotlib import pyplot as plt
from itertools import product


def complex_plot(Z):
    X = [x.real for x in Z]
    Y = [x.imag for x in Z]
    plt.scatter(X, Y, color='red')


def w(z):
    return 1/2 * (z+1/z)


xs = np.linspace(-50, 50, 50)
ys = np.linspace(-5, -1, 50)

# grid = np.meshgrid(xs, ys)
grid = product(xs, ys)


line = np.array([np.complex(a, b) for a, b in grid])


# plt.ylim(-2, 2)
plt.subplot(2, 1, 1)
complex_plot(line)

plt.subplot(2, 1, 2)
complex_plot(w(line))


plt.show()
