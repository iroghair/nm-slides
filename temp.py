import numpy as np
import matplotlib.pyplot as plt

t_sim, c_sim = np.loadtxt("./data/sim_data.txt").T
t_exp, c_exp = np.loadtxt("./data/exp_data.txt").T

# Linear interpolation
c_sim_new = np.interp(t_exp, t_sim, c_sim)
diff = np.abs(c_exp - c_sim_new)

# Plot the solution
plt.figure(figsize=(4.5,4.5))
plt.subplot(2, 1, 1)
plt.plot(t_exp, c_exp, 'b-x', label='c_exp')
plt.plot(t_exp, c_sim_new, 'r-o', label='c_sim_new')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_exp, diff); plt.show()

# Compute the L2-norm
norm = np.linalg.norm(diff)
print(norm)