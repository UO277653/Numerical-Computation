# -*- coding: utf-8 -*-
"""
Lab 4, Exercise 2

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def bisection(f,a,b,tol=1e-6,maxiter=100):
    n = 0
    k = 0
    x = 0
    
    a1 = a
    b1 = b
    
    while k < maxiter:
        n+=1
        k+=1
        x1 = x
        x = (a1+b1)/2
        if(np.abs(x - x1) < tol):
            return x, n
        elif(f(a1)*f(x)<0):
            b1 = x
        elif(f(x)*f(b1)<0):
            a1 = x
        else:
            return x, n
    return x, n

f1 = lambda x : x**5 - 3*x**2 + 1.6

x1, n1 = bisection(f1,-0.7,-0.6)
x2, n2 = bisection(f1,0.8,0.9)
x3, n3 = bisection(f1,1.2,1.3)
print(x1, n1)
print(x2, n2)
print(x3, n3)
    


#%%