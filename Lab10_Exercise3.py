# -*- coding: utf-8 -*-
"""
Lab 10, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def gaussjordan(A):
    
    # Output are the transformed upper triangular matrix U and vector c of a 
    # given matrix A and right hand side of the system b.
    
    I = np.eye(len(A))
    
    M = np.concatenate((A,I),axis=1)
    
    for k in range(0, len(A)):
        
        if(M[k][k] == 0):
            continue
        else:
            
            M[k] = M[k]/M[k][k]
            
            for i in range(0,len(A)):
                if(i != k):
                    M[i,:] = M[i,:] - (M[i][k] * M[k,:])
    
    return M[:,len(A):]

# System 1
A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])

print("Matrix")
print(A)
print("")

print("Inverse matrix")
print(gaussjordan(A))
print("")

# System 2
n = 5
np.random.seed(3)           
A = np.random.random((n,n)) 

print("Matrix")
print(A)
print("")

print("Inverse matrix")
print(gaussjordan(A))
print("")
