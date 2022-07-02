# -*- coding: utf-8 -*-
"""
Exercise 2 - Lab 1

Stelian Adrian Stanci - UO277653
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

def funExp(x, tol, maxNumSum):
    
    polynomial = 0. # Result
    factorial = 1.
    error = np.exp(x[0]) - polynomial
    i = 0
    
    while tol <= np.abs(error) and i < maxNumSum: # Stopping conditions
        term = x**i / factorial
        polynomial += term
        error = np.max(abs(term))
        factorial *= i+1
        i+=1
    return polynomial

tol=1.e-8
maxNumSum=100
x = np.linspace(-1,1) # We obtain the points
resPlot = funExp(x, tol, maxNumSum) # We invoke the function

plt.figure() # We prepare and plot the figure
plt.plot(x,np.exp(x),'y',linewidth=5,label='f')
plt.plot(x,resPlot,'b--',label='f approximation')
plt.legend()
plt.title("f approximation with McLaurin series")
plt.show()