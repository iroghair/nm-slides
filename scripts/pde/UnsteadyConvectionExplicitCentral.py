import numpy as np
import matplotlib.pyplot as plt

Nx = 1000
Nt = 10000
u = 0.0001
cin = 1
tend = 100
length = 0.1

dt = tend/Nt
dx = length/Nx

Co = u*dt/dx

x = np.linspace(0, length, Nx+1)

c = np.zeros((Nt+1, Nx+1))
c[:,0] = cin

for n in range(Nt):
    for i in range(1, Nx):
        c[n+1,i] = c[n,i] - Co*(c[n,i+1] - c[n,i-1])/2
    c[n+1,Nx] = c[n+1,Nx-1]
    
out = [10, 20, 30, 60, 100]
outdt = np.floor_divide(out, dt).astype(int)
plt.plot(x,c[outdt,:])
plt.show()