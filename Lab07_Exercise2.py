# -*- coding: utf-8 -*-
"""
Lab 7, Exercise 2

UO277653, Stelian Adrian Stanci
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv('http://www.unioviedo.es/compnum/labs/new/cars.csv',sep=',')

# Step 1: extract weight and horsepower
weight = df['weight']
horsepower = df['horsepower']

# Step 2: Using np.polyfit calculate and plot the degree 1 fitting polynomial 
# using as variable x the weight and as variable y the horsepower.
polynomial = np.polyfit(weight, horsepower, 1)

polyvalPoints = np.polyval(polynomial, weight)

# Using np.polyval estimate the necessary power (horsepower) of a 3000 lbs car.
polyvalValue = np.polyval(polynomial, 3000)

print(str(int(polyvalValue)) + " horse power")
print("")
plt.figure()
plt.plot(weight, horsepower, 'o', weight, polyvalPoints, 'r-', 3000, polyvalValue, 'ro')
plt.show()

# mpg

mpg = df['mpg']

horsePoints = np.linspace(min(horsepower), max(horsepower))

polynomial = np.polyfit(horsepower, mpg, 2)

polyvalPoints = np.polyval(polynomial, horsePoints)

# With the horsepower obtained for the 3000 lbs car, estimate the miles per 
# gallon that this car could travel within a city using the approximation polynomial.
polyvalValue2 = np.polyval(polynomial, polyvalValue)

print(str(int(polyvalValue2)) + " mpg")
print("")

plt.figure()
plt.plot(horsepower, mpg, 'o')
plt.plot(horsePoints, polyvalPoints, 'r', polyvalValue, polyvalValue2, 'ro')
plt.show()