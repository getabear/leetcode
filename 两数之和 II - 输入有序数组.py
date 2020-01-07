from typing import List

class Solution:
    #击败75%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1=0
        size=len(numbers)
        index2=size-1
        if size<2:
            return
        while index1<index2:
            tp=numbers[index2]+numbers[index1]
            if tp==target:
                return [index1+1,index2+1]
            elif tp>target:
                index2-=1
            else:
                index1+=1
        return

a=Solution()
numbers = [2, 7, 11, 15]
target = 9
print(a.twoSum(numbers,target))


