# -*- coding: utf-8 -*-
"""
Lab 3, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def triangular(A, b):
    At = np.copy(A);
    bt = np.copy(b);
    m, n = A.shape;
    
    for i in range(1, len(b)):
        f = At[i][0] / At[i-1][1]
        At[i][0] = At[i][0] - f*At[i-1][1]
        At[i][1] = At[i][1] - f*At[i-1][2]
        bt[i] = bt[i] - f*bt[i-1]
        
    return At, bt
    
def back_subs(At,bt):
    
    x = np.copy(bt)
    
    n1 = len(bt) - 2
    n2 = -1
    
    x[-1] = bt[-1]/At[-1][1]
    
    
    for k in range(n1,n2,-1):
        x[k] = (bt[k] - At[k][2]*x[k+1])/At[k][1]
    return x;
    
np.set_printoptions(precision = 2)   # only two decimals
np.set_printoptions(suppress = True) # do not use exponential format


n = 7 

Ar = np.zeros((n,3))
Ar[:,0] = np.concatenate((np.array([0]),np.ones((n-1),)))
Ar[:,1] = np.ones((n),)*3
Ar[:,2] = np.concatenate((np.ones((n-1),),np.array([0])))

b = np.arange(n,2*n)*1.

At, bt = triangular(Ar,b)
"""

""" 
"""
n = 8

np.random.seed(3)
Ar = np.zeros((n,3))
Ar[:,1] = np.random.rand(n)
Ar[:,0] = np.concatenate((np.array([0]),np.random.rand(n-1)))
Ar[0:n-1,2] = Ar[1:n,0]

b = np.random.rand(n)

At, bt = triangular(Ar,b)
""" 

print("-------------  DATA  -------------")
print("Ar")
print(Ar)
print("b")
print(b)
print("-------  TRIANGULAR SYSTEM -------")
print("At")
print(At)
print("------------  SOLUTION ------------")
print("x")
print(back_subs(At,bt))
#%%