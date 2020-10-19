#!/usr/bin/env python3
import numpy as np

# Given constants with units
u = 2500 # m/s
M = 2.8 * pow(10, 6) # Kg
m = 1.3 * pow(10, 4) # Kg
g = 9.8 # m/s^2
v = 340 # m/s

# From the given equation,
# we can write a function of t and find its root
def f(t):
    f = u*np.log(M/(M-m*t)) - g*t - v
    return f

# Derivative of f(t)
def Df(t):
    Df = (u*m*(M - m*t)/(M - m*t)**2) - g
    return Df

# We use Newton-Raphson method to find the root
# t0 is our initial guess
def Newton_Raph(f, Df, t0, epsilon, max_iter):
    tn = t0
    for i in range(0,max_iter):
        if abs(f(tn)) < epsilon:
            print("The solution is found after ", i, " iterations.")
            return tn
        if Df(tn) == 0:
            print("The derivative is zero. No solution found.")
            return None
        tn = tn - (f(tn)/Df(tn))
    print("Maximum iterations were executed. No solutions found.")
    return None

# Calculating for given values
t0 = 0
epsilon = 1e-10
max_iter = 100
root = Newton_Raph(f, Df, t0, epsilon, max_iter)
print("The rocket reaches the speed of sound ",root, " seconds after launching.")
