# -*- coding: utf-8 -*-
"""
Mark of the lab: 7

Lab 8, Exercise 1

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

f = lambda x: np.log(x)
df = lambda x: 1/x

# Example with h = 0.1
a = 1.
b = 2.
h = 0.1

xpoints = np.arange(a,b + h,h)

# Progressive vector
xp = np.arange(a,b,h) # can also use linspace

df_p = (f(xp + h) - f(xp)) / h
# Regressive vector
xr = np.arange(a+h,b+h,h)

df_r = (f(xr) - f(xr - h)) / h
# Central vector
xc = np.arange(a+h,b,h)

df_c = (f(xc + h) - f(xc - h)) / (2 * h)

# plot xp, xr and xc
plt.figure()
plt.grid()
plt.plot(xpoints, df(xpoints),'--')
plt.plot(xp, df_p)
plt.plot(xr, df_r)
plt.plot(xc, df_c)
plt.legend(['df', 'df_f', 'df_b', 'df_c'],loc='best')
plt.title('Derivative of f(x) = ln(x) and its approximations with h = 0.1')
plt.show()

# Errors
Error_p = np.abs(df(xp)-df_p)
Error_r = np.abs(df(xr)-df_r)
Error_c = np.abs(df(xc)-df_c)

plt.figure()
plt.grid()
plt.plot(xp, Error_p, 'o')
plt.plot(xr, Error_r, 'o')
plt.plot(xc, Error_c, 'o')
plt.legend(['df_f', 'df_b', 'df_c'],loc='best')
plt.title('Errors with h = 0.1')
plt.show()

# Global errors
Error_G_f = norm(df(xp) - df_p)/norm(df(xp))
Error_G_b = norm(df(xr) - df_r)/norm(df(xr))
Error_G_c = norm(df(xc) - df_c)/norm(df(xc))
#vn = norm(v)

print('h = ' + str(h))
print('Error_G_f = ' + str(Error_G_f))
print('Error_G_b = ' + str(Error_G_b))
print('Error_G_c = ' + str(Error_G_c))
print("")

# Example with h = 0.01
a = 1.
b = 2.
h = 0.01

xpoints = np.arange(a,b + h,h)

# Progressive vector
xp = np.arange(a,b,h) # can also use linspace

df_p = (f(xp + h) - f(xp)) / h
# Regressive vector
xr = np.arange(a+h,b+h,h)

df_r = (f(xr) - f(xr - h)) / h
# Central vector
xc = np.arange(a+h,b,h)

df_c = (f(xc + h) - f(xc - h)) / (2 * h)

# plot xp, xr and xc
plt.figure()
plt.grid()
plt.plot(xpoints, df(xpoints),'--')
plt.plot(xp, df_p)
plt.plot(xr, df_r)
plt.plot(xc, df_c)
plt.legend(['df', 'df_f', 'df_b', 'df_c'],loc='best')
plt.title('Derivative of f(x) = ln(x) and its approximations with h = ' + str(h))
plt.show()

# Errors
Error_p = np.abs(df(xp)-df_p)
Error_r = np.abs(df(xr)-df_r)
Error_c = np.abs(df(xc)-df_c)

plt.figure()
plt.grid()
plt.plot(xp, Error_p, 'o')
plt.plot(xr, Error_r, 'o')
plt.plot(xc, Error_c, 'o')
plt.legend(['df_f', 'df_b', 'df_c'],loc='best')
plt.title('Errors with h = ' + str(h))
plt.show()

# Global errors
Error_G_f = norm(df(xp) - df_p)/norm(df(xp))
Error_G_b = norm(df(xr) - df_r)/norm(df(xr))
Error_G_c = norm(df(xc) - df_c)/norm(df(xc))

print('h = ' + str(h))
print('Error_G_f = ' + str(Error_G_f))
print('Error_G_b = ' + str(Error_G_b))
print('Error_G_c = ' + str(Error_G_c))
print("")