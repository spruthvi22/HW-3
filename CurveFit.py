"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Fitting Spline and Polynomial to data

"""

import numpy as np
import scipy.interpolate as inter
import matplotlib.pyplot as plt

x=np.linspace(0,5,6)
y=np.array([1.0,2.0,1.0,0.5,4.0,8.0])
sp_in_1=inter.InterpolatedUnivariateSpline(x,y,k=1)
sp_in_2=inter.InterpolatedUnivariateSpline(x,y,k=2)
sp_in_3=inter.InterpolatedUnivariateSpline(x,y)
sp_lag=inter.lagrange(x,y)
fig1=plt.figure()
plt.plot(x,y,'ro',label='data')
xs=np.linspace(0,5,100)
plt.plot(xs,sp_in_1(xs),'r',label='1st order spline')
plt.plot(xs,sp_in_2(xs),'b',label='2nd order spline')
plt.plot(xs,sp_in_3(xs),'g',label='3rd order spline')
plt.plot(xs,sp_lag(xs),'k',label='lagrange poynomial')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Interpolated data")
plt.legend()
plt.show()
fig1.savefig("plot.pdf")
