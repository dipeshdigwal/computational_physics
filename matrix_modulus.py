from math import pow
def cofactor(i,j,a):
    x=len(a)
    b=[]
    for m in range(x):
        if(m!=i):
            c=[]
            for n in range(x):
                if(n!=j):
                    c.append(a[m][n])
            b.append(c)
    return(b)

def modulus(a):
    n=len(a)  #number of rows of matrix
    m=len(a[0])  #number of cols of matrix
    if(n!=m):
        print("invalid matrix")
        return(0)
    if(n==2):
        return((a[0][0]*a[1][1])-(a[0][1]*a[1][0]))
    else:
        s=0
        for i in range(m):
           s+=pow(-1,2+i)*a[0][i]*modulus(cofactor(0,i,a)) 
        return(s)

"""a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=cofactor(1,0,a)
n=len(b)
for i in range(n):
    for j in range(n):
        print(str(b[i][j]),end=" ")
    print("\n")"""
#a=[[1,1,1,2,1],[2,1,2,0,1],[3,1,3,2,3],[4,2,3,1,2],[5,2,3,1,1]]
#print(str(modulus(a)))