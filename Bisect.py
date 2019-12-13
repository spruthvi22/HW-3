"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Finding root using Bisect method

"""

import numpy as np
import scipy.optimize as op

def f(x):
    fx=np.sin(np.cos(np.exp(x)))
    return(fx)

rt=op.bisect(f,-1,1)
print("The root is = ",rt)
print("The value of Function at root = ",f(rt)) ## the root is valid to the Epyslon of the computer
