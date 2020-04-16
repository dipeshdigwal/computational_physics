def check():
    for i in range(4):
        print(str(arr[i][0])+" "+str(arr[i][1]))
    print()
def square(count):
    if(count==4):
        check()
    else:
        for i in range(n):
            if(i not in sol):
                sol[count]=i
                square(count+1)
n=int(input())
sol=[-1 for i in range(4)]
arr=[]
for i in range(n):
    arr.append(input().split())
square(0)