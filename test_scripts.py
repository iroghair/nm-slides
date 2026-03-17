import numpy as np

a,b,c = 1.0,1e8,1.0
disc = np.sqrt(b*b-4*a*c)

x1 = (-b+disc)/(2*a)
x2 = (-b-disc)/(2*a)

print(x1, x2, x1*x2)


import numpy as np

def roots_stable(a,b,c):
    disc = np.sqrt(b*b-4*a*c)
    q = -0.5*(b+np.sign(b)*disc)
    return q/a, c/q

print(roots_stable(a,b,c))