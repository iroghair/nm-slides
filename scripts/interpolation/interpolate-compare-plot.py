import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

t_sim, c_sim = np.loadtxt("scripts/interpolation/sim_data.txt").T
t_exp, c_exp = np.loadtxt("scripts/interpolation/exp_data.txt").T

# Linear interpolation
f = interp1d(t_sim, c_sim)
diff = np.abs(c_exp - f(t_exp))

# Plot the solution
plt.subplot(2, 1, 1)
plt.plot(t_exp, c_exp, '-x', label='c_exp')
plt.plot(t_exp, f(t_exp), '-|', label='c_sim_new')
plt.xlabel('Time [s]'); plt.ylabel('Conc [mol m$^{-3}$]')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_exp, diff)
plt.xlabel('Time [s]'); plt.ylabel('Difference [mol m$^{-3}$]')
plt.tight_layout()
# plt.show()
plt.savefig('figures/sim_exp_data_interp.pdf')