import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s}"

def calc_meshgrid(F, x_range, y_range, resolution):
    x = np.linspace(x_range[0], x_range[1], resolution)[None,:]
    y = np.linspace(y_range[0], y_range[1], resolution)[:,None]
    x, y = np.meshgrid(x, y)
    return x, y, F(x,y)

def plot_contours(F, x_range=(-3, 3), y_range=(-3, 3), resolution=400, **kwargs):
    if "levels" not in kwargs:
        kwargs["levels"] = [0]
        plot_implicit_function(F, x_range, y_range, resolution, **kwargs)
        return 
    x, y, z = calc_meshgrid(F, x_range, y_range, resolution)

    # Plot the contour where F(x, y) = 0
    CS = plt.contour(x, y, z, kwargs["levels"], **kwargs)
    plt.gca().clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)

def plot_implicit_function(F, x_range=(-3, 3), y_range=(-3, 3), resolution=400, **kwargs):
    """
    Plots an implicit function F(x, y) = 0 within the given range.
    
    Parameters:
        F: Callable function that takes x and y and returns a scalar.
        x_range: Tuple specifying the range for x-values (xmin, xmax).
        y_range: Tuple specifying the range for y-values (ymin, ymax).
        resolution: Integer specifying the number of points in the meshgrid.
    """
    x, y, z = calc_meshgrid(F, x_range, y_range, resolution)

    # Plot the contour where F(x, y) = 0
    return plt.contour(x, y, z, [0], **kwargs)

def plot_surface_function(F, x_range=(-3, 3), y_range=(-3, 3), resolution=400, **kwargs):
    """
    Plots an implicit function F(x, y) = 0 within the given range.
    
    Parameters:
        F: Callable function that takes x and y and returns a scalar.
        x_range: Tuple specifying the range for x-values (xmin, xmax).
        y_range: Tuple specifying the range for y-values (ymin, ymax).
        resolution: Integer specifying the number of points in the meshgrid.
    """
    x, y, z = calc_meshgrid(F, x_range, y_range, resolution)

    # Plot the contour where F(x, y) = 0
    ax = plt.gcf().add_subplot(111, projection="3d")
    ax.plot_surface(x, y, z, cmap="coolwarm")
    ax.set_zlabel("z")
    ax.set_box_aspect((1, 1, 1))

# Making a small figure
plt.figure(figsize=(3,3))

# Plot the function
# plot_implicit_function(lambda x,y: y-x**2, resolution=100, colors="blue")
# plot_implicit_function(lambda x,y: y**2+x**2-4, resolution=100, colors="red")
# plot_surface_function(lambda x,y: np.sqrt((x**2 + y**2 -4)**2+(x**2-y+1)**2),
#                       (0,3),(0,3), resolution=100)
plot_contours(lambda x,y: np.sqrt((x**2 + y**2 -4)**2+(x**2-y+1)**2),
              (0, 3), (0, 3), resolution = 100, levels=[0, 1, 2, 3, 4])

# Add axis labels and title
plt.xlabel('x')
plt.ylabel('y')

# Show grid and make the aspect ratio equal
plt.grid(True)
plt.axis('equal')
plt.tight_layout()

plt.show()
