import numpy as np
from matplotlib import pyplot as plt


def complex_plot(Z):
    X = [x.real for x in Z]
    Y = [x.imag for x in Z]
    plt.scatter(X, Y, color='red')
    # plt.show()


def w(z):
    return 1/2 * (z+1/z)


x = np.linspace(-3, 3, 100)
y = -np.ones(100)
# y = np.zeros(1000)
grid = np.meshgrid(x, np.linspace(-3, -0.01, 100))
print(grid)
plt.plot(grid)

line = np.array([np.complex(a, b) for a, b in zip(x, y)])

plt.ylim(-2, 2)
plt.subplot(2, 1, 1)
# complex_plot(line)

plt.subplot(2, 1, 2)
# complex_plot(w(line))


plt.show()
