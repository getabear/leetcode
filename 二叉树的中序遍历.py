from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #递归方案
        self.ret=[]
        def fun(root: TreeNode):
            if not root:
                return
            fun(root.left)
            self.ret.append(root.val)
            fun(root.right)

        fun(root)
        return self.ret

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #迭代方案,先一直找左节点,当到尽头了开始回溯
        ret=[]
        stack=[]
        head=root
        while head or stack:
            while head:
                stack.append(head)
                head=head.left
            head=stack.pop()
            ret.append(head.val)
            head=head.right
        return ret