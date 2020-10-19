from gauss_siedel import *
err=10e-5
L=1.2
t=1
dx=0.4
dt=0.1
D=1
un0=0
ul0=0
u0j="x*(L-x)"
alp=((D*dt)/(dx*dx))
u=[[]]
step=int(L/dx)
step2=int(t/dt)

for j in range(step+2):
    u[0]+=[eval(u0j,{"x":j,"L":L})]
for n in range(step2):
    A=[]
    u_curr=[]
    B=[]
    for j in range(step):
        a=[]
        for i in range(step):
            if(i==j):
                a.append((1+(2*alp)))
            elif(i==(j-1) or i==(j+1)):
                a.append((-alp))
            else:
                a.append(0)
        A.append(a)
        u_curr.append(0)
        val=(alp*u[n][j])+((1-(2*alp))*u[n][j+1])+(u[n][j+2])
        if(j==0):
            B.append(val+(alp*un0))
        elif(j==step-2):
            B.append(val+(alp*ul0))
        else:
            B.append(val)
    #print(A)
    #print(B)
    u_curr=gauss_siedel(A,u_curr,B,err)
    u.append([un0]+u_curr+[ul0])
print(u)