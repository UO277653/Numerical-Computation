# -*- coding: utf-8 -*-
"""
Lab 2, Exercise 2

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

def hornerv(p, x): # Polynomial, vector of points x0
    
    y = np.zeros_like(x)
    
    for i in range(len(x)):
        quotient = np.zeros_like(p)
        remainder = p[0]
        quotient[0] = remainder
        
        for j in range(1, len(p)):
            remainder = p[j] + x[i]*remainder
            quotient[j] = remainder
        y[i] = quotient[-1]
        
    return y # Values of P in the points of x

p = np.array([1., -1, 2, -3, 5, -2])

r = np.array([1., -1, -1, 1, -1, 0, -1, 1])

x1 = np.linspace(-1,1)
x = np.linspace(-1,1)

plt.figure()
plt.plot(x1, hornerv(p, x1))
plt.plot(x,0*x,'k')
plt.title("P")
plt.show()

plt.figure()
plt.plot(x1, hornerv(r, x1))
plt.plot(x,0*x,'k')
plt.title("R")
plt.show()


#%%