# interpolate_demo.py
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1/(x**2 + 1/25)
# x4 = np.linspace(-1,1,5,endpoint=True)
# x11 = np.linspace(-1,1,11,endpoint=True)

x4,x10,xinf = [np.linspace(-1,1,n,endpoint=True) for n in [5,11,1001]]
y4,y10,yinf = f(x4),f(x10),f(xinf)

p4 = np.polyfit(x4,y4,4)
p10 = np.polyfit(x10,y10,10)

y4_int = np.polyval(p4,xinf)
y10_int = np.polyval(p10,xinf)

plt.plot(x4,y4,'o')
plt.plot(x10,y10,'x')
plt.plot(xinf,yinf,'-')
plt.plot(xinf,y4_int,'-')
plt.plot(xinf,y10_int,'-')
plt.show()