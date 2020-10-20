import numpy as np

def solve_heateq_fd(D, x_range, t_range, initial_func, bd_func, M, N):
    a, b = x_range
    T0, T = t_range
    
    # Discretization
    h = (b-a)/M
    k = (T-T0)/N
    x = np.linspace(a,b,M)
    t = np.linspace(T0,T,N)
    
    # Solution points
    w = np.zeros((M,N))
    
    # Initial conditions
    for i in range(M):
        w[i,0] = initial_func(x[i])
    
    # Boundary points
    bd_left, bd_right = bd_func
    for j in range(M):
        w[0,j] = bd_left(t[j])
        w[M-1,j] = bd_right(t[j])
        
    # Iteration matrix
    sigma = D*k/(h*h)
    s = 1.0 + 2.0*sigma
    P = M-2
    A = np.zeros((P,P))
    for i in range(0,P-1):
        A[i,i+1] = -sigma
    for i in range(P):
        A[i,i] = s
    for i in range(1,P):
        A[i,i-1] = -sigma

    for j in range(1,N):
        w[1,j-1] += sigma * w[0,j]
        w[M-1,j-1] += sigma * w[M-1,j]
        w[1:M-1,j:j+1] += np.dot(np.linalg.inv(A), w[1:M-1,j-1:j])
    #print(A)
    return w

# Problem
def initial_func(x):
    y = np.sin(np.pi*x)
    return y*y

def bd_left(t):
    return 0.0

def bd_right(t):
    return 0.0

xrange = (0,1.0)
trange = (0,0.1)

m = 1.0/0.1
n = 1.0/0.004
M = int(m)+1
N = int(n)+1

D = 1.0
w = solve_heateq_fd(D, xrange, trange, initial_func, (bd_left, bd_right), M, N)

# Plotting the solutions:

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, 1.0, M)
t = np. linspace(0, 0.1, N)
X, Y = np.meshgrid(t,x)

plt.tight_layout()
plt.title("1 D Heat Equation using backward difference method", fontsize = 14)
plt.xlabel("Time", fontsize = 14)
plt.ylabel("Distance", fontsize = 14)
ax.set_zlabel("Amplitude", fontsize = 14)
ax.plot_surface(X, Y, w)

plt.show()
