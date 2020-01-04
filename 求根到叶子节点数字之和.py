class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ret=0
        def fun(root: TreeNode,sum):
            if not root.left and not root.right:  #到达叶子节点
                self.ret+=sum+root.val
                return
            sum=(root.val+sum)*10
            if root.left:   #如果存在左节点,继续深入
                fun(root.left,sum)
            if root.right:  #如果存在右节点,继续深入
                fun(root.right,sum)
        if root:
            fun(root,0)
        return self.ret
