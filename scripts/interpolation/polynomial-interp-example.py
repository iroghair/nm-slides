import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(4.8,3.8))
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.axis([-1.2,1.2,0,1])
xdata = np.arange(-1,1.5,0.5)
ydata = [x * np.sin(x)/np.sqrt(x+2) if x != 0 else 0.5 for x in xdata]
plt.plot(xdata,ydata,'o')

plt.savefig(f'figures/polyfit-example-data.pdf')

xc = np.linspace(-1.1,1.1,1001,endpoint=True)
for deg in range(1,6):
    # Fit coefficients
    p_coeffs = np.polyfit(xdata,ydata,deg)
    # Compute function values
    y = np.polyval(p_coeffs,xc)
    # Plot
    plt.plot(xc,y,label=f'Degree {deg}')
    plt.axis([-1.2,1.2,0,1])    
    plt.legend()
    plt.savefig(f'figures/polyfit-example-p{deg}.pdf')

plt.show()