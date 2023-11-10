import numpy as np
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

c = np.zeros((Nt+1,Nx+1))
c[:,0] = cL
c[:,Nx] = cR

t = np.arange(1,Nt+1)

for n in t:
    for i in range(1,Nx):
        c[n,i] = Fo*c[n-1,i-1] + (1 - 2*Fo)*c[n-1,i] + Fo*c[n-1,i+1]

out = np.array([12.6, 62.5, 125, 625, 5000])
outdt = np.array([int(i) for i in np.linspace(1,Nt,min(Nt,10))])

plt.figure()
for n in outdt:
    plt.plot(x,c[n,:])
    
plt.xlabel('x')
plt.ylabel('c')
plt.title('Concentration Profile at Specific Timesteps')
plt.legend(['t='+str(np.round(t[int(i)]*dt,2)) for i in outdt])
plt.show()