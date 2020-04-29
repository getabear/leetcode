class MountainArray:
    def __init__(self,arr):
        self.arr=arr
        self.count=0
    def get(self, index: int) -> int:
        self.count+=1
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        #二分查找的函数
        def fun(mountain,l,r,target,direct):
            while(l<r):
                mid=(l+r)//2
                tmp=mountain.get(mid)
                if tmp==target:
                    return mid
                if tmp<target:
                    if direct==1:  #数组是升序
                        l=mid+1
                    else:
                        r=mid-1
                else:
                    if direct==1:  #数组是升序
                        r=mid-1
                    else:
                        l=mid+1
            if mountain.get(l)==target:
                return l
            return -1

        length=mountain_arr.length()
        self.middle=0
        l,r=0,length-1
        while l<r:
            mid = (l+r) // 2
            if mid==0:
                break
            #左边有序
            if mountain_arr.get(mid-1) < mountain_arr.get(mid):
                self.middle=mid
                l=mid+1
            #右边有序
            else:
                r=mid-1
        tmp=fun(mountain_arr, 0, self.middle, target, 1)
        if tmp!=-1:
            return tmp
        tmp = fun(mountain_arr, self.middle+1, length-1, target, -1)
        if tmp!=-1:
            return tmp
        return -1
arr=[3,5,3,2,0]
mountain_arr=MountainArray(arr)
a=Solution()
print(a.findInMountainArray(5,mountain_arr))
print(mountain_arr.count)