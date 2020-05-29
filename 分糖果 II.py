from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ret=[0]*num_people
        candie=1
        index=0
        while candies>0:
            if candie<candies:
                ret[index]+=candie
            else:
                ret[index]+=candies
            candies-=candie
            index=(index+1)%num_people
            candie+=1
        return ret


a=Solution()
candies = 10
num_people = 3
print(a.distributeCandies(candies,num_people))