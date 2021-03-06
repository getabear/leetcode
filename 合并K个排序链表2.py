from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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
            mid=length//2
            if length==0:
                return None
            if length==1:
                return lists[0]
            else:
                left=divide(lists[0:mid])
                right=divide(lists[mid:])
                return merge(left,right)
        return divide(lists)