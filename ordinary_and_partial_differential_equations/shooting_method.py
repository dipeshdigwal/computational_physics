from runge_kutta import *

y_1=[10,2]
a=runge_kutta_4_order(x0,y_1,xe,h,f_1)
y_2=[5,2]
b=runge_kutta_4_order(x0,y_2,xe,h,f_1)
ye=0
err=10e-5
plot.plot(a[-1])
plot.plot(b[-1])
if(fabs(a[-1][-1]-ye)<err):
    print("a:"+str(a[-1][-1]))
    plot.plot(a[-1])
    plot.show()
elif(fabs(b[-1][-1]-ye)<err):
    print("b:"+str(b[-1][-1]))
    plot.plot(b[-1])
    plot.show()
else:
    alpha=y_1[0]+(((y_2[0]-y_1[0])/(b[-1][-1]-a[-1][-1]))*(ye-a[-1][-1]))
    while(fabs(b[-1][-1]-ye)>err):
        y_1=y_2
        a=b
        y_2=[alpha,y_1[1]]
        b=runge_kutta_4_order(x0,y_2,xe,h,f_1)
        print("els:"+str(b[-1][-1]))
        plot.plot(b[-1])
        x=(b[-1][-1]-a[-1][-1])
        if(x==0):
            break
        alpha=y_1[0]+(((y_2[0]-y_1[0])/x)*(ye-a[-1][-1]))
        
    plot.show()