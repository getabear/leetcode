class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret=-1
        children=[root.left,root.right]
        if not any(children):
            return 1
        else:
            for child in children:
                ret=max(self.maxDepth(child),ret)
            return ret+1