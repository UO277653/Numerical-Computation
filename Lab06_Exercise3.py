# -*- coding: utf-8 -*-
"""
Lab 6, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

def chebyshev(f,a,b,n):
    
    # Building the nodes
    x = lambda x : np.cos(((2*x - 1)*np.pi)/(2*n))
    res = np.zeros(n)
    for i in range(1,n + 1): 
        res[i-1] = x(i)
    
    return res

# Example 1
print("------------  Function f1  ------------")
f1 = lambda x : 1/(1 + 25 * x**2)
a = -1
b = 1
n = 11
points = np.linspace(a,b,100)

# Plot using equispaced
equipoints = np.linspace(a,b,n)
pol = np.polyfit(equipoints,f1(equipoints),len(equipoints)-1)  # polynomial coefficients

xp = np.linspace(min(equipoints),max(equipoints),200)
yp = np.polyval(pol,xp)
plt.figure()
plt.plot(points,f1(points),'blue',equipoints,f1(equipoints),'ro',xp,yp,'r')
plt.legend(['function','points','polynomial'],loc='best')
plt.title("Equispaced nodes")
plt.show()

# Plot using chebyshev
x = chebyshev(f1,a,b,n)
y = f1(x)

pol = np.polyfit(x,y,len(x)-1)

xp = np.linspace(min(x),max(x),200)
yp = np.polyval(pol,xp)

points = np.linspace(a,b,100)
plt.figure()
plt.axis([-1.05, 1.05, -0.3, 2.3])
plt.plot(points,f1(points),'blue',x, f1(x),'ro',xp, yp,'r')
plt.legend(['function','points','polynomial'],loc='best')
plt.title("Chebyshev nodes")
plt.show()

# Example 2
print("------------  Function f2  ------------")
f1 = lambda x : np.exp(-20*x**2)
a = -1
b = 1
n = 15
points = np.linspace(a,b,100)

# Plot using equispaced
equipoints = np.linspace(a,b,n)
pol = np.polyfit(equipoints,f1(equipoints),len(equipoints)-1)  # polynomial coefficients

xp = np.linspace(min(equipoints),max(equipoints),200)
yp = np.polyval(pol,xp)
plt.figure()
plt.plot(points,f1(points),'blue',equipoints,f1(equipoints),'ro',xp,yp,'r')
plt.legend(['function','points','polynomial'],loc='best')
plt.title("Equispaced nodes")
plt.show()

# Plot using chebyshev
lolpoints = np.linspace(a,b,n)
x = chebyshev(f1,a,b,n)
y = f1(x)

pol = np.polyfit(x,y,len(x)-1)

xp = np.linspace(min(x),max(x),200)
yp = np.polyval(pol,xp)

points = np.linspace(a,b,100)
plt.figure()
plt.axis([-1.05, 1.05, -0.3, 2.3])
plt.plot(points,f1(points),'blue',x, f1(x),'ro',xp, yp,'r')
plt.legend(['function','points','polynomial'],loc='best')
plt.title("Chebyshev nodes")
plt.show()