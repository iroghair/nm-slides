# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Linear interpolation
c_sim_new = np.interp(t_exp, t_sim, c_sim, kind='linear')
diff = abs(c_exp - c_sim_new)

# Plot the solution
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t_exp, c_exp, 'b-x', t_exp, c_sim_new, 'r-o')
ax1.set_title('Linear interpolation')
ax2.stem(t_exp, diff)
ax2.set_title('L2-norm')
plt.show()

# Compute the L2-norm
np.linalg.norm(diff)