from typing import List

class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #暴力法
        i,j=0,0
        length=len(T)
        ret=[]
        while i<length:
            j=i+1
            while j<=length:
                if j==length:
                    ret.append(0)
                    break
                if T[j]>T[i]:
                    ret.append(j-i)
                    break
                j+=1
            i+=1
        return ret

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #利用栈进行数据的记录
        length=len(T)-1
        ret=[0]*(length+1)
        stack=[]
        while length>=0:
            if not stack:
                ret[length]=0
                stack.append(length)
            else:
                while stack:
                    if T[length]>=T[stack[-1]]:
                        stack.pop()
                    else:
                        ret[length]=stack[-1]-length
                        stack.append(length)
                        break
                if not stack:
                    stack.append(length)
            length-=1
        return ret
T=[73, 74, 75, 71, 69, 72, 76, 73]
a=Solution()
print(a.dailyTemperatures(T))