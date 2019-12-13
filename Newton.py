"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Finding root of the equation

"""
import numpy as np
import scipy.optimize as opt

def df(x):
    return(-1* np.exp(x) * np.cos(np.cos(np.exp(x))) * np.sin(np.exp(x)))

def f(x):
    return(np.sin(np.cos(np.exp(x))))

print("Newton Rapson at -1 = ",opt.newton(f,-1,fprime=df))
print("Newton Rapson at -0.1 = ",opt.newton(f,-0.1,fprime=df))
print("Secant at -0.1 = ",opt.newton(f,-0.1))
## As the function has multiple roots the initial value determines the root that is found 
