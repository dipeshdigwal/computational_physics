from math import pow


# find the factorial of a integer n.
def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return(p)


# find sin of a number
def sin_2(x, n):
    s = 0
    for i in range(n):
        s += (pow(-1, i)*pow(x, (2*i)+1))/factorial((2*i)+1)
    return(s)
