import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def g1(x):
    return (3*x**2 + 3*x + 4)**(1/3)

def g2(x):
    return (x**3 - 3*x**2 - 4) / 3

def f(x):
    return 0.1*x**3 - 3*x - 4

# Number of iterations
N = 4

# Initialize lists to store x and g1(x), g2(x) values
x = np.linspace(-3, 7, 100)
x_values_g1 = [0]
x_values_g2 = [0]
g1_values = [0]
g2_values = [0]

# Perform N iterations for both g1(x) and g2(x)
for i in range(N):
    new_x1 = g1(x_values_g1[-1])
    new_x2 = g2(x_values_g2[-1])
    
    x_values_g1.extend([x_values_g1[-1], new_x1])
    x_values_g2.extend([x_values_g2[-1], new_x2])
    g1_values.extend([new_x1, new_x1])
    g2_values.extend([new_x2, new_x2])

# Create the staircase plot for both functions
plt.figure(figsize=(4, 2.6))
plt.xlim(-3, 8)
plt.ylim(-3, 8)
plt.plot(x, g1(x), label="$g_1(x)$")
plt.plot(x, g2(x), label="$g_2(x)$")
plt.plot(x, x, label="$y=x$")
plt.plot(x_values_g1, g1_values, 'r-', label='Iterations (g1)')
plt.plot(x_values_g2, g2_values, 'g-', label='Iterations (g2)')
# Plot iterations for g1(x)
for p1 in zip(x_values_g1[1::2], g1_values[1::2]):
    plt.plot([p1[0]], [p1[1]], "ro-", mfc="none")

# Plot iterations for g2(x)
for p2 in zip(x_values_g2[1::2], g2_values[1::2]):
    plt.plot([p2[0]], [p2[1]], "go-", mfc="none")
plt.yticks([])
plt.xticks(x_values_g1[1::2], ["$x_%i$" % i for i in range(N)])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.text(x[-1] + 0.3, g1(x[-1]), "$y=g_1(x)$")
plt.text(x[-1] + -2.5, g1(x[-1])+1, "$y=g_2(x)$")
# plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("./martin_slides_dependencies/direct_iteration_photo2.eps")
plt.show()
