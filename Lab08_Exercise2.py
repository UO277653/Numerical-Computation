# -*- coding: utf-8 -*-
"""
Lab 8, Exercise 2

UO277653, Stelian Adrian Stanci
"""

import numpy as np
from numpy.linalg import norm
import sympy as sym

x = sym.Symbol('x', real=True)

f = lambda x: x**3 + x**2 + x
df  = lambda x: 3*x**2 + 2*x + 1

# Order 1 formulas
a = 0.
b = 1.
h = 0.02

xpoints = np.arange(a,b + h,h)

res = np.ones(len(xpoints))

res[0] = (f(xpoints[0]+h) - f(xpoints[0])) / h

for i in range(1, len(xpoints)):
    res[i] = (f(xpoints[i] + h) - f(xpoints[i] - h)) / (2 * h)
    
res[-1] = (f(xpoints[-1]) - f(xpoints[-1] - h)) / h

# Errors
Error_p = np.abs(df(xpoints)-res)

# Global errors
Error_G_f = norm(df(xpoints) - res)/norm(df(xpoints))

print('Error with order 1 approximation = ' + str(Error_G_f))

# Order 2 formulas
a = 0.
b = 1.
h = 0.02

xpoints = np.arange(a,b + h,h)

res = np.ones(len(xpoints))

res[0] = (1/(2*h)) * (-3 * f(xpoints[0]) + 4*f(xpoints[0] + h) - f(xpoints[0] + 2*h)) 

for i in range(1, len(xpoints)):
    res[i] = (f(xpoints[i] + h) - f(xpoints[i] - h)) / (2 * h)
    
res[-1] = (1/(2*h)) * (f(xpoints[-1] - 2*h) - 4*f(xpoints[-1] - h) + 3*f(xpoints[-1]))

# Errors
Error_p = np.abs(df(xpoints)-res)

# Global errors
Error_G_f = norm(df(xpoints) - res)/norm(df(xpoints))

print('Error with order 2 approximation = ' + str(Error_G_f))
print("")
