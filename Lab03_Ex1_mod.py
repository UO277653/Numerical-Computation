# -*- coding: utf-8 -*-
"""
Mark of the lab: 7 
    
Please, print all the examples.

Lab 3, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def triangular(A, b):
    At = np.copy(A);
    bt = np.copy(b);
    m, n = A.shape;
    
    for i in range(1, len(b)):
        f = At[i][i-1] / At[i-1][i-1]
        At[i][i-1] = At[i][i-1] - f*At[i-1][i-1]
        At[i][i] = At[i][i] - f*At[i-1][i]
        bt[i] = bt[i] - f*bt[i-1]
        
    return At, bt
    
    
np.set_printoptions(precision = 2)   # only two decimals
np.set_printoptions(suppress = True) # do not use exponential format


n = 7 

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 

b = np.arange(n,2*n)*1.

At, bt = triangular(A,b)

"""

n = 8 

np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T 

b = np.random.rand(n)
At, bt = triangular(A,b)
""" 

print("-------------  DATA  -------------")
print("A")
print(A)
print("b")
print(b)
print("-------  TRIANGULAR SYSTEM -------")
print("At")
print(At)
print("bt")
print(bt)
#%%