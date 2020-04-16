from matrix_modulus import *
def echleon_mat():
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i][i]!=0):
                t=a[j][i]/a[i][i]
                for k in range(len(a[0])):
                    a[j][k]=a[j][k]-(t*a[i][k])
                b[j][0]-=t*b[i][0]
            else:
                w=list(a[i])
                for k in range(len(a[0])):
                    a[i][k]=a[j][k]
                    a[j][k]=w[k]
                o=b[i][0]
                b[i][0]=b[j][0]
                b[j][0]=o
            #print(a)
            #print(b)

def gaussian_elemination():
    x=[0 for i in range(len(a[0]))]
    for i in range(len(a[0])-1,-1,-1):
        s=0
        for j in range(i+1,len(a[0])):
            s+=a[i][j]*x[j]
        if(a[i][i]!=0):
            x[i]=(b[i][0]-s)/a[i][i]
    return(x)

def cramers_mat(j):
    g=[]
    g.append(list(a[0]))
    g.append(list(a[1]))
    g.append(list(a[2]))
    for i in range(len(b)):
        g[i][j]=b[i][0]
    return(g)

def cramers():
    x=[]
    for i in range(len(a[0])):
        x.append(modulus(cramers_mat(i))/modulus(a))
    return(x)
a=[[1,2,3],[3,1,2],[2,3,1]]
b=[[14],[11],[11]]
x2=cramers()
print(x2)
echleon_mat()
"""for i in range(len(a)):
    for j in range(len(a[0])):
        print(str(a[i][j]),end=' ')
    print()
print(b)"""
x=gaussian_elemination()
print(x)

#print(modulus(a))