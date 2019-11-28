class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root1,root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val==root2.val:
                return helper(root1.left,root2.right) and helper(root1.right,root2.left)
        return helper(root,root)



