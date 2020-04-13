class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        listB=set()
        i=headA
        # 时间复杂度为O(n),空间复杂度为O(n)
        while headB:
            listB.add(headB)
            headB=headB.next
        while(i):
            if i in listB:
                return i
            i=i.next
        return None
