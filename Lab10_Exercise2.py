# -*- coding: utf-8 -*-
"""
Lab 10, Exercise 2

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def triang(A,b):
    
    # Output are the transformed upper triangular matrix U and vector c of a 
    # given matrix A and right hand side of the system b.
    
    for k in range(0, len(b)):
        if(A[k][k] == 0):
            continue
        else:
            for i in range(k+1,len(b)):
                f = A[i][k]/A[k][k]
                b[i] = b[i] - f*b[k]
                for j in range(len(A)):
                    U[i][j] = U[i][j] - f*U[k][j]
    
    return U, b

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
U = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([2., 4, 6])

print("------------- SYSTEM 1 -------------")
print("              --DATA--       ")
print("U")
print(U)
print("b")
print(b)
print("")

print("         --TRIANGULARIZATION--       ")
U, c = triang(U,b)
print("")
print("U")
print(U)
print("")
print("c")
print(c)
print("")
print("        --BACKWARD SUBSTITUTION--       ")
print("x")
print(subs_backward(U,b))

# System 2
n = 5
np.random.seed(3)           
U = np.random.random((n,n)) 
b = np.random.random((n,))

print("------------- SYSTEM 2 -------------")
print("              --DATA--       ")
print("U")
print(U)
print("b")
print(b)
print("")

print("         --TRIANGULARIZATION--       ")
U, c = triang(U,b)
print("")
print("U")
print(U)
print("")
print("c")
print(c)
print("")
print("        --BACKWARD SUBSTITUTION--       ")
print("x")
print(subs_backward(U,b))
