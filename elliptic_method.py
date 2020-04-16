def gauss_siedel(A,y,B,err):
	e=0
	for j in range(len(y)):
		s=0
		for k in range(len(y)):
			if(j!=k):
				s+=A[j][k]*y[k]
		y_prev=y[j]
		y[j]=(B[j]-s)/A[j][j]
		e+=(y[j]-y_prev)/len(y)
	#print(y)
	if(e<err):
		return(y)
	return(gauss_siedel(A,y,B,err))
	
"""A=[[-4,1,0,0],[1,-4,1,0],[0,1,-4,1],[0,0,1,-4]]
y=[0,0,0,0]
B=[1,2,3,4]
err=10e-5
print(gauss_siedel(A,y,B,err))
"""

err=10e-5
x_init=0
y_init=0
x_end=4
y_end=4
h=0.25
f="1"
f0y=0
fay=0
fx0=0
fxb=100
step_x=int((x_end-x_init)/h)-1
step_y=int((y_end-y_init)/h)-1
print(step_x)
print(step_y)
A=[]
y=[]
B=[]
y_sol=[]
for i in range(step_y+2):
	y_sol.append([f0y])
for i in range(step_x*step_y):
	m=int((i)/step_y)+1
	n=((i)%step_y)+1
	#print([m,n])
	s=[]
	for j in range(step_x*step_y):
		if(i==j):
			s.append(-4)
		elif(j==(i+1) or j==(i-1)):
			s.append(1)
		elif(j==(i+step_y) or j==(i-step_y)):
			s.append(1)
		else:
			s.append(0)
	A.append(s)
	y.append(0)
	B.append((h*h)*eval(f,{'x':x_init+(m*h),'y':y_init+(n*h)}))
	if((m-1)==0):
		B[i]-=f0y
	if((n-1)==0):
		B[i]-=fx0
	if((m+1)==(step_x+1)):
		B[i]-=fay
	if((n+1)==(step_y+1)):
		B[i]-=fxb
#print(A)
#print(B)
ans=gauss_siedel(A,y,B,err)
#print(ans)
#print(y_sol)
for i in range(len(ans)):
	m=int(i/step_y)+1
	n=(i%step_y)+1
	if(n==1):
		y_sol[n-1].append(fx0)
	y_sol[n].append(ans[i])
	if(n==step_x):
		y_sol[n+1].append(fxb)
#print(y_sol)
for i in range(step_y+2):
	y_sol[i].append(fay)
print(y_sol)
fil=open("point.txt","w")
for i in range(len(y_sol)):
	for j in range(len(y_sol[1])):
		m=x_init+(h*j)
		n=y_init+(h*i)
		fil.write(str(m)+" "+str(n)+" "+str(y_sol[i][j])+"\n")
		
fil.close()
