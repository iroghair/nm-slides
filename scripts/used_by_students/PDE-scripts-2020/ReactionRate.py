import numpy as np

def ReactionRate(c):
    k = 0.01
    r = -k*c**2
    return r