import numpy as np
import matplotlib.pyplot as plt

# Define the function g(x)
def g(x):
    return np.cbrt(10*(3*x+ 3))

def f(x):
    return 0.1*x**3 -3*x - 3

# Number of iterations
N = 4

# Initialize lists to store x and g(x) values
x = np.linspace(-1, 7, 100)
x_values = [0]
gx_values = [0]

# Perform N iterations
for i in range(N):
    new_x = g(x_values[-1])
    x_values.extend([x_values[-1], new_x])
    gx_values.extend([new_x, new_x])

# Create the staircase plot
plt.figure(figsize=(3, 2))
plt.xlim(-0.5,7)
plt.ylim(0,8)
plt.plot(x, g(x), label = "$g(x)$")
plt.plot(x, x, label = "$y=x$")
plt.plot(x_values, gx_values, 'r-', label='Iterations')
for p in zip(x_values[1::2], gx_values[1::2]):
    plt.plot([p[0]], [p[1]], "ro", mfc="none")

plt.yticks([])
plt.xticks(x_values[1::2], ["$x_%i$"%i for i in range(N)])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.text(x[-1]+0.3,g(x[-1]),"$y=g(x)$")
plt.text(x[-1]+0.3,x[-1],"$y=x$")
# plt.xlabel('$x$')
# plt.ylabel('$g(x)$')
# plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("./martin_slides_dependencies/direct_iteration_photo.eps")
plt.show()
