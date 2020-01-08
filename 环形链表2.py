class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    # 提交后通过了,击败62%的用户,空间复杂度O(n),时间复杂度是O(n)
    def detectCycle(self, head: ListNode) -> ListNode:
        #思路:
        #1.如果下一个节点是None则代表链表无环
        #2.如果被访问的节点再次被访问,则代表有环,并且为环形链表的开头
        rec={}
        def fun(head: ListNode):
            count=0
            while(head):
                if head not in rec:
                    rec[head]=count  #记录访问过的节点的下标
                else:
                    return head
                head=head.next
                count+=1

            return None
        return fun(head)

class Solution:
    #题目的进阶为尝试不用额外的空间,我们尝试下
    #没想出来,只知道双指针可以判断是否有链表,但是不知道如何判断链表的开头
    #大佬题解:
    #解题链接   https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
    def detectCycle(self, head: ListNode) -> ListNode:
        f,s=head,head
        while True:
            if not (f and f.next):
                return None
            f,s=f.next.next,s.next
            if f==s:
                break
        f=head
        while f!=s:
            f,s=f.next,s.next
        return f

