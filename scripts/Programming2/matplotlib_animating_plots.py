import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)    
y = np.sin(x)
y1 = np.cos(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y, '-')
line2, = ax.plot(x, y1, '-')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Animating a Sine Wave')
plt.show(block=False)

for i in range(20,len(x)):
    line.set_data(x[i-20:i+1], y[i-20:i+1])
    line2.set_data(x[i-20:i+1], y1[i-20:i+1])
    fig.canvas.draw()
    fig.canvas.flush_events()
    # fig.savefig(f'anim{i}.png')
    plt.pause(0.01)

