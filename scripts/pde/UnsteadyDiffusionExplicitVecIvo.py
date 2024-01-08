import numpy as np
from scipy.sparse import diags
import matplotlib.pyplot as plt

Nx = 2000
Nt = 200000
Dax = 1e-8
cL = 1
cR = 0
tend = 50
length = 5e-3

dt = tend/Nt
dx = length/Nx

Fo = Dax*dt/(dx*dx)

x = np.linspace(0, length, Nx+1)

e = np.ones(Nx-1)
ld = np.concatenate(([Fo*e], [0], [0]))
md = np.concatenate(([1], [(1-2*Fo)*e], [1]))
ud = np.concatenate(([0], [0], [Fo*e]))
A = diags([ld, md, ud], [-1, 0, 1], shape=(Nx+1, Nx+1), format='csc')

c = np.zeros((Nt+1, Nx+1))
c[:, 0] = cL
c[:, Nx] = cR

start = time.time()
for n in range(1, Nt+1):
    c[n, :] = A.dot(c[n-1, :])
end = time.time()

c = c.T
out = np.linspace(1, Nt, min(Nt, 10), dtype=int)
plt.plot(x, c[:, out])
plt.show()