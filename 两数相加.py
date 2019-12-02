class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:   #过于暴力,算法效率低,不美

        def tonum(l):
            num=0
            times=1
            while(l.next!=None):
                num+=l.val*times
                times*=10
                l=l.next
            num+=l.val*times
            return num

        def tolist(num):
            l = ListNode(num % 10)
            ret=l   #记录返回值
            num=num//10
            while(num!=0):
                l1=ListNode(num%10)
                num//=10
                l.next=l1
                l=l1
            return ret
        #这两句只是本地测试用的
        l1=tolist(l1)
        l2=tolist(l2)


        num1=tonum(l1)
        num2=tonum(l2)
        num=num1+num2
        return tolist(num)
    def addtwolist(self,l1,l2):   #用一种效率高的,更美的算法
        carry=0    #进位标志
        l=ListNode(0)
        ret=l     #ret 返回值
        if(l1!=None or l2!=None):    #这个if是为了便于处理返回值...,技术达不到只有靠代码量
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            num = l1.val + l2.val + carry
            carry = num // 10
            l.val=num%10
            l1 = l1.next
            l2 = l2.next
        while(l1!=None or l2!=None):
            if l1==None:
                l1=ListNode(0)
            if l2==None:
                l2=ListNode(0)
            num=l1.val+l2.val+carry
            carry=num//10
            l.next=ListNode(num%10)
            l=l.next
            l1=l1.next
            l2=l2.next
        if(carry==1):
            l.next=ListNode(carry)
        return ret



l1=342
l2=465
a=Solution()
print(a.addTwoNumbers(l1,l2))