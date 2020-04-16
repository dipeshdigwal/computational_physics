def gauss_siedel(A,Y,B,limit):
    while(True):
        err=0
        y=[]
        for j in range(len(Y)):
            s1=0
            s2=0
            for k in range(len(Y)):
                if(k<(j)):
                    s1+=A[j][k]*Y[k]
                elif(k>j):
                    s2+=A[j][k]*Y[k]
            y.append(Y[j])
            Y[j]=(B[j]-s1-s2)/A[j][j]
            err+=(Y[j]-y[j])/len(Y)
        #print(Y)
        if(err<limit):
            return(Y)

"""err=10e-5
h=0.25
t_y0=0
t_x0=0
t_ye=100
t_xe=0
ran_x=[0,1]
ran_y=[0,1.5]
steps=int((((ran_x[1]-ran_x[0])/h)-1)*(((ran_y[1]-ran_y[0])/h)-1))
A=[]
T=[]
B=[]
print(steps)
for i in range(steps):
    l=[]
    for j in range(steps):
        if(j==(i-1) or j==(i+1) or j==(i-5) or j==(i+5)):
            l.append(1)
        elif(j==i):
            l.append(-4)
        else:
            l.append(0)
    A.append(l)
    T.append(0)
    m=int(i/(int(((ran_y[1]-ran_y[0])/h)-1)))+1
    n=(i%(int(((ran_y[1]-ran_y[0])/h)-1)))+1
    #print(str(m)+" "+str(n))
    if(n==(int(((ran_y[1]-ran_y[0])/h)-1))):
        B.append(-t_ye)
    else:
        B.append(0)
#print(A)
#print(T)
#print(B)
gauss_siedel(A,T,B,err)"""