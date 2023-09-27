import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.optimize
from scipy.stats import linregress
data = np.loadtxt('TP19.txt',skiprows = 1)

x = np.linspace(0,30*1e-2,100)
theta = np.linspace(0,np.pi/2,100)

Ep = lambda x,theta: -0.2*9.81*29.5*1e-2*np.cos(theta) + 0.2*9.81*x*np.cos(theta) - 9.81*(40*1e-2+0.5*1e-2*theta)

xexp = data[:,0]
thetaexp = data[:,2]
dx = data[:,1]
dtheta = data[:,3]

for xi in x:
    y = Ep(xi,theta)
    plt.plot(theta,y)

theta_eq = np.arcsin(0.5*1e-2/(0.2*(29.5*1e-2-xexp)))
theta_rad = thetaexp*np.pi/180
y1 = Ep(xexp,theta_rad)
plt.plot(theta_rad,y1,'o')
'''plt.plot(theta_eq+0.1,Ep(xexp,theta_eq))'''
plt.savefig('TP19.png')
plt.show()
