class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def change(head):
            if head is None:
                return
            if head.next is None:
                return
            #交换两个节点的val
            temp=head.val
            before=head
            head=head.next
            before.val=head.val
            head.val=temp
            change(head.next)   #递归这样处理
        ret=head   #保存头结点
        change(head)
        return ret