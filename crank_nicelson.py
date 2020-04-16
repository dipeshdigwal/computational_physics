from math import ceil

def gauss_siedel(A,Y,B,err):
	e=0
	for j in range(len(Y)):
		s1=0
		for k in range(1,len(Y)+1):
			if(k!=(j+1)):
				s1+=A[j][k-1]*Y[k-1]
		Y_old=Y[j]
		Y[j]=(B[j]-s1)/A[j][j]
		e+=(Y[j]-Y_old)/len(Y)
	#print(Y)
	if(e<err):
		return(Y)
	return(gauss_siedel(A,Y,B,err))
	
"""A=[[1,2],[1,4]]
Y=[0,0]
B=[4,8]
err=10e-5
print(gauss_siedel(A,Y,B,err))"""

err=10e-5
L=10
t=10
x_init=0
t_init=0
dx=0.1
D=0.2
dt=0.1
alpha=(D*dt)/(2*dx*dx)
un0=0
unl=0
u0j="x*(L-x)"
step_x=ceil(L/dx)
step_t=ceil(t/dt)
u=[[]]
#print(step_x)
#print(step_t)
f=open("points.txt","w")
for j in range(step_x+1):
	w=eval(u0j,{"x":(x_init+(dx*j)),"L":L})
	u[0].append(w)
	#f.write(str(x_init+(dx*j))+" 0 "+str(w)+"\n")
#print(u)
for n in range(1,step_t+1):
	A=[]
	u_curr=[]
	B=[]
	for j in range(1,step_x):
		l=[]
		for k in range(1,step_x):
			if(k==j):
				l.append(1+(2*alpha))
			elif(k==(j-1) or k==(j+1)):
				l.append(-1*alpha)
			else:
				l.append(0)
		A.append(l)
		u_curr.append(0)
		val=(alpha*u[n-1][j-1])+((1-(2*alpha))*u[n-1][j])+u[n-1][j+1]
		if(j==1):
			B.append(val+(alpha*un0))
		elif(j==(step_x-1)):
			B.append(val+(alpha*unl))
		else:
			B.append(val)
	#print(A)
	#print(B)
	u.append([un0]+gauss_siedel(A,u_curr,B,err)+[unl])
#print(u)
for n in range(len(u)):
	for j in range(len(u[0])):
		f.write(str(x_init+(j*dx))+" "+str(t_init+(n*dt))+" "+str(u[n][j])+"\n")
		#f.write(str(x_init+(j*dx))+" "+str(u[n][j])+"\n")

"""
for j in range(len(u[0])):
	f.write(str(x_init+(j*dx))+" "+str(u[-1][j])+"\n")
"""
f.close()
