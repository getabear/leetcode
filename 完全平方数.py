def fun(n):
    min=1000
    if n==0:
        return 0
    for i in range(1,100):
        if(n-i*i>=0):
            times=1+fun(n-i*i)
        else:
            break
        if times<min:
            min=times
    return min

for n in range(20):
    print(fun(n))