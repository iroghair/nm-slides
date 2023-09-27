import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set grid resolution
nx = 40
ny = 40

# Set old solution array
T = np.zeros((nx, ny))

# Set boundary conditions
T[0, :] = 40  # Left
T[nx-1, :] = 60  # Right
T[:, 0] = 20  # Bottom
T[:, ny-1] = 30
T[19:25, 19:25] = 100
fixedT = np.zeros((nx, ny))
fixedT[19:25, 19:25] = 1

# Set new solution array (including boundary conditions)
Tnew = T.copy()

# Required for plotting
x, y = np.meshgrid(np.arange(1, nx+1), np.arange(1, ny+1))

for iter in range(1000):
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            if fixedT[i, j] != 1:
                Tnew[i, j] = (T[i-1, j] + T[i+1, j] + T[i, j-1] + T[i, j+1]) / 4.0

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, y, T, cmap='coolwarm', linewidth=0, antialiased=False)
    ax.set_title("Iteration: " + str(iter+1))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Temperature")
    ax.set_zlim(0, np.max(T))
    plt.show()

    T = Tnew.copy()