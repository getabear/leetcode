from git import lian

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ret=ListNode(float('-inf'))   #负无穷,保证最小
        while head:
            tp=head.next   #记录下一个为排序的节点
            start=ret.next
            pre=ret
            if start:    #如果下一个ret的下一个节点有值
                while start:
                    if start.val>head.val:  #如果值大于了当前节点,把当前节点插入ret所在的链表中
                        head.next=start
                        pre.next=head
                        break
                    pre=start     #更新前节点
                    if start.next:   #如果本节点不是末尾节点
                        start=start.next
                    else:
                        start.next=head
                        head.next=None
                        break
            else:
                pre.next=head
                head.next=None
            head=tp

        return ret.next

b=lian()
head=b.creat([-1,5,3,4,0])
a=Solution()
head=a.insertionSortList(head)
print("end")
