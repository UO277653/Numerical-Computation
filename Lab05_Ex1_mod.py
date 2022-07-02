# -*- coding: utf-8 -*-
"""
Mark of the lab: 7

Lab 5, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

def secant(f,x0,x1,tol=1e-6,maxiter=100):
    n = 0
    k = 0
    x = 0
    
    while k < maxiter:
        k+=1
        n+=1
        
        x = x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
        x0 = x1
        x1 = x
        
        if(np.abs(x1 - x0) < tol):
             return x, n
    
    return x, n

f1 = lambda x : x**5 - 3*x**2 + 1.6

x1, n1 = secant(f1,-0.7,-0.6)
x2, n2 = secant(f1,0.8,0.9)
x3, n3 = secant(f1,1.2,1.3)

print(x1, n1)
print(x2, n2)
print(x3, n3)


xspace = np.linspace(-1,1.5,100)

r=np.zeros(3)

r[0]= x1
r[1]= x2
r[2]= x3

plt.figure()

plt.plot(xspace, f1(xspace),xspace,xspace*0,'k', r, r*0, 'ro')