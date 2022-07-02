# -*- coding: utf-8 -*-
"""
Lab 3, Exercise 2

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

    # At each iteration
    # f = a[i][i-1] / a[i-1][i-1]
    # a[i][i-1] = 0
    # a[i][i] = a[i][i] - f*a[i-1][i]
    # b[i] = b[i] - f*[b[i-1]]
    
def back_subs(At,bt):
    
    x = np.copy(bt)
    
    n1 = len(bt) - 2
    n2 = -1
    
    x[-1] = bt[-1]/At[-1][-1]
    
    
    for k in range(n1,n2,-1):
        x[k] = (bt[k] - At[k][k+1]*x[k+1])/At[k][k]
    return x;
    
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
print("x")
print(back_subs(At,bt))
#%%