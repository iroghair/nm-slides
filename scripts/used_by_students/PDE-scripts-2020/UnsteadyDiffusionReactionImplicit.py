import numpy as np
from scipy.sparse import diags

Nx = 100
Nt = 4000
Dax = 1e-8
cL = 1
cR = 0
tend = 5000
length = 5e-3
h = 1e-8

dt = tend / Nt
dx = length / Nx

Fo = Dax * dt / (dx * dx)

x = np.linspace(0, length, Nx+1)

A = np.zeros((Nx+1, Nx+1))
A[0, 0] = 1
for i in range(1, Nx):
    A[i, i-1] = -Fo
    A[i, i] = 1 + 2*Fo
    A[i, i+1] = -Fo
A[Nx, Nx] = 1
A[Nx, Nx-1] = -1

c = np.zeros((Nt+1, Nx+1))
c[:, 0] = cL
for n in range(1, Nt+1):
    b = c[n, :].copy()
    b[Nx] = 0
    
    for i in range(1, Nx):
        r = ReactionRate(c[n, i])
        rh = ReactionRate(c[n, i]+h)
        drdc = (rh - r) / h
        A[i, i] = 1 + 2*Fo - drdc*dt
        b[i] = b[i] + (r - drdc*c[n, i])*dt
    
    c[n+1, :] = np.linalg.solve(A, b)

out = [12.6, 62.5, 125, 625, 5000]
outdt = [int(x / dt) for x in out]
plt.plot(x, c[outdt, :])