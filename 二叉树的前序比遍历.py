from typing import List
from git import er

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:   #递归版本
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret=[]
        def fun(root: TreeNode):
            if not root:
                return
            if root.val:
                self.ret.append(root.val)
            fun(root.left)
            fun(root.right)
        fun(root)
        return self.ret


class Solution:
    #迭代版本
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        ret=[]
        head=root
        while head or stack:
            while head:
                ret.append(head.val)
                stack.append(head.right)
                head=head.left
            head=stack.pop()
        return ret
nums=[1,None,2,3]
a=Solution()
b=er()
head=b.creat_er(nums)
print(a.preorderTraversal(head))