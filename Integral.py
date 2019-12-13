"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Finding the integral of the fiunction

"""
import numpy as np
import scipy.integrate as integ

def f(x):
    return(np.exp(x))

xs=np.linspace(0,1,1000)
print("Trapezoid = ",np.trapz(f(xs),x=xs))
print("Simpson = ",integ.simps(f(xs),x=xs))
print("Romberg = ",integ.romberg(f,0,1))
print("Gaussian = ",integ.fixed_quad(f,0,1)[0])
