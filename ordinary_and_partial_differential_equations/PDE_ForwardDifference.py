#!/usr/bin/env python3

import numpy as np

def solve_heateq_fd(D, x_range, t_range, ic_func, bc_func, M, N):
    a, b = x_range
    T0, T = t_range
    
    # discretization
    h = (b-a)/M
    k = (T-T0)/N
    x = np.linspace(a, b, M)
    t = np.linspace(T0, T, N)
    #print(x)
    
    # solution points
    w = np.zeros((M,N))
    
    # initial condition values
    for i in range(M):
        w[i,0] = ic_func(x[i])
        
    # boundary points
    bc_left, bc_right = bc_func
    for j in range(M):
        w[0,j] = bc_left(t[j])
        w[M-1,j] = bc_right(t[j])
    
    # Construct iteration matrix
    sigma = D*k/(h*h)
    s = 1.0 - 2.0*sigma
    P = M-2
    A = np.zeros((P,P))       
    for i in range(P):
        A[i,i] = s
    for i in range(0,P-1):
        A[i,i+1] = sigma
    for i in range(1,P):
        A[i,i-1] = sigma
    #print(A.shape)
    #print(w[1:M-1,1:2].shape)
    
    for j in range(0,N-1):
        w[1:M-1,j+1:j+2] = np.dot(A, w[1:M-1,j:j+1])
        w[1,j+1] += sigma * w[0,j]
        w[M-1,j+1] += sigma * w[M-1,j]
        
    return w


# problem definition
def ic_func(x):
    y = np.sin(np.pi*x)
    return y*y

def bc_left(t):
    return 0.0

def bc_right(t):
    return 0.0

xrange = (0, 1.0)
trange = (0, 0.1)

m = 1.0/0.1
n = 1.0/0.004
M = int(m)+1
N = int(n)+1

D = 1.0
w = solve_heateq_fd(D, xrange, trange, ic_func, (bc_left, bc_right), M, N)

# Plot the solutions
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, 1.0, M)
t = np.linspace(0, 0.1, N)
X, Y = np.meshgrid(t, x)
ax.plot_surface(X, Y, w)

plt.show()
