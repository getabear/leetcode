from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        min_num=1
        for i in nums: #n
            if i<min_num and i>0:
                min_num=i
        while min_num in nums:   #其实这种解法我感觉复杂度并不止是n,但是提交居然通过了
            min_num+=1
        return min_num

    def firstMissingPositive2(self, nums: List[int]) -> int:
        #这是咋们的正牌解法   1,桶排序
        def __swap(nums,index1,index2):
            nums[index1],nums[index2]=nums[index2],nums[index1]
        size=len(nums)
        if size==0:
            return 1
        #如果nums中有数字大于size,则必然不可能是那个大的数字
        #size个数,最大的数应该为size,如果有数大于size,则必然会有些正数空缺
        for i in range(size):
            while 0<nums[i]<size and nums[i]!=nums[nums[i]-1]:
            #将他们的位置交换
                __swap(nums,i,nums[i]-1)
        for i in range(size):
            if i+1!=nums[i]:
                return i+1
        return size+1

    def firstMissingPositive3(self, nums: List[int]) -> int:
        #我的另外一种理解
        if 1 not in nums:
            return 1
        size = len(nums)
        if size==1:
            return 2
        for i in range(size):
            if nums[i]>size or nums[i]<=0:   #将超过size的数和负数替换为1
                nums[i]=1
        map={}
        for i in range(1,size+1):   #建立1到n 的map字典
            map[i]=0
        for i in range(size):
            if nums[i] in map.keys():
                map[nums[i]]+=1
        for i in map.keys():    #检查字典中值为0的项说明没出现
            if map[i]==0:
                return i
        return size+1
    def firstMissingPositive4(self, nums: List[int]) -> int:
        #leetcode官方题解
        if 1 not in nums:
            return 1
        size = len(nums)
        if size==1:
            return 2
        for i in range(size):
            if nums[i]>size or nums[i]<=0:   #将超过size的数和负数替换为1
                nums[i]=1
        for i in range(size):
            i=abs(nums[i])   #保证取得正数
            if i==size:
                nums[0]=-abs(nums[0])
            else:
                nums[i]=-abs(nums[i])    #将数字作为索引,把对应位置的数变为负数
        for i in range(1,size):
            if nums[i]>0:
                return i
        if nums[0]>0:
            return size
        return size+1

        return size+1


a=Solution()
nums=[0,1,2]
print(a.firstMissingPositive4(nums))