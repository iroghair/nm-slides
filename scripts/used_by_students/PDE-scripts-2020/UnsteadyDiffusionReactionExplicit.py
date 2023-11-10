import numpy as np
import matplotlib.pyplot as plt

Nx = 100
Nt = 40000
Dax = 1e-8
cL = 1
cR = 0
tend = 5000
length = 5e-3

dt = tend/Nt
dx = length/Nx

Fo = Dax*dt/(dx*dx)

x = np.linspace(0, length, Nx+1)

c = np.zeros((Nt+1, Nx+1))
c[:,0] = cL
#c[:,Nx+1] = cR
def ReactionRate(c):
    return 0 #replace with your own function

for n in range(Nt):
  for i in range(1,Nx):
    r = ReactionRate(c[n,i])
    c[n+1,i] = Fo*c[n,i-1] + (1 - 2*Fo)*c[n,i] + Fo*c[n,i+1] + r*dt
  c[n+1,Nx+1] = c[n+1,Nx]

out = np.array([12.6, 62.5, 125, 625, 5000])
outdt = np.floor(out/dt).astype(int) #fix changed to floor to avoid errors
plt.plot(x,c[outdt,:])  #plot function changed to plt.plot
plt.show()