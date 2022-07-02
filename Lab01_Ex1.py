# -*- coding: utf-8 -*-
"""
Exercise 1 - Lab 1

Stelian Adrian Stanci - UO277653
"""

import numpy as np
#%%
x0 = -0.4 # Point at which we calculate value
tol=1.e-8 # Tolerance
maxNumSum=100 # Maximum number of iterations

polynomial = 0. # Where we store the result
factorial = 1. 
error = np.exp(1) - polynomial # Initial error
i = 0 # Initialize and update counter

while tol <= np.abs(error) and i < maxNumSum: # Stopping conditions
    term = x0**i / factorial
    polynomial += term
    factorial *= i+1
    error = term
    i+=1

print('Function value in -0.4      = ', np.exp(x0))
print('Approximation value in -0.4 = ', polynomial)
print('Number of iterations        = ', i)
#%%