class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        rootA=headA
        rootB=headB
        m,n=0,0
        while rootA:
            m+=1
            rootA=rootA.next
        while rootB:
            n+=1
            rootB=rootB.next
        if m < n:
            headA,headB=headB,headA
            m,n=n,m
        while m-n>0:
            headA=headA.next
            n+=1
        while headA and headB:
            if headA==headB:
                return headA.val
            headA=headA.next
            headB=headB.next
        return None


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        # 我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，
        # 然后同时分别逐结点遍历，当 node1 到达链表 headA 的末尾时，
        # 重新定位到链表 headB 的头结点；当 node2 到达链表 headB 的末尾时，
        # 重新定位到链表 headA 的头结点。
        # 原理两个链表走的路程相同
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
