from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for index,num in enumerate(nums):#enumerate()返回下标和值
            map[num]=index
        for index,num in enumerate(nums):
            j=map.get(target-num)        #get方法返回对应键值的内容
            if j is not None and j!=index:
                return [index,j]
        return []
    def mytwoSum(self,nums,target):
        map={}
        for index,num in enumerate(nums):
            if map.get(target-num) is not None:
                return [map.get(target-num),index]
            map[num]=index
        return []
a=Solution()
nums=[2, 7, 11, 15]
target=9
print(a.mytwoSum(nums,target))

