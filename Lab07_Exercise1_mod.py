# -*- coding: utf-8 -*-
"""
Mark of the lab: 7

Lab 7, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

def approx1(f,d,a,b,n):
    
    # d is the degree of the polynomial, n equispaced points of the function f
    # in interval [a,b]
    # does not return anything
    
    # Step 1
    x = np.linspace(a,b,n)
    y = f(x)
    
    # Step 2
    V = np.ones((n, d + 1))
    
    for i in range(n):
        for j in range(d + 1):
            
            V[i][j] = x[i] ** j
            
    C = np.dot(V.T,V)
    
    # Print coefficient matrix
    print("Coefficient matrix")
    print(C)
    print("")
    
    d = np.dot(V.T,y)
    
    print("Right hand side term")
    print(d)
    print("")
    
    # Step 3
    p = np.linalg.solve(C,d)
    
    print("System solution")
    print(p)
    print("")
    
    # Step 4
    p = p[::-1]
    
    # Step 5
    xp = np.linspace(a,b, 50)
    polyvalPoints = np.polyval(p, xp)
    
    # Step 6
    plt.figure()
    plt.plot(x, y, 'ro', xp, polyvalPoints)
    plt.legend(['points','fitting polynomial'],loc='best')
    plt.show()

np.set_printoptions(precision = 2)   # only 2 fractionary digits
np.set_printoptions(suppress = True) # do not use exponential notation

# Example 1
f1 = lambda x : np.sin(x)
approx1(f1, 2, 0, 2, 5)

# Example 2
f2 = lambda x : np.cos(np.arctan(x)) - np.log(x + 5)
approx1(f2, 4, -2, 0, 10)