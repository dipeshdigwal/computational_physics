#!/usr/bin/env python3
import numpy as np

# Function to be integrated
def erf(t):
    erf = (2/np.sqrt(np.pi))*np.exp(-pow(t,2))
    return erf
    
# We use Composite Simpson's method to calculate the integral
def simpson(f, a, b, m):
    h = (b-a)/(2*m)
    x = np.linspace(a, b, 2*m +1)
    sum1 = 0
    sum2 = 0
    k = 0
    l = 0
    for i in range(1, m+1):
        k = x[2*i-1]
        sum1 += f(k)
    for i in range(1, m):
        l = x[2*i]
        sum2 += f(l)
    S = h/3 * (f(a) + f(b) + 4*sum1 + 2*sum2)
    return round(S, 10)

# Calculating for given values
a = 0
b = 1.0
m = 20
integral = simpson(erf, a, b, m)
print("The approximate value of erf(",b,") using Composite Simpson's method is ",integral)
