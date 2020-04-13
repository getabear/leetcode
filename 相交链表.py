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


class Solution1(object):
    # 这个算法也浪漫了吧，错的人迟早会走散，而对的人迟早会相逢！
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

