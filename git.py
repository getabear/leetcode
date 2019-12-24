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

def creat_er(nums):
    def fun(nums,node):
        if len(nums)==0 or node==None:
            return None
        if  len(nums)>0:
            if nums[0]!=None:
                node.left=TreeNode(nums[0])
        if len(nums)>1:
            if nums[1]!=None:
                node.right=TreeNode(nums[1])
        fun(nums[2:],node.left)
        fun(nums[4:],node.right)

    if len(nums)<1:
        return None
    node=TreeNode(nums[0])
    fun(nums[1:],node)
    return node

nums=[3,9,20,None,None,15,7,8,9]
node=creat_er(nums)
print(node)

