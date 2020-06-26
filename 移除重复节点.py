class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        mem=set()
        ret=head
        pre=head
        if head:
            mem.add(head.val)
            head=head.next
        else:
            return head
        while head:
            if head.val not in mem:
                mem.add(head.val)
                pre=pre.next
            else:
                pre.next=head.next
            head=head.next
        return ret

def creat(nums):   #构造一个链表的函数
    ret=ListNode(-1)
    res=ret
    for i in nums:
        ret.next=ListNode(i)
        ret=ret.next
    return res.next
head=creat([1, 1, 1, 1, 2])
a=Solution()
ret=a.removeDuplicateNodes(head)
print("hello")
