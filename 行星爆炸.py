from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        flag=0
        tp=[]
        for index,asteroid in enumerate(asteroids):
            if index+1<len(asteroids):
                if asteroid>0 and asteroids[index+1]<0:   #会发生相撞
                    flag=1
                    if asteroid>abs(asteroids[index+1]):
                       tp.append(index+1)
                    elif asteroid<abs(asteroids[index+1]):
                        tp.append(index)
                    else:
                        tp+=[index,index+1]
        tp=tp[::-1]
        for i in tp:
            asteroids.pop(i)
        while flag:
            flag=0
            tp=[]
            for index,asteroid in enumerate(asteroids):
                if index + 1 < len(asteroids):
                    if asteroid > 0 and asteroids[index + 1] < 0:  # 会发生相撞
                        flag = 1
                        if asteroid > abs(asteroids[index + 1]):
                            tp.append(index + 1)
                        elif asteroid < abs(asteroids[index + 1]):
                            tp.append(index)
                        else:
                            tp += [index, index + 1]
            tp = tp[::-1]
            for i in tp:
                asteroids.pop(i)
        return asteroids

a=Solution()
nums=[-2,-2,1]
print(a.asteroidCollision(nums))