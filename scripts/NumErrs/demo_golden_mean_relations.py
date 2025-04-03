import numpy as np

def golden_mean_recurrent(Ntot):
# Initialize the series with the given initial conditions
    y = np.zeros(Ntot,dtype=np.float32)
    y[0] = 1
    y[1] = 2 / (1 + np.sqrt(5))
    # Perform the recurrence to fill in the rest of the series
    for n in range(2, Ntot):
        y[n] = y[n-2] - y[n-1]
    return y

def golden_mean_powerlaw(Ntot):
    # Initialize the constant value
    x = (1 + np.sqrt(5)) / 2
    # Generate a range of values from 0 to Ntot and apply the power law
    y = x ** -np.arange(0, Ntot + 1,dtype=np.float32)

    return y    

y1 = golden_mean_recurrent(41)
y2 = golden_mean_powerlaw(41)

for i,j in zip(y1,y2):
    print(i,j)

