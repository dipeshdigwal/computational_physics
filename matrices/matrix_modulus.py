from math import pow


def cofactor(i, j, a):  # (i,j) indices of the element
    # a : given matrix
    x = len(a)
    b = []
    for m in range(x):
        if(m != i):
            c = []
            for n in range(x):
                if(n != j):
                    c.append(a[m][n])
            b.append(c)
    return(b)


def modulus(a):
    n = len(a)  # number of rows of matrix
    m = len(a[0])  # number of cols of matrix
    if(n != m):
        print("invalid matrix")
        return(0)
    if(n == 2):
        return((a[0][0]*a[1][1])-(a[0][1]*a[1][0]))
    else:
        s = 0
        for i in range(m):
            s += pow(-1, 2+i)*a[0][i]*modulus(cofactor(0, i, a))
        return(s)
