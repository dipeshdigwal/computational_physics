def factors(k):
    fac = []
    for i in range(2, int(k/2)+1):
        if(k % i == 0):
            fac.append(i)
    return(fac)


def max_finder(count, nums, max_prod, max_nums):
    if(count == 4):
        if(sum(nums) == n):
            c = 1
            for i in range(4):
                c *= nums[i]
            if(c > max_prod):
                max_prod = c
                max_nums = list(nums)
    else:
        l = factors(n)
        for i in l:
            nums[count] = i
            max_finder(count+1)


nums = [0 for i in range(4)]
max_prod = 0
max_nums = [0 for i in range(4)]
t = int(input())
for q in range(t):
    n = int(input())
    max_finder(0)
    print(max_nums)
