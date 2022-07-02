# -*- coding: utf-8 -*-
"""
Lab 11, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np

np.set_printoptions(precision = 8)   
np.set_printoptions(suppress = True)

def jacobi(A,b,tol,maxiter=1000):
    
    x = np.zeros_like(b) # Initial guesses
    xp = np.zeros_like(b)
    num_iter = 0
    
    for k in range(maxiter):
        
        num_iter += 1
        
        for i in range(len(b)):
            
            temp1 = 0
            temp2 = 0
            
            for j in range(i):
                temp1 += A[i][j] * xp[j]
                
            for j in range(i+1,len(b)):
                temp2 += A[i][j] * xp[j]
                
            x[i] = (1/A[i][i]) * (b[i] - temp1 - temp2)
            
        if(np.linalg.norm(x-xp) < tol):
            return x, num_iter
        
        xp = np.copy(x) # Updating xp vector
        
    # As output, give the solution x and the number of iterations num_iter
    
    return x, num_iter

# System 1
A = np.array([[5.,1,-1,-1],[1,4,-1,1],[1,1,-5,-1],[1,1,1,-4]])
b = np.array([1.,1,1,1])

tol = 1.e-6

approx, iterations = jacobi(A,b,tol)
xs = np.linalg.solve(A,b) # For checking that the solution is good

print("------------- System 1 -------------")
print("---- Data ----")
print("A")
print(A)
print("b")
print(b)
print("")
print("---- Solution ----")
print(str(iterations) + " iterations")
print("")
print("approximate x")
print(approx)
print("")
print("exact x")
print(xs)
print("")

# System 2
n = 9 
A1 = np.diag(np.ones(n))*2 
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T 
b = np.concatenate((np.arange(1,6),np.arange(4,0,-1)))*1.

tol = 1.e-6

approx, iterations = jacobi(A,b,tol)
xs = np.linalg.solve(A,b) # For checking that the solution is good

print("------------- System 2 -------------")
print("---- Data ----")
print("A")
print(A)
print("b")
print(b)
print("")
print("---- Solution ----")
print(str(iterations) + " iterations")
print("")
print("approximate x")
print(approx)
print("")
print("exact x")
print(xs)
print("")