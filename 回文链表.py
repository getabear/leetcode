class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        length=len(res)
        left,right=0,length-1
        while left<right:
            if res[left]!=res[right]:
                return False
            left+=1
            right-=1
        return True