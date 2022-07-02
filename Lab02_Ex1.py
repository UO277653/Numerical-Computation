# -*- coding: utf-8 -*-
"""
Mark of the lab: 7
    
Lab 2, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def horner(p, x0): # Polynomial, point x0
    
    quotient = np.zeros_like(p)
    remainder = p[0]
    quotient[0] = remainder
    
    for i in range(1, len(p)):
        remainder = p[i] + x0*remainder
        quotient[i] = remainder
        
    return quotient[:-1], remainder # Numpy array that contains the coefficients of Q 

p = np.array([1.,2,1])
x0 = 1.

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.

p2 = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x2 = -1.

c, r = horner(p, x0)

c1, r1 = horner(p1, x1)

c2, r2 = horner(p2, x2)

print("Q coefficients =  ", c)
print("P0(1) =  ", r)
print("\n")
print("Q coefficients =  ", c1)
print("P1(1) =  ", r1)
print("\n")
print("Q coefficients =  ", c2)
print("P2(-1) =  ", r2)

#%%