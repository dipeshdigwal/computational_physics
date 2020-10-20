def mat_mult(c, d):
    if(len(c[0]) == len(d)):
        res = [[0 for i in range(len(d[0]))] for j in range(len(c))]
        for i in range(len(c)):
            for k in range(len(d[0])):
                for j in range(len(c[0])):
                    res[i][k] += c[i][j]*d[j][k]
        return(res)


def row_operation(m, n, a, b):
    t = a[n][m]
    if(t != 0):
        if(m == n):
            for k in range(len(a)):
                a[m][k] /= t
            for k in range(len(b[0])):
                b[m][k] /= t
        else:
            for k in range(len(a)):
                #print(str(m)+" "+str(n)+" "+str(k))
                a[n][k] -= (t*a[m][k])
            for k in range(len(b[0])):
                b[n][k] -= t*b[m][k]


def row_echelon(a, b):
    for i in range(len(a)):
        # print(a)
        # print(b)
        row_operation(i, i, a, b)
        for j in range(len(a)):
            if(i != j):
                # print(a)
                # print(b)
                row_operation(i, j, a, b)


"""a=[[2,1,1],[1,2,1],[1,1,2]]
#b=[[7],[8],[9]]
c=[list(a[i]) for i in range(len(a))]
b=[[1,0,0],[0,1,0],[0,0,1]]
row_echelon()
print(b)
print(c)
print(mat_mult(c,b))"""
