class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        # 没想到居然超时了
        nums=[2,3,5]
        mem=dict()
        def fun(num):
            if num in mem:
                return mem[num]
            if num==1:
                mem[num]=True
                return True
            for i in nums:
                if num%i==0:
                    if fun(num//i):
                        mem[num]=True
                        return True
            mem[num]=False
            return False
        count=0
        i=1
        while count<n:
            if fun(i):
                count+=1
            i+=1
        return i-1

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        i1,i2,i3=0,0,0
        while len(nums)<n:
            tmp=min(nums[i1]*2,nums[i2]*3,nums[i3]*5)
            nums.append(tmp)
            if tmp==nums[i1]*2:
                i1+=1
            if tmp==nums[i2]*3:
                i2+=1
            if tmp==nums[i3]*5:
                i3+=1
        return nums[-1]
a=Solution1()
print(a.nthUglyNumber(378))


