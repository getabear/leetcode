import heapq

class Solution1:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# 实现一个小顶堆
class heap:
    def __init__(self,k,nums):
        self.size=k+1
        self.array=[0]+nums[:]
        return

    # 函数功能，完成较大值的下沉
    def build(self,nums,parent):
        i=2*parent
        while i<self.size:
            if i+1<self.size and nums[i+1]<nums[i]:  #找出两个子节点较小的节点
                i+=1
            if nums[parent]<nums[i]:
                break
            nums[parent],nums[i]=nums[i],nums[parent]
            parent=i
            i=parent*2
        return

    #函数功能：用于维护长度为k的堆，用于寻找第k大的数
    def add_val(self,val):
        if val>self.array[1]:
            self.array[1]=val
        else:
            return self.array[1] #返回堆顶的值
        self.build(self.array,1)
        return self.array[1]  #返回堆顶的值

    # 函数功能：构造小顶堆
    def build_min(self):
        for i in range(self.size//2,0,-1):
            self.build(self.array,i)

class Solution:
    def findKthLargest(self, nums, k):
        queue=heap(k,nums[:k])
        queue.build_min()
        for i in range(k,len(nums)):
            queue.add_val(nums[i])
        return queue.array[1]

nums=[3,2,3,1,2,4,5,5,6]
k = 4
a=Solution1()
b=Solution()
print(a.findKthLargest(nums,k))
print(b.findKthLargest(nums,k))