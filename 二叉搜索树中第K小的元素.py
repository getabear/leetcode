class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.cnt=0
        self.ret=None
        def fun(root):
            if not root:
                return
            fun(root.left)
            self.cnt+=1
            if self.cnt==k:
                self.ret=root.val
                return  #找到结果直接返回
            fun(root.right)
            return
        fun(root)
        return self.ret

