from typing import List

class Solution:
    #提交后超时了,我们优化下,
    def canJump(self, nums: List[int]) -> bool:
        size=len(nums)-1
        def fun(nums,cur):
            if cur==size:
                return True
            else:
                val=nums[cur]   #val为可以跳跃的步数,可以比这个步数小
                if val==0:
                    return False
                if val+cur>size:
                    return True
                res=False
                for i in range(1,val+1):  #尝试所有跳法
                    res=fun(nums,cur+i)
                    if res:
                        return res
                return res

        return fun(nums,0)

class Solution1:
    #提交后超时了,我们优化下,我们用一个字典记录下结果,虽然优化了很多时间,但是还是通不过leetcode最后两个测试用例
    #这是自顶向下的动态规划,比自底向上的动态规划更加耗时一点,不知道自底向上能否通过
    def canJump(self, nums: List[int]) -> bool:
        size=len(nums)-1
        dit={}   #字典记录下标cur是否可以到达末尾
        def fun(nums,cur):
            if cur==size:
                return True
            else:
                val=nums[cur]   #val为可以跳跃的步数,可以比这个步数小
                if val==0:
                    return False
                if val+cur>size:
                    return True
                res=False
                if cur in dit:  #如果在字典中就直接返回
                    return dit[cur]
                for i in range(1,val+1):  #尝试所有跳法
                    res=fun(nums,cur+i)
                    dit[cur+i]=res   #记录在字典中
                    if res:
                        return res
                return res

        return fun(nums,0)

class Solution2:
    #这次咱们用贪心算法
    def canJump(self, nums: List[int]) -> bool:
        size=len(nums)-1
        def fun(nums,cur):
            if cur==size:
                return True
            val=nums[cur]  #可以跳跃的步数
            if val==0:
                return False
            temp=0
            index=cur
            for i in range(1,val+1):
                if cur+i>size:
                    return True
                if cur+i+nums[cur+i]>temp:
                    temp=cur+nums[cur+i]+i
                    index=cur+i
            return fun(nums,index)

        return fun(nums,0)


a=Solution1()
nums=[1,2,3,4]
import time
print(a.canJump(nums))
print(time.process_time())

