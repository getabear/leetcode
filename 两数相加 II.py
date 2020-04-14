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

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #常规思路:将链表先转换为数字,然后相加,最后在转换为链表
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

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #升级思路:利用栈进行(因为栈可以将链表最后一个弄到前面,符合我们相加的机制)
        stack1=[]
        stack2=[]

        def fun(l,stack):
            while(l):
                stack.append(l.val)
                l=l.next

        fun(l1,stack1)
        fun(l2,stack2)
        last=None
        carry=0
        while stack1 or stack2 or carry:
            if stack1 and stack2:
                val=stack2.pop(-1)+stack1.pop(-1)+carry
            elif stack1:
                val =stack1.pop(-1)+carry
            elif stack2:
                val=stack2.pop(-1)+carry
            else:
                val=carry
            now=ListNode(val%10)
            now.next=last
            last=now
            carry=val//10

        return now

l1=creat("7243")
l2=creat("564")
a=Solution()
print(a.addTwoNumbers(l1,l2))