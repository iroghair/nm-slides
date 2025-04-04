import numpy as np
import matplotlib.pyplot as plt

Nx = 1000
Nt = 100000
u = 0.001
cin = 1
tend = 100
length = 0.1

dt = tend/Nt
dx = length/Nx

Co = u*dt/dx

x = np.linspace(0, length, Nx+1)

c = np.zeros((Nt+1, Nx+1))
c[:, 0] = cin

for n in range(1, Nt+1):
    for i in range(1, Nx):
        c[n, i] = c[n-1, i] - Co*(c[n-1, i+1] - c[n-1, i-1])/2
    c[n, Nx] = c[n, Nx-1]

out = [10, 20, 30, 60, 100]
outdt = [int(x/dt) for x in out]

plt.plot(x, c[outdt[:-1], :])