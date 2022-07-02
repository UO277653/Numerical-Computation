# -*- coding: utf-8 -*-
"""
Lab 9, Exercise 1

UO277653, Stelian Adrian Stanci
"""

#%%

# Exercise 1a

import numpy as np
import sympy as sym

def midpoint(f,a,b):
    
    approx = (b - a) * f((a+b)/2)
    
    return approx

# Values for calculating
f = lambda x: np.log(x)
a = 1
b = 3

# We calculate the approximate value using the midpoint function
approxv = midpoint(f,a,b)

# We calculate the exact value using sympy
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,a,b))
exactv = float(Ie)

print('The approximate value is ',  approxv)
print('The exact value is       ',  exactv)
#%%

# Exercise 1b

import sympy as sym

def trapez(f,a,b):
    
    approx = ((b - a)/2) * (f(a) + f(b))
    
    return approx

# Values for calculating
f = lambda x: np.log(x)
a = 1
b = 3

approxv = trapez(f,a,b)

# We calculate the exact value using sympy
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,a,b))
exactv = float(Ie)

print('The approximate value is ',  approxv)
print('The exact value is       ',  exactv)
#%%

# Exercise 1c

import sympy as sym

def simpson(f,a,b):
    
    approx = ((b-a)/6) * (f(a) + 4*f((a+b)/2) + f(b))
    
    return approx

# Values for calculating
f = lambda x: np.log(x)
a = 1
b = 3

approxv = simpson(f,a,b)

# We calculate the exact value using sympy
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,a,b))
exactv = float(Ie)

print('The approximate value is ',  approxv)
print('The exact value is       ',  exactv)
#%%
