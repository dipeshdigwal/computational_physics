import matplotlib.pyplot as plot
from math import exp,cos,sin
"""def euler_met(x0,y0,xe,h,f):
    i=x0
    j=0
    y=[y0]
    while(i<xe):
        c=y[j]+(h*eval(f,{"x":i,"y0":y[j],"y1":}))
        y.append(c)
        i+=h
        j+=1
    return(y)
"""
def euler_met2(x0,y_x,xe,h,f):
    i=x0
    j=0
    y=[]
    q=len(y_x)
    w={"x":i,"sin":sin,"e":exp}
    for k in range(len(y_x)):
        y.append([y_x[k]])
        w["y"+str(k)]=y_x[k]
    while(i<xe):
        for k in range(len(y_x)):
            if(k==0):
                c=y[q-1-k][j]+(h*eval(f,w))
                #print(str(y[q-1-k][j])+str((h*eval(f,w))))
                w["y"+str(q-1-k)]=c
            else:
                c=y[q-1-k][j]+(h*y[q-k][j])
                #print(str(y[q-1-k][j])+str(h*y[q-k][j]))
                w["y"+str(q-1-k)]=c
            y[q-1-k].append(c)
        i+=h
        j+=1
        w["x"]=i
    return(y)
"""x0=0
xe=20
y=[1,0]
h=0.1
o=int(input("enter order of matrix"))
const_diff=[]
print("put brackets in start and end of every coefficient")
#f="sin(x)-(3*y0)-(y0*y1)"
f=""
for i in range(o+1):
    a=input("enter coefficient of "+str(i)+" order derivative:")
    const_diff.append(a)
    if(i==0):
        f+="-"+a
    else:    
        f+="-("+a+"*y"+str(i-1)+")"
"""
#print(f)
"""plot.plot(euler_met(x0,y0,xe,h,f))
i=x0
c=[]
while(i<=xe):
    c.append(exp(i))
    i+=h
plot.plot(c)
plot.show()"""
#r=euler_met2(x0,y,xe,h,f)
#plot.plot(r[0])
#print(r)
"""i=x0
ex="(1/4)*((9*e(-x))+(7*e(5*x))-(18*x*e(5*x)))"
li=[]
while(i<=xe):
    f=eval(ex,{"x":i,"cos":cos,"sin":sin,"e":exp})
    i+=h
    li.append(f)
"""
#print(li)
#plot.plot(li)
#plot.plot(r[0])
#plot.show()