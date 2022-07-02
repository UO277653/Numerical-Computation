# -*- coding: utf-8 -*-
"""
Lab 7, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def approx2(f,d,a,b):
    
    # Step 1
    n = 100
    x = np.linspace(a,b,n)
    y = f(x)
    
    # Step 2
    I = np.ones((d + 1, d + 1))
    
    for i in range(d + 1):
        for j in range(d + 1):
            
            aux = lambda x: x **(i+j)
            I[i][j] = quad(aux,a,b)[0]
            
    
    # Print coefficient matrix
    print("Coefficient matrix")
    print(I) # C
    print("")
    
    g = lambda x: x * f(x)
    
    r = np.ones(d+1)
    
    #r = np.ones(I.T)
    
    for i in range(d + 1):
        g = lambda x: x**i * f(x)
        r[i] = quad(g, a, b)[0]
    
    print("Right hand side term")
    print(r)
    print("")
    
    # Step 3
    p = np.linalg.solve(I,r) # C
    
    # Step 4
    p = p[::-1]
    
    print("System solution")
    print(p)
    print("")
    
    # Step 5
    xp = np.linspace(a,b, n)
    polyvalPoints = np.polyval(p, xp)
    
    # Step 6
    plt.figure()
    plt.plot(x, y, 'r', xp, polyvalPoints)
    plt.legend(['function','fitting polynomial'],loc='best')
    plt.show()

np.set_printoptions(precision = 2)   # only 2 fractionary digits
np.set_printoptions(suppress = True) # do not use exponential notation

# Example 1
f1 = lambda x : np.sin(x)
approx2(f1, 2, 0, 2)

# Example 2
f2 = lambda x : np.cos(np.arctan(x)) - np.log(x + 5)
approx2(f2, 4, -2, 0)