class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp=ListNode(None)
        ret=temp   #返回值
        bef=temp
        while(l1!=None and l2!=None):
            if l1.val<l2.val:
                temp.val=l1.val
                l1=l1.next
            else:
                temp.val=l2.val
                l2=l2.next
            temp.next=ListNode(0)
            bef=temp
            temp=temp.next
        while(l1!=None):
            temp.val = l1.val
            l1=l1.next
            temp.next = ListNode(0)
            bef=temp
            temp = temp.next
        while(l2!=None):
            temp.val = l2.val
            l2=l2.next
            temp.next = ListNode(0)
            bef=temp
            temp = temp.next
        if ret.val==None:
            return None
        bef.next=None
        return ret
