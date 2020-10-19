def f(k,l):
	if(k==0):
		return(1)
	elif(k==1):
		return(a[0][0]-l)
	return(((a[k-1][k-1]-l)*f(k-1,l))-((a[k-2][k-1]**2)*f(k-2,l)))
def givens():
	mi=-10
	ma=10
	print("l\t0\t1\t2\t3")
	for l in range(int(mi),int(ma)+1):
		print(l,end="\t")
		for k in range(len(a)+1):
			print(f(k,l),end="\t")
		print()
		
#a=[[1,6**(1/2),0],[6**(1/2),3,-(2**(1/2))],[0,-(2**(1/2)),1]]
x=6**(1/2)
y=2**(1/2)
a=[[1,x,0],[x,3,-y],[0,-y,1]]
givens()
