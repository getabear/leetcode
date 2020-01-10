from git import lian

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #由于链表的分割不好弄,所以我们先进行数组的分割,然后赋值给链表
        nums=[]
        root=head  #记录头结点
        while head:
            nums.append(head.val)
            head=head.next
        def merge(nums1,nums2):
            len1=len(nums1)
            len2=len(nums2)
            index1=0
            index2=0
            nums=[]
            while index1<len1 and index2<len2:
                if nums1[index1]<nums2[index2]:
                    nums.append(nums1[index1])
                    index1+=1
                else:
                    nums.append(nums2[index2])
                    index2+=1
            while index1<len1:
                nums.append(nums1[index1])
                index1+=1
            while index2<len2:
                nums.append(nums2[index2])
                index2+=1
            return nums
        def divide(nums):
            size=len(nums)
            if size==1:
                return nums
            mid=size//2
            nums1=divide(nums[:mid])
            nums2=divide(nums[mid:])
            return merge(nums1,nums2)
        if root:
            nums=divide(nums)
            head=root
            for i in nums:
                head.val=i
                head=head.next
            return root
        return []   #这行很关键,该死的leetcode细节

a=Solution()
b=lian()
nums=[]
head=b.creat(nums)
print(a.sortList(head))
