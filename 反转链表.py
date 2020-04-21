class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def creat(nums):   #构造一个链表的函数
    ret=ListNode(-1)
    res=ret
    for i in nums:
        ret.next=ListNode(i)
        ret=ret.next
    return res.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        self.res=None
        def fun(head):
            if head.next==None:
                self.res=head
                return head
            ret=fun(head.next)
            # head.next=None
            ret.next=head
            return head

        if not head:
            return head
        fun(head)
        head.next=None
        return self.res

nums=[1,2,3,4,5]
head=creat(nums)
a=Solution()
print(a.reverseList(head))


