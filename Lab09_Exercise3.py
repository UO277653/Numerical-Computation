# -*- coding: utf-8 -*-
"""
Lab 9, Exercise 3

UO277653, Stelian Adrian Stanci
"""

#%%

# Exercise 3a

import numpy as np
import sympy as sym
from scipy.integrate import fixed_quad

def degree_of_precision(formula):
    
    k = 0 # Counter
    
    real = 0. 
    approx = 0.
    error = 0. # Real - approx
    
    while error < 10**-11:
        
        x = sym.Symbol('x', real=True) 
        f_sym = x ** k
        
        real = sym.integrate(f_sym,(x,a,b))
        
        xlamb = lambda x : x**k
        
        approx = formula(xlamb, a, b)[0]
        
        error = abs(approx - real)
        
        
        print('f(x) = x^' + str(k) + ' error: ', error)
        
        k+=1
    
    print('The degree of precision is: ', k-2)

a = 1
b = 3

def midpoint(f,a,b):
    
    approx = (b - a) * f((a+b)/2)
    
    return approx, a

def trapez(f,a,b):
    
    approx = ((b - a)/2) * (f(a) + f(b))
    
    return approx, a

def simpson(f,a,b):
    
    approx = ((b-a)/6) * (f(a) + 4*f((a+b)/2) + f(b))
    
    return approx, a

print('----  Midpoint rule  ----')
degree_of_precision(midpoint)
print()

print('----  Trapezoidal rule  ----')
degree_of_precision(trapez)
print()

print('----  Simpsons rule   ----')
degree_of_precision(simpson)
print()

print('----  fixed_quad  ----')
degree_of_precision(fixed_quad)
print()