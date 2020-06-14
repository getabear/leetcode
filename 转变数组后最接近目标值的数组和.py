from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left,right=0,max(arr)
        res,tmp=0,float("inf")
        while left<=right:
            mid=left+(right-left)//2
            cnt,total=0,0
            for i in arr:
                if i<mid:
                    total+=i
                else:
                    cnt+=1
            total+=cnt*mid
            dis=abs(total-target)
            if dis<=tmp:
                if dis==tmp and mid>res:
                    pass
                else:
                    res,tmp=mid,dis
            if total<target:
                left=mid+1
            elif total>=target:
                right=mid-1
        return res

a=Solution()
arr=[60864,25176,27249,21296,20204]
target=56803
print(a.findBestValue(arr,target))



