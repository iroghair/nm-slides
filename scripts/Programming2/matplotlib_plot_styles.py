import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,80)
y2 = 2*x**2 + 4*x - 3
y3 = 20*np.random.rand(y2.size)

ax1 = plt.subplot(2, 2, 1)
ax1.plot(x,y2)
ax1.set_title('Line plot')

ax2 = plt.subplot(2, 2, 2)
ax2.scatter(x,y3)
ax2.set_title('Scatter plot')

ax3 = plt.subplot(2, 2, 3)
ax3.errorbar(x,y2,yerr=y3)
ax3.set_title('Errorbar')

ax4 = plt.subplot(2,2,4)
ax4.hist(y3)
ax4.set_title('Histogram')

# plt.savefig('MyFigure.pdf')
plt.show()