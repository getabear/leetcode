class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def creat(nums):   #构造一个链表的函数
    ret=ListNode(-1)
    res=ret
    for i in nums:
        ret.next=ListNode(int(i))
        ret=ret.next
    return res.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def fun(l):
            if not l:
                return (1,0)  #倍数和加的数字
            x,ret=fun(l.next)
            return (x*10,l.val*x+ret)

        x,ret=fun(l1)
        x2,ret2=fun(l2)
        ret=ret+ret2
        ret=creat(str(ret))
        return ret

l1=creat("7243")
l2=creat("564")
a=Solution()
print(a.addTwoNumbers(l1,l2))