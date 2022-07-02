# -*- coding: utf-8 -*-
"""
Lab 4, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import sympy as sym

def newton(f,df,x0,tol=1e-6,maxiter=100):
    n = 0
    k = 0
    x = x0
    
    while k < maxiter:
        n+=1
        k+=1
        x1 = x
        x = x1 - (f(x1)/df(x1))
        if(np.abs(x - x1) < tol):
            return x, n
    return x, n

x = sym.Symbol('x', real=True)
f_sim   = x**5 - 3 * x**2 + 1.6
df_sim  = sym.diff(f_sim,x)
f1   = sym.lambdify([x], f_sim,'numpy')
f1d  = sym.lambdify([x], df_sim,'numpy')

x1, n1 = newton(f1, f1d,-0.7)
x2, n2 = newton(f1, f1d,0.8)
x3, n3 = newton(f1, f1d,1.2)

print(x1, n1)
print(x2, n2)
print(x3, n3)

    


#%%