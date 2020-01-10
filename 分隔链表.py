class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before=ListNode(0)
        after=ListNode(0)
        tp=head
        b=before
        a=after
        while head:
            if head.val<x:
                b.next=head
                b=head
            else:
                a.next=head
                a=head
            head=head.next
        a.next=None
        b.next=after.next
        return before.next if tp else []  #不知道leetcode为什么非要这样搞...