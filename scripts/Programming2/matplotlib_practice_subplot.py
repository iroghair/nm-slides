import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1000)
y1,y2,y3 = np.sin(x), np.cos(x), np.tan(x)

ax1 = plt.subplot(2, 2, 1) 
ax1.plot(x,y1)
ax1.set_title('sin(x)')

ax2 = plt.subplot(2, 2, 3) 
ax2.plot(x,y2)
ax2.set_title('cos(x)')

# Second index of 2x1 grid (whole bottom)
ax3 = plt.subplot(1, 2, 2) 
ax3.plot(x,y3)
ax3.set_title('tan(x)')
ax3.set_ylim(-10, 10)

plt.tight_layout()
plt.show()