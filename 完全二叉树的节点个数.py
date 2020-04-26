class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        #暴力法，遍历了所有的节点，然后得出长度,居然通过了60%击败
        self.res=0
        def fun(root):
            if not root:
                return
            self.res+=1
            fun(root.left)
            fun(root.right)

        fun(root)
        return self.res

