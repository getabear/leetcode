class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def creat(nums):
    ret=ListNode(-1)
    res=ret
    for i in nums:
        ret.next=ListNode(i)
        ret=ret.next
    return res.next

def display(head):
    while head:
        print(head.val)
        head=head.next

#太多细节了,差点哭晕在厕所
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        self.ret=None
        self.next=None
        def fun(head: ListNode,n):
            if n==0:
                self.ret=head
                self.next=head.next
                head.next=None
                return head
            last=fun(head.next,n-1)
            last.next=head
            head.next=None
            return head
        res=head
        count=0
        if m!=1:
            while count+1<m-1:
                count+=1
                head=head.next
            start=head
            end = fun(head.next, n - m)
            start.next = self.ret
        else:
            end=fun(head,n-m)
            end.next=self.next
            return self.ret
        end.next=self.next
        return res

a=Solution()
nums=[1,2,3,4,5]
head=creat(nums)
head=a.reverseBetween(head,1,5)

