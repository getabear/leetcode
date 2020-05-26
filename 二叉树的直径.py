class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def fun(root):
            if not root:
                return [0,0]
            left=fun(root.left)
            right=fun(root.right)
            return [max(left[0],right[0])+1,max(left[0]+right[0]+1,left[1],right[1])]
        ret=fun(root)
        return max(ret)-1 if root else 0

