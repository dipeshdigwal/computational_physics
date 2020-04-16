from reduced_row_echelon import mat_mult
def power_met():
    c=x0
    for i in range(iterations):
        c=mat_mult(a,c)
        if(i==iterations-1):
            print(c[0][0]/c_sto)
        d=0
        for j in range(len(c)):
            d+=c[j][0]**2
        d=d**(1/2)
        print(d)
        for j in range(len(c)):
            c[j][0]/=d
        if(i==iterations-2):
            c_sto=c[0][0]
        print(c)
a=[[1,2,3],[4,5,6],[7,8,9]]
x0=[[1]]*len(a[0])
#a=[[3,1],[2,4]]
#x0=[[(2**(1/2))/2]]*2
iterations=10
power_met()