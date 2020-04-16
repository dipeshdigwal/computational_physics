from math import atan,cos,sin,fabs,pi,degrees
def mat_disp(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end='\t')
        print()
    print()
def mat_mult(c,d):
    if(len(c[0])==len(d)):
        mat=[]
        for i in range(len(c)):
            s=[]
            for k in range(len(d[0])):
                sum=0
                for j in range(len(c[0])):
                    sum+=c[i][j]*d[j][k]
                s.append(sum)
            mat.append(s)
        return(mat)

def transpose(mat):
    out=[[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            out[j][i]=mat[i][j]
            #print(mat[i][j])
    return(out)
def jacobi(a):
    global flag
    maxi=a[0][1]
    max_i=0
    max_j=1
    limit=1e-10
    if(maxi<limit):
        maxi=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            """if(a[i][j]<limit):
                a[i][j]=0
                a[j][i]=0
            """
            if(fabs(a[i][j])>fabs(maxi)):
                maxi=a[i][j]
                max_i=i
                max_j=j
    if(fabs(maxi)<limit):
        flag=-1
        mat_disp(a)
        return(a)
    i=max_i
    j=max_j
    x=fabs(a[j][j]-a[i][i])
    if(x!=0):
        theta=atan((2*a[i][j])/x)/2
    else:
        theta=pi/4
    c=cos(theta)
    s=sin(theta)
    r=[]
    for m in range(len(a)):
        d=[]
        for n in range(len(a)):
            if(m==n):
                if(m==i or m==j):
                    d.append(c)
                else:
                    d.append(1)
            elif(m==i and n==j):
                d.append(s)
            elif(m==j and n==i):
                d.append(-s)
            else:
                d.append(0)
        r.append(d)
    r_inv=transpose(r)
    #mat_disp(a)
    a=mat_mult(r_inv,mat_mult(a,r))
    print("-"*100)
    print("i:"+str(i)+" "+"j:"+str(j))
    print("theta : "+str(degrees(theta)))
    mat_disp(a)
    mat_disp(r)
    #mat_disp(r_inv)
    print("-"*100)
    return(a)

a=[[1,2**(1/2),2],[2**(1/2),3,2**(1/2)],[2,2**(1/2),1]]
iterations=10
flag=1
for w in range(iterations):
    a=jacobi(a)
    if(flag==-1):
        break
#mat_disp(transpose(a))