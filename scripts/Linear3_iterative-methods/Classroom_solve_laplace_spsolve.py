from laplace_demo import create_laplace_coefficient_matrix, set_boundary_conditions
from scipy.sparse.linalg import spsolve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from it_methods import jacobi, jacobi_vec
import time

Nx, Ny = 20, 20
Tb = {'bottom': 10, 'top': 20, 'left': 200, 'right': 500}

A,b = create_laplace_coefficient_matrix(Nx,Ny)
A,b = set_boundary_conditions(A,b,Tb,Nx,Ny)

# T = spsolve(A,b).reshape(Nx,Ny)
A = A.toarray()

start = time.time()
T = jacobi(A,b)[0].reshape(Nx,Ny)
print(f'Time to compute: {time.time() - start}')

x,y = np.meshgrid(np.linspace(0,1,Nx), np.linspace(0,1,Ny))
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
surf = ax.plot_surface(x,y,T.reshape(Nx,Ny),cmap=cm.inferno,edgecolor='black')
fig.colorbar(surf,shrink=0.5)
plt.show()


T_ex = np.zeros_like(x)

for n in range(1,120):
    m = 2*n - 1
    term = np.sin(m*np.pi*x) * np.sinh(m*np.pi*y)/(m * np.sinh(m*np.pi))
    T_ex += term

T_ex *= (4/np.pi)

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
surf = ax.plot_surface(x,y,T_ex-T,cmap=cm.inferno,edgecolor='black')
fig.colorbar(surf,shrink=0.5)
plt.show()



