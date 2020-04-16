from random import random
import matplotlib.pyplot as plot
n=500
arr=[]
for i in range(n):
    arr.append(random())
plot.plot(arr)
plot.show()