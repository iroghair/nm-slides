import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(4,5))
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()

f = lambda x: 1/(x**2 + 1/25)
x4,x10,xinf = [np.linspace(-1, 1, n) for n in [5,11,1001]]
y4,y10,yinf = f(x4), f(x10), f(xinf)
plt.plot(x4,y4,'s',label='$p_4$ data')
plt.plot(x10,y10,'o',label='$p_{10}$ data')
plt.plot(xinf,yinf,label='f(x)')

# Get coefficients for 4th and 10th order polynomial
p4 = np.polyfit(x4, y4, 4)
p10 =  np.polyfit(x10, y10, 10)
# Compute function values using fitted coeffs
yinf4 = np.polyval(p4, xinf)
yinf10 =  np.polyval(p10, xinf)

plt.plot(xinf,yinf4,label='$p_4$ fit')
plt.plot(xinf,yinf10,label='$p_{10}$ fit')

plt.legend()
plt.savefig('figures/polyfit-exercise-p4.pdf')
plt.show()