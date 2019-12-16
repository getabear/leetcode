# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #一次遍历实现
        tp=None
        ret=head
        while(head!=None):
            if tp and head.val==tp.val:
                tp.next=head.next
                head = head.next
                continue
            tp=head
            head=head.next

        return ret


