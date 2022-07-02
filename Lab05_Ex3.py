# -*- coding: utf-8 -*-
"""
Lab 5, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

def incrementalSearch(f,a,b,n):
    
    intervals = np.zeros((n,2))
    dx = (b-a)/n
    c = 0
    for i in range (n):
        if(f(a + i * dx)*f(a + (i+1) * dx) < 0):
            intervals[c][0]=a + i * dx
            intervals[c][1]=a + (i+1) * dx
            c+=1;
    
    return intervals[:c,:]

def fixedPoint(g,x0,tol=1e-6,maxiter=200):
    n = 0
    k = 0
    x = x0
    x1 = 0
    
    while k < maxiter:
        k+=1
        n+=1
        
        x = g(x)
        
        if(np.abs(x - x1) < tol): # np.abs(x - x1)
             return x, n
        x1 = x
        
       # if(np.abs(x - x1) < tol):
           #     return x, n
    
    return x, n

g = lambda x : np.exp(-x)

f = lambda x: np.exp(-x) - x

# Using the function incrementalSearch for the interval [0,1] find a 0.1 length 
# interval that contains a zero of function f.

prec = 10
interval = incrementalSearch(f, 0, 1, prec)

print("There is a zero in ", interval)
print("\n")


# Taking as initial guess x0 the left border in the previous interval, compute 
# the fixed point of g. Remember that the fixed point method sequence is defined 
# by xk+1=g(xk).

x1, n1 = fixedPoint(g, interval[0][0])
print(x1, n1)
print("\n")

pf, n = fixedPoint(g, interval[0][0])

xspace = np.linspace(0., 1., 100)
plt.figure()
plt.plot(xspace,g(xspace),'r',xspace,xspace,'b',pf,pf,'bo')
plt.legend(['g','y=x'],loc='best')
plt.title('Zeros of f prime') 

plt.show()

f = lambda x: x - np.cos(x)
interval = incrementalSearch(f, 0, 1, prec)

print("There is a zero in ", interval)
print("\n")

g1 = lambda x : np.cos(x)
g2 = lambda x : 2*x - np.cos(x)
g3 = lambda x : x - (x - np.cos(x)) / (1 + np.sin(x))
g4 = lambda x : (9*x + np.cos(x)) / 10

plt.figure()
pf, n = fixedPoint(g1, interval[0][0])
plt.plot(xspace,g1(xspace),'r',xspace,g2(xspace),'purple',xspace,g3(xspace),'g',xspace,g4(xspace),'y',xspace,xspace,'b',pf,pf,'bo')
plt.legend(['g1','g2','g3','g4','y=x'],loc='best')
plt.title('Zeros of f prime') 

gx1, gn1 = fixedPoint(g1, interval[0][0])
gx2, gn2 = fixedPoint(g2, interval[0][0])
gx3, gn3 = fixedPoint(g3, interval[0][0])
gx4, gn4 = fixedPoint(g4, interval[0][0])

print("g1 ", gx1, gn1)
print("g2 ", gx2, gn2)
print("g3 ", gx3, gn3)
print("g4 ", gx4, gn4)