triangle=[2,[3,4],[6,5,7],[4,1,8,3]] #triangle 三角形
length=len(triangle)

def min_(a,b):
    if(a>b):
        return b
    return a

def Solution(triangle,level,i):
    if(level==length):
        return 0
    left=Solution(triangle,level+1,i)
    right=Solution(triangle,level+1,i+1)
    if(level==0):
        return min_(left, right) + triangle[level]
    else:
        return min_(left, right) + triangle[level][i]

print(Solution(triangle,0,0))
