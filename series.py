from math import pow,sin,pi
def factorial(n):
    p=1
    for i in range(2,n):
        p*=i
    return(p)

def sin_2(x,n):
    s=0
    for i in range(n):
        s+=(pow(-1,i)*pow(x,(2*i)+1))/factorial((2*i)+1)
    return(s)

x=pi/20
n=2
k=(sin(x)-sin_2(x,n))/sin(x)
print(str(k))