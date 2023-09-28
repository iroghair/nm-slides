import numpy as np

Nx = 100           # Nx grid points
Nt = 40000         # Nt time steps
D = 1e-8           # m/s
c_L = 1.0; c_R = 0 # mol/m3
t_end = 5000.0     # s
x_end = 5e-3       # m

# Time step and grid size
dt = t_end / Nt 
dx = x_end / Nx

# Fourier number
Fo = D * dt / dx / dx

# Initial matrices for solutions (Nx times Nt)
c = np.zeros((Nt + 1, Nx + 1))  # All concentrations are zero
c[:, 0]  = c_L     # Concentration at the left side
c[:, Nx] = c_R     # Concentration at the right side

# Grid node and time step positions
x = np.linspace(0, x_end, Nx + 1)

for n in range(Nt): # time loop
    for i in range(1, Nx): # Nested loop for grid nodes
        c[n+1, i] = Fo*c[n, i-1] + (1-2*Fo)*c[n, i] + Fo*c[n, i+1];
# Output times
outt = [12.5, 62.5, 125, 625, 5000]

# Convert+round to time steps
outt_dt = [int(t // dt) for t in outt]

c_save = c[outt_dt, :].T
with open("inst_diff_example_pde.csv", "w") as f:
    f.write(",".join(["x"]+[("c%.1f"%(t_/60)).replace(".", "") for t_ in outt]))
    for row in np.hstack((x[:,None],c_save)):
        f.write("\n")
        f.write(",".join(["%.5f"%n for n in row]))

# Plot all time steps at once
import matplotlib.pyplot as plt
plt.plot(x, c[outt_dt, :].T)
plt.show()