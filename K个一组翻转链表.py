class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def fun(head,k):
            temp=[]  #用来记录k个值
            rec=head   #记录初始节点的位置
            for i in range(k):    #0--(k-1)  i 的值
                if head is None:
                    return
                temp.append(head.val)
                head=head.next
            for i in range(k):
                rec.val=temp.pop()
                rec=rec.next
            return fun(head,k)
        ret=head
        fun(head,k)
        return ret