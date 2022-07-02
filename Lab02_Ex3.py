# -*- coding: utf-8 -*-
"""
Lab 2, Exercise 3

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def horner(p, x0):
    
    quotient = np.zeros_like(p)
    remainder = p[0]
    quotient[0] = remainder
    
    for i in range(1, len(p)):
        remainder = p[i] + x0*remainder
        quotient[i] = remainder
        
    return quotient[:-1], remainder

def divisors(m):
    
    n = 0;
    m = np.abs(m)
    div = np.zeros(2*m)
    
    for i in range(1, m+1):
        if(m%i==0):
            div[n]=i
            div[n+1]=-i
            n+=2
            
    div = div[:n]
    
    return div

def roots(p):
    
    # We calculate divisors
    constant=p[-1]
    divisorsP = divisors(constant.__int__())
    roots = np.zeros(len(p))
    n=0
    # We try with each divisor and if root (remainder = 0) we:
    for i in range(len(divisorsP)):
        q, remain = horner(p, divisorsP[i])
        if(remain == 0):
            roots[n]=divisorsP[i]
            n+=1
            p=q
            
    return roots[:n]

print('Divisors of 6')
print(divisors(6))
print('Divisors of 18')
print(divisors(18))
print('Divisors of 20')
print(divisors(20))

p0 = np.array([1., 0, -1])
p1 = np.array([1., -3, -6, 8])
p2 = np.array([1., 2, -16, -2, 15])
p3 = np.array([1.,-5, -13, 53, 60])
p4 = np.array([1., 4, -56, -206, 343, 490])

print("\n")
print('Roots of p0')
print(roots(p0))
print("\n")
print('Roots of p1')
print(roots(p1))
print("\n")
print('Roots of p2')
print(roots(p2))
print("\n")
print('Roots of p3')
print(roots(p3))
print("\n")
print('Roots of p4')
print(roots(p4))
#%%