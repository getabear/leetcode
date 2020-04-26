from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(list1,list2):   #功能,和并两个排序链表
            ret=ListNode(None)
            res=ret    #返回值
            temp=ret
            while(list1!=None and list2!=None):
                if(list1.val<list2.val):
                    ret.val=list1.val
                    list1=list1.next
                else:
                    ret.val=list2.val
                    list2=list2.next
                ret.next = ListNode(0)
                temp=ret
                ret = ret.next
            while(list1!=None):
                ret.val = list1.val
                list1 = list1.next
                ret.next = ListNode(0)
                temp=ret
                ret = ret.next
            while (list2 != None):
                ret.val = list2.val
                list2=list2.next
                ret.next = ListNode(0)
                temp=ret
                ret = ret.next
            if temp==res and temp.val==None:
                return None
            temp.next=None
            return res

        def divide(lists):
            length=len(lists)
            if(length==0):
                return None
            if(length==1):
                return merge(lists[0],None)
            else:
                temp=merge(lists[0],lists[1])
                return merge(temp,divide(lists[2:]))
        return divide(lists)    #暂时是对的,只是超时了


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def merge(Node1,Node2):
            Node=ListNode(-1)
            res=Node
            while Node1 and Node2:
                if Node1.val<=Node2.val:
                    Node.next=ListNode(Node1.val)
                    Node1=Node1.next
                else:
                    Node.next = ListNode(Node2.val)
                    Node2 = Node2.next
                Node=Node.next
            while Node1:
                Node.next=ListNode(Node1.val)
                Node1=Node1.next
                Node = Node.next
            while Node2:
                Node.next=ListNode(Node2.val)
                Node2=Node2.next
                Node = Node.next
            return res.next

        def divide(lists):
            length=len(lists)
            if length==1:
                return lists[0]
            # if length==2:
            #     return merge(lists[0],lists[1])
            left=divide(lists[:length//2])
            right=divide(lists[length//2:])
            return merge(left,right)

        if len(lists) == 0:
            return []
        return divide(lists)

def creat(nums):   #构造一个链表的函数
    ret=ListNode(-1)
    res=ret
    for i in nums:
        ret.next=ListNode(i)
        ret=ret.next
    return res.next
node1=creat([1,4,5])
node2=creat([1,3,4])
lists=[node1,node2]
a=Solution()
print(a.mergeKLists(lists))




