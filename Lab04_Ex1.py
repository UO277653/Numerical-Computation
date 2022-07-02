# -*- coding: utf-8 -*-
"""
Lab 4, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np

def incrementalSearch(f,a,b,n):
    
    intervals = np.zeros((n,2))
    dx = (b-a)/n
    c = 0
    for i in range (n):
        if(f(a + i * dx)*f(a + (i+1) * dx) < 0):
            intervals[c][0]=a + i * dx
            intervals[c][1]=a + (i+1) * dx
            c+=1;
    
    return intervals[:c,:]

f1 = lambda x : x**5 - 3 * x**2 + 1.6
x1 = np.linspace(-1,1.5)

f2 = lambda x : (x+2)*np.cos(2*x)

print("Intervals that contain f1 zeros")
print("")
print(incrementalSearch(f1, -1, 1.5, 25))
print("")
print("Intervals that contain f2 zeros")
print("")
print(incrementalSearch(f2, 0, 10, 100))
    


#%%