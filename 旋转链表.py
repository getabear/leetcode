class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        nums=[]
        root=head
        while head:
            nums.append(head.val)
            head=head.next
        length=len(nums)
        if k>length:
            k=k%length
        start=-k
        head=root
        for i in range(length):
            head.val=nums[start]
            start+=1
            head=head.next
        return root