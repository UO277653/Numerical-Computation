# -*- coding: utf-8 -*-
"""
Lab 9, Exercise 2

UO277653, Stelian Adrian Stanci
"""

#%%

# Exercise 2a

import numpy as np
import sympy as sym

def comp_midpoint(f,a,b,n):
    
    h = (b-a)/n
    
    xi = a
    xiprev = 0
    ximed = 0
    
    approx = 0.
    
    for i in range(1, n + 1):
        
        xiprev = xi
        xi = a + i * h
        ximed = (xiprev + xi)/2
        approx += f(ximed)
    
    return h * approx

# Values for calculating
f = lambda x: np.log(x)
a = 1
b = 3
n = 5

# We calculate the approximate value using the midpoint function
approxv = comp_midpoint(f,a,b,n)

# We calculate the exact value using sympy
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,a,b))
exactv = float(Ie)

print('The approximate value is ',  approxv)
print('The exact value is       ',  exactv)
#%%

# Exercise 2b

import sympy as sym

def comp_trapz(f,a,b,n):
    
    h = (b-a)/n
    
    xi = a
    approx = 0.
    for i in range(1, n):
        
        xi = a + i * h
        approx += f(xi)
    
    return (h/2) * (f(a) + f(b)) + h * approx

# Values for calculating
f = lambda x: np.log(x)
a = 1
b = 3
n = 4

approxv = comp_trapz(f,a,b,n)

# We calculate the exact value using sympy
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,a,b))
exactv = float(Ie)

print('The approximate value is ',  approxv)
print('The exact value is       ',  exactv)
#%%

# Exercise 2c

import sympy as sym

def comp_simpson(f,a,b,n):
    
    h = (b-a)/n
    
    xi = a
    approx = 0.
    for i in range(1, n + 1):
        
        xiprev = xi
        xi = a + i * h
        ximed = (xiprev + xi)/2
        approx += f(xiprev) + 4 * f(ximed) + f(xi)
    
    return (h/6) * approx

# Values for calculating
f = lambda x: np.log(x)
a = 1
b = 3
n = 4

approxv = comp_simpson(f,a,b,n)

# We calculate the exact value using sympy
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,a,b))
exactv = float(Ie)

print('The approximate value is ',  approxv)
print('The exact value is       ',  exactv)
#%%