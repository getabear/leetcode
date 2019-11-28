class NumArray:

    def __init__(self, nums):
        self.nums=nums
    def sumRange(self, i: int, j: int) -> int:
        sum=0
        for temp in range(i,j+1):
            sum+=self.nums[temp]
        return sum
a=[-2, 0, 3, -5, 2, -1]
b=NumArray(nums=a)
print(b.sumRange(0,2))
print(b.sumRange(2,5))
print(b.sumRange(0,5))