# NOTE: Changing this file will reflect in the slides!
dydx = lambda x,y: (-0.2*y + 2.5)
tspan = [0,20]
y0 = [0.12]

from scipy.integrate import solve_ivp
sol = solve_ivp(dydx, tspan, y0)

import matplotlib.pyplot as plt
plt.figure(figsize=(4,3))
plt.plot(sol.t, sol.y[0,:])
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('figures/demo_single_ode.pdf')
plt.show()