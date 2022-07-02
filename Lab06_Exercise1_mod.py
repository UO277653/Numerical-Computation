# -*- coding: utf-8 -*-
"""
Mark of the lab: 7

Lab 6, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

def lagrange_fundamental(k,x,z):
    res = 1
    factor = 0
    res = np.ones_like(z)
        
    for j in range(len(z)):
        for i in range(len(x)):
            if i != k: 
                factor = (z[j]-x[i])/(x[k]-x[i])
                res[j] = res[j] * factor
    
    return res
    
    
# Input: k, index of the fundamental polynomial, x, the x coordinates of the 
# nodes (or points the polynomial passes through) and z, point (or array of points) 
# where we will evaluate the polynomial. 
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])

# We compute and plot ℓ0
k = 0
z = np.linspace(-1,5,100)
zpoints = np.array(x * (np.eye(len(x))))
yz = lagrange_fundamental(k,x,z)

plt.figure()
plt.plot(z, yz, z, z*0, 'black')
plt.plot(zpoints, lagrange_fundamental(k, x, zpoints),'o',color='orange')
plt.title('L0') 
plt.show()

# We compute and plot ℓ1
k = 1
z = np.linspace(-1,5,100)
zpoints = np.array(x * (np.eye(len(x))))
yz = lagrange_fundamental(k,x,z)

plt.figure()
plt.plot(z, yz, z, z*0, 'black')
plt.plot(zpoints, lagrange_fundamental(k, x, zpoints),'o',color='orange')
plt.title('L1') 
plt.show()

# We compute and plot ℓ2
k = 2
z = np.linspace(-1,5,100)
zpoints = np.array(x * (np.eye(len(x))))
yz = lagrange_fundamental(k,x,z)

plt.figure()
plt.plot(z, yz, z, z*0, 'black')
plt.plot(zpoints, lagrange_fundamental(k, x, zpoints),'o',color='orange')
plt.title('L2') 
plt.show()

# We compute and plot ℓ3
k = 3
z = np.linspace(-1,5,100)
zpoints = np.array(x * (np.eye(len(x))))
yz = lagrange_fundamental(k,x,z)

plt.figure()
plt.plot(z, yz, z, z*0, 'black')
plt.plot(zpoints, lagrange_fundamental(k, x, zpoints),'o',color='orange')
plt.title('L3') 
plt.show()

# We compute and plot ℓ4
k = 4
z = np.linspace(-1,5,100)
zpoints = np.array(x * (np.eye(len(x))))
yz = lagrange_fundamental(k,x,z)

plt.figure()
plt.plot(z, yz, z, z*0, 'black')
plt.plot(zpoints, lagrange_fundamental(k, x, zpoints),'o',color='orange')
plt.title('L4') 
plt.show()

# Pn(z)=y0ℓ0(z)+y1ℓ1(z)+⋯+ynℓn(z)
