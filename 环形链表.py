class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #方法使用hash检测元素是否被访问过
        hash_tab={}
        while head:
            if head not in hash_tab:
                hash_tab[head]=1
            else:
                return True
            head=head.next
        return False

class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        #这次使用双指针来实现,如果有环,快指针必然会追到慢指针,就像跑步快追跑步慢的人
        if head==None or head.next==None:
            return False
        sp=head
        fp=head.next
        while sp!=fp:
            if fp==None or fp.next==None:
                return False
            fp=fp.next.next
            sp=sp.next
        return True