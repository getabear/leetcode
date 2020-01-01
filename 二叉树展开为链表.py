class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre=None
        def fun(root):
            if not root:
                return
            fun(root.right)
            fun(root.left)
            root.right=self.pre
            root.left=None
            self.pre=root
        fun(root)

