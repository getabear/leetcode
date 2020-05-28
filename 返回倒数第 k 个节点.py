class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def kthToLast(self, head: ListNode, k: int) -> int:
        #迭代
        if not head:
            return
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        return nums[-k]


class Solution2:
    def kthToLast(self, head: ListNode, k: int) -> int:
        #递归
        self.ret=None
        def fun(head):
            if not head:
                return 1
            ret=fun(head.next)
            if ret==k:
                self.ret=head.val
            return ret+1
        fun(head)
        return self.ret

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        slow=head
        fast=head
        while k>0:
            fast=fast.next
            k-=1
        while fast:
            slow=slow.next
            fast=fast.next
        return slow.val
