import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1001)
y1 = np.sin(x)
y2 = np.cos(x)

ax1 = plt.subplot(2,2,1)
ax1.plot(x,y1)

ax2 = plt.subplot(2,2,3)
ax2.plot(x,y2)

ax3 = plt.subplot(1,2,2)
ax3.plot(x,np.tan(x))
ax3.set_ylim(-10,10)
ax3.set_xlim(-5,5)

plt.show()