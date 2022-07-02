# -*- coding: utf-8 -*-
"""
Lab 3, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def triangular(A, b):
    At = np.copy(A);
    bt = np.copy(b);
    m, n = A.shape;
    
    for i in range(n):
        f = At[i][i-1] / At[i-1][i-1]
        At[i][i-1] = 0
        At[i][i] = At[i][i] - f*At[i-1][i]
        bt[i] = bt[i] - f*bt[i-1] # Error in this line: TypeError: can't multiply sequence by non-int of type 'numpy.float64'
        
    return At, bt

    # At each iteration
    # f = a[i][i-1] / a[i-1][i-1]
    # a[i][i-1] = 0
    # a[i][i] = a[i][i] - f*a[i-1][i]
    # b[i] = b[i] - f*[b[i-1]]
    
    
np.set_printoptions(precision = 2)   # only two decimals
np.set_printoptions(suppress = True) # do not use exponential format

n = 7 

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 

b = np.arange(n,2*n)*1.

At, bt = triangular(A,b)


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