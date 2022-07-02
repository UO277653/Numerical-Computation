# -*- coding: utf-8 -*-
"""
Lab 8, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np
from numpy.linalg import norm

f = lambda x: np.cos(2*np.pi*x)
df  = lambda x: -2*np.pi*np.sin(2*np.pi*x)
d2f = lambda x: -4*np.pi**2*np.cos(2*np.pi*x)

# Order 2 formulas
a = -1.
b = 0.
h = 0.001

xpoints = np.arange(a + h,-h,h) # igual es a + h, b

res = np.ones(len(xpoints))

res = (1/(h**2)) * (f(xpoints + h) - 2*f(xpoints) + f(xpoints - h))

# Errors
Error_p = np.abs(d2f(xpoints)-res)

# Global errors
Error_G_f = norm(d2f(xpoints) - res)/norm(d2f(xpoints))
#vn = norm(v)

print('Relative error = ' + str(Error_G_f))
print("")
