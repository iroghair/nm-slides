import numpy as np
import matplotlib.pyplot as plt

def is_inside_circle(x, y, radius):
    return x**2 + y**2 <= radius**2

def is_inside_gap(x, y, radius, gap_angle):
    theta = np.arctan2(y, x)
    return is_inside_circle(x, y, radius) and (0 <= theta <= gap_angle)

def random_step():
    angle = np.random.uniform(0, 2 * np.pi)
    step_size = 0.5
    return step_size * np.cos(angle), step_size * np.sin(angle)

def simulate_prisoners_with_gap(num_prisoners, radius, gap_angle):
    positions = np.zeros((num_prisoners, 2))
    escape_times = np.zeros(num_prisoners)

    max_iterations = 1000 #setting a maximum number of iterations
    for iteration in range(max_iterations):
        for prisoner in range(num_prisoners):
            if escape_times[prisoner] == 0:
                step_suggestion = random_step()

                while not is_inside_gap(positions[prisoner, 0] + step_suggestion[0],
                                    positions[prisoner, 1] + step_suggestion[1],
                                    radius, gap_angle):
                    step_suggestion = random_step()

                positions[prisoner, 0] += step_suggestion[0]
                positions[prisoner, 1] += step_suggestion[1]
                
                
                if not is_inside_circle(positions[prisoner, 0], positions[prisoner, 1], radius):
                    escape_times[prisoner] += 1
                    # Remove the prisoner from the simulation once escaped
                    positions[prisoner, :] = np.zeros(2)
        if np.all(escape_times > 0):
            print("All prisoners have escaped.Iteration:", iteration + 1)
            break #All prisoners have escaped, exiting the loop
        if iteration ==max_iterations - 1:
            print("Maximum number of iterations reached. Some prisoners may not have escaped.")
    return escape_times

def plot_histogram_escape_times(escape_times, log_scale=False):
    plt.hist(escape_times, bins='auto', alpha=0.7, color='blue', edgecolor='black', linewidth=1.2, density=True)
    if log_scale:
        plt.xscale('log')
    plt.xlabel('Escape Time')
    plt.ylabel('Frequency')
    plt.title('Histogram of Escape Times')
    plt.show()

radius = 12.0
num_prisoners = 2
gap_angle = 0.1 * np.pi

escape_times = simulate_prisoners_with_gap(num_prisoners, radius, gap_angle)
plot_histogram_escape_times(escape_times, log_scale=True)