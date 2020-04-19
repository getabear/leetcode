class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        while(head and head.val==val):
            head=head.next
        ret=head
        slow=head
        fast=None
        if head:
            fast=head.next
        while(fast):
            if fast.val==val:
                slow.next=fast.next
                fast=fast.next
                continue
            slow=slow.next
            fast=fast.next
        return ret