class Solution:
    def searchMatrix(self, matrix, target):
        high=len(matrix)
        if not high:
            return False
        width=len(matrix[0])
        if not width:
            return False
        minVal=matrix[0][0]
        maxVal=matrix[-1][-1]
        if target<minVal or target>maxVal:
            return False
        def find(nums,target):  #二分搜索
            right=len(nums)-1
            left=0
            while left<=right:
                mid=left+(right-left)//2   #虽然python不用考虑溢出，但是还是注意下
                if nums[mid]==target:
                    return True
                if nums[mid]>target:
                    right=mid-1
                if nums[mid]<target:
                    left=mid+1
            return False
        for nums in matrix:
            if nums[0]>target:
                return False
            if nums[-1]>=target:
                if find(nums,target):
                    return True
        return False

matrix=[[-5]]
a=Solution()
print(a.searchMatrix(matrix,-5))
