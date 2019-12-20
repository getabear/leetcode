# 这是一个测试
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def creat(nums):   #构造一个链表的函数
    ret=ListNode(-1)
    res=ret
    for i in nums:
        ret.next=ListNode(i)
        ret=ret.next
    return res.next