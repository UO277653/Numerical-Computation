# -*- coding: utf-8 -*-
"""
Lab 10, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def subs_backward(U,b):
    
    # Output x is the solution of the system Ux=b, being U a upper triangular 
    # matriz and b a column matrix.
    x = np.zeros(len(b))
    x[len(b)-1] = b[len(b)-1]/U[len(b)-1][len(b)-1]

    for i in range(len(b)-2,-1,-1):
        if U[i][i] == 0:
            continue
        else:
            s = 0
            for j in range(i+1,len(b)):
                s += U[i][j] * x[j]
            x[i] = (1/U[i][i])*(b[i] - s)
    
    return x

# System 1
U = np.array([[2, 1, 1], [0, 2, 1], [0, 0, 2]])
b = np.array([9, 4, 4])

print("------------- SYSTEM 1 -------------")
print("--- Data ---")
print("U")
print(U)
print("b")
print(b)
print("")

print("--- Solution ---")
print("x")
print(subs_backward(U,b))

# System 2
n = 5
np.random.seed(2)           
U = np.random.random((n,n)) 
U = np.triu(U) # make zero elements under the diagonal
b = np.random.random(n)

print("------------- SYSTEM 2 -------------")
print("--- Data ---")
print("U")
print(U)
print("b")
print(b)
print("")

print("--- Solution ---")
print("x")
print(subs_backward(U,b))

