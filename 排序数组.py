from typing import List

class Solution1:
    #归并排序
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            ret=[]
            leftsize=len(left)
            rightsize=len(right)
            index1=0
            index2=0
            while(index1<leftsize and index2<rightsize):
                if(left[index1]<right[index2]):
                    ret.append(left[index1])
                    index1+=1
                else:
                    ret.append(right[index2])
                    index2+=1
            ret+=left[index1:]
            ret+=right[index2:]
            return ret
        def devide(nums):
            size=len(nums)
            if size==1:
                return nums
            left=devide(nums[:size//2])
            right=devide(nums[size//2:])
            return merge(left,right)

        return devide(nums)

class Solution:
    #试试堆排序
    def sortArray(self, nums: List[int]) -> List[int]:
        #build  用于构造大顶堆
        def build(arr,parent,length):
            #参数 数组 父节点 数组长度
            i=2*parent   #子节点下标
            while(i<length):
                if(i+1<length and arr[i]<arr[i+1]):
                    i+=1  #选择两个子节点中较大的一个和父节点比较
                if(arr[parent]>arr[i]): #如果父节点小于子节点,则交换他们的值
                    break
                arr[parent],arr[i]=arr[i],arr[parent]
                parent=i
                i=2*parent

        def paixu(arr):
            length=len(arr)
            for i in range(length//2,0,-1):  #构造大顶堆
                build(arr,i,length)

            for i in range(length-1,0,-1):
                arr[i],arr[1]=arr[1],arr[i]
                build(arr,1,i)
            return arr[1:]

        return paixu([-1]+nums)




a=Solution()
nums=[5,1,1,2,0,0]
print(a.sortArray(nums))