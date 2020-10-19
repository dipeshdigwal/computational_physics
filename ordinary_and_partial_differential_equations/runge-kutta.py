import matplotlib.pyplot as plot
from euler_method import euler_met2
from math import exp,sin

def runge_kutta_4_order(x0,y,xe,h,f):
    len_y=len(y)
    k=[]
    sol=[]
    y_sol=[]
    w={"x":x0,"e":exp,"sin":sin}
    coeff=[1/2,1/2,1,1]
    for i in range(len_y):
        k.append([])
        sol.append([y[i]])
        w["y"+str(i)]=y[len_y-i-1]
        y_sol.append(0)
    n=0
    while(x0<xe):
        for i in range(4):
            for j in range(len_y):
                t=h*eval(f[j],w)
                k[j].append(t)
            if(i!=3):
                w["x"]=x0+(coeff[i]*h)
                for j in range(len_y):
                    w["y"+str(j)]=sol[len_y-j-1][-1]+(coeff[i]*k[j][i])
            if(i==0 or i==3):
                co=1/6
            else:
                co=1/3
            for j in range(len_y):
                y_sol[j]+=co*k[j][i]
        for j in range(len_y):
            sol[j].append(sol[j][-1]+y_sol[j])
        x0+=h
        n+=1
        y_sol=[0 for i in range(len_y)]
        #print(k)
        k=[[] for i in range(len_y)]
    return(sol)
x0=0
xe=20
y=[0,1] #(n-1) order derivative term first
y2=[1,0]
h=0.1
o=int(input("enter order of matrix"))
const_diff=[]
print("put brackets in start and end of every coefficient")
#f="sin(x)-(3*y0)-(y0*y1)"
f_1=[]
f=""
for i in range(o+1):
    a=input("enter coefficient of "+str(i)+" order derivative:")
    const_diff.append(a)
    if(i==0):
        f+="-"+a
    else:    
        f+="-("+a+"*y"+str(i-1)+")"
        if(i>1):
            f_1=["y"+str(i-1)]+f_1
f_1=[f]+f_1
#print(f_1)
#print(f)
ans=runge_kutta_4_order(x0,y,xe,h,f_1)
ans2=euler_met2(x0,y2,xe,h,f)
#print(ans)
plot.plot(ans[-1])
plot.plot(ans2[0])
plot.legend(["runge-kutta","euler"])
plot.show()