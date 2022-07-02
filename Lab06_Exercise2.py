# -*- coding: utf-8 -*-
"""
Lab 6, Exercise 2

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

def lagrange_polynomial(x,y,z):
    res = 0
    for i in range(len(y)):
            res += y[i] * lagrange_fundamental(i, x, z)
        
    
    return res
    
    
# Input: x and y, coordinates of the nodes (or points the polynomial passes through) 
# and z, point (or array of points) where we will evaluate the polynomial. 
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])

# Example 1
z = np.linspace(-1,5,100)
zpoints = np.array(x * (np.eye(len(x))))
yz = lagrange_polynomial(x,y,z)

plt.figure()
plt.plot(x, y,'o',color='red')
plt.plot(z, yz)
plt.legend(['points','p'])
plt.show()

# Example 2
x1 = np.array([-1., 0, 2, 3, 5, 6, 7])
y1 = np.array([ 1., 3, 4, 3, 2, 2, 1])

z = np.linspace(-1,7,100)
zpoints = np.array(x1 * (np.eye(len(x1))))
yz = lagrange_polynomial(x1,y1,z)

plt.figure()
plt.plot(x1, y1,'o',color='red')
plt.plot(z, yz)
plt.legend(['points','p'])
plt.show()

# Pn(z)=y0ℓ0(z)+y1ℓ1(z)+⋯+ynℓn(z)
