from reduced_row_echelon import mat_mult
def lu_decom():
    u=[[0 for i in range(len(a[0]))] for j in range(len(a))]
    l=[[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for k in range(i,len(a)):
            sum=0
            for j in range(i):
                sum+=l[i][j]*u[j][k]
            u[i][k]=a[i][k]-sum
        for k in range(i,len(a)):
            if(i==k):
                l[i][k]=1
            
            else:
                sum=0
                for j in range(i):
                    sum+=l[k][j]*u[j][i]
                l[k][i]=(a[k][i]-sum)/u[i][i]
    print(l)
    print(u)
    print(mat_mult(l,u))
a=[[3,4,2],[5,2,1],[2,3,2]]
lu_decom()
