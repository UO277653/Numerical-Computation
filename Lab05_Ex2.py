# -*- coding: utf-8 -*-
"""
Lab 5, Exercise 2

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import scipy.optimize as op

# Declaring the variable
x = sym.Symbol('x', real=True)

# Calculating the function and its derivatives
f_sim = x**2 + sym.log(2*x+7) * sym.cos(3*x) + 0.1
df_sim  = sym.diff(f_sim,x)
d2f_sim  = sym.diff(df_sim,x)
d3f_sim  = sym.diff(d2f_sim,x)

# Lambdifying the functions
f   = sym.lambdify([x], f_sim,'numpy') 
df  = sym.lambdify([x], df_sim,'numpy')
d2f = sym.lambdify([x], d2f_sim,'numpy')
d3f = sym.lambdify([x], d3f_sim,'numpy')

# Calculating the points of the space we will represent the graph
xspace = np.linspace(-1,3,100)

# Plotting the derivative of f
plt.figure()
plt.plot(xspace,df(xspace),xspace,xspace*0,'k')
plt.title('Derivative of f') 
plt.show()

# Calculating the zeros of f
xspace = np.linspace(-2,4,100)
x0 = np.array([-0.7, -0.1, 0.9, 2., 2.7])
zeros = op.newton(df,x0,fprime=d2f,tol=1.e-6,maxiter=100)

minima = np.array([])
maxima = np.array([])

for i in range(0, len(zeros)):
    if i % 2 == 0:
        minima = np.append(minima,zeros[i])
    else:
        maxima = np.append(maxima,zeros[i])
    
plt.figure()
plt.plot(xspace,f(xspace),xspace,xspace*0,'k',maxima,f(maxima),'ro',minima,f(minima),'go')
plt.show()

print("EXTREMES")
print(zeros)

# Calculate inflexion points

xspace = np.linspace(-1,4,100)

plt.figure()
plt.plot(xspace,d2f(xspace),xspace,xspace*0,'k')
plt.title('Second derivative of f') 
plt.show()

x0 = np.array([-0.7, 0.3, 1.3, 2.3, 3.4]) # With these points it works
zeros = op.newton(d2f,x0,fprime=d3f,tol=1.e-6,maxiter=100)

print("INFLEXION POINTS IN [-1,4]")
print(zeros)

plt.figure()
plt.plot(xspace,f(xspace),xspace,xspace*0,'k',zeros,f(zeros),'bo')
plt.show()