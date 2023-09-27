import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
data = np.loadtxt('Donnees.txt',skiprows = 1)

xexp = data[:,0]*1e-2
deltax = data[:,1]*1e-2
Texp = data[:,2]
deltaT = data[:,3]
m = 200e-3
l = 28.6e-2
g = 9.81
x = np.linspace(9e-2,25e-2,100)

Itheo = m*(x**2 + l**2)
Iexp = m*g*(l-xexp)*(Texp/(2*np.pi))**2
plt.plot(xexp,Iexp,'o',label='Valeurs expérimentales')
plt.plot(x,Itheo,label='Valeurs théoriques')
plt.plot(x,Itheo+0.007,label='Valeurs théoriques corrigées')
plt.xlabel('Longueur x en m')
plt.ylabel("Moment d'inertie en kg.m²")
plt.errorbar(xexp,Iexp,xerr=deltax,yerr=m*g*(l-deltax)*(deltaT/(2*np.pi))**2,fmt='o')
plt.legend(loc='upper left')
plt.savefig('TP 20.png')
plt.clf()

y = Texp**2*(l-xexp)
plt.plot(xexp**2,y,'o')
f = lambda x,a,b: a*x + b
p,pcov = scipy.optimize.curve_fit(f,xexp**2,y)
a,b=p
x1 = np.linspace(0,25e-2,100)
y1 = f(x1**2,a,b)
plt.plot(x1**2,y1,label = "a = {} et b= {}".format(a,b))
plt.xlabel("x² en m")
plt.ylabel("T²(l-x) en m.s²")
plt.legend()
plt.savefig("En prenant en compte Itige")

plt.clf()