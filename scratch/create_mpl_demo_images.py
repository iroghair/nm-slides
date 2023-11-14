import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-10.0, 10.0, 20)
p = np.cos(np.pi * t/10) 
q = 1/(1+np.exp(-t)) - 0.5

plt.plot(t,p,'--x') # Dashed line, cros
plt.plot(t,q,'r-o') # Red, line, circles
plt.plot(t,-q,'k^') # Black triangle marker
plt.xlabel('x+2')
plt.ylabel('Function value [-]')
# plt.ion()
# plt.show()

# plt.clf()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1000)
y1,y2 = np.sin(x), 2*np.cos(x)

# Specify figure size
fig = plt.figure(figsize=(8, 7))

# First index of 2x2 grid (top-left)
ax1 = plt.subplot(2, 2, 1) 
ax1.plot(x,y1)
ax1.set_title('sin(x)')

# Second index of 2x2 grid (top-right)
ax2 = plt.subplot(2, 2, 2) 
ax2.plot(x,y2)
ax2.set_title('cos(x)')

# Second index of 2x1 grid (whole bottom)
ax3 = plt.subplot(2, 1, 2) 
ax3.plot(x,y1**2+y2**2)
ax3.set_title(r'$\sin^2(x)+\cos^2(x)$')
plt.tight_layout()





fig2 = plt.figure(figsize=(8, 7))
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
plt.show()

