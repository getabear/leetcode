# 这是一个测试
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class lian:
    def creat(self,nums):   #构造一个链表的函数
        ret=ListNode(-1)
        res=ret
        for i in nums:
            ret.next=ListNode(i)
            ret=ret.next
        return res.next

    def display(self,head):   #展示一个链表的值
        while head:
            print(head.val)
            head=head.next




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class er:
    def creat_er(self,nums):  #宽度优先遍历利用数组构造二叉树,nums是构造二叉树的数组
        if not nums:
            return
        root=TreeNode(nums[0])
        queue=[root]
        length=len(nums)
        index=1
        while(queue):
            newroot=queue.pop(0)
            if index<length and newroot:
                if nums[index]!=None:
                    newroot.left=TreeNode(nums[index])
                else:
                    newroot.left=None
                index+=1
                queue.append(newroot.left)
            if index<length and newroot:
                if nums[index]!=None:
                    newroot.right=TreeNode(nums[index])
                else:
                    newroot.right=None
                index+=1
                queue.append(newroot.right)

        return root









