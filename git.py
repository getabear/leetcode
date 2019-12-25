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

def display(head):   #展示一个链表的值
    while head:
        print(head.val)
        head=head.next





class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# nums=[3,9,20,None,None,15,7,8,9]
# node=creat_er(nums)
# print(node)

