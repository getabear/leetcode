class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ret=head
        temp=head
        tempn=head
        while(n>0):#使temp和tempn之间有n个节点
            tempn=tempn.next
            n-=1
        if tempn==None:   #说明移动到了末尾后一位
            temp=temp.next
            return temp
        while(tempn.next!=None):   #移动指针到数据末尾
            temp=temp.next
            tempn=tempn.next

        temp.next=temp.next.next
        return ret