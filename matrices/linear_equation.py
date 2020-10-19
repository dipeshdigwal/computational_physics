from matrix_modulus import modulus


#function to convert a matrix to echleon form.
def echleon_mat(a,b): #arguments ax=b.
                        # a:matrix
                        # b:column matrix
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if(a[i][i] != 0):
                t = a[j][i]/a[i][i]
                for k in range(len(a[0])):
                    a[j][k] = a[j][k]-(t*a[i][k])
                b[j][0] -= t*b[i][0]
            else:
                w = list(a[i])
                for k in range(len(a[0])):
                    a[i][k] = a[j][k]
                    a[j][k] = w[k]
                o = b[i][0]
                b[i][0] = b[j][0]
                b[j][0] = o
           


#function to implement gaussian elemination method.
def gaussian_elemination(a,b): #ax=b
                            #   a:matrix
                            #   b:column matrix
    echleon_mat(a,b)   #convert a and b to echleon matrix.
    x = [0 for i in range(len(a[0]))]
    for i in range(len(a[0])-1, -1, -1):
        s = 0
        for j in range(i+1, len(a[0])):
            s += a[i][j]*x[j]
        if(a[i][i] != 0):
            x[i] = (b[i][0]-s)/a[i][i]
    return(x)


#function to form a cramers matrix.
def cramers_mat(j,a,b): #arguments j:column number
                                #a:matrix
                                #b:column matrix
    g = []
    g.append(list(a[0]))
    g.append(list(a[1]))
    g.append(list(a[2]))
    for i in range(len(b)):
        g[i][j] = b[i][0]
    return(g)


#function to apply cramers rule.
def cramers(a,b): #argument a:matrix on nth order.
                    #       b:column matrix.
    x = []
    for i in range(len(a[0])): #get the loop for number of columns in a matrix.
        x.append(modulus(cramers_mat(i,a,b))/modulus(a))
    return(x)


#example test case
#a = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
#b = [[14], [11], [11]]
#ax=b =>>> x=[[1],[2],[3]]