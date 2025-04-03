import numpy as np
import matplotlib.pyplot as plt

fun = lambda x: 4.5*x + 2.0 + np.random.normal(0, 0.5, x.shape)

x = np.array([0, 1, 2, 3])
y = fun(x)

A = np.vander(x)
a = np.linalg.solve(A, y)
print(A,a)

xfit = np.linspace(x[0,], x[-1])
yfit = np.dot(np.vander(x), a)
plt.plot(x, y, 'o')
plt.plot(xfit, yfit, '-')
plt.show()

