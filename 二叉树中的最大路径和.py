class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ret=float("-inf")
        def fun(root: TreeNode):  #递归,返回左右树到上一个节点的最大值
            if not root:
                return 0
            left=fun(root.left)
            right=fun(root.right)
            self.ret=max(left+right+root.val,self.ret)   #记录最大值
            return max(0,left+root.val,right+root.val)  #返回左右树到上一个节点的最大值
        fun(root)
        return self.ret

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ret=float("-inf")
        def fun(root):
            if not root:
                return 0
            left=fun(root.left)
            right=fun(root.right)
            self.ret=max(self.ret,max(left,right,left+right)+root.val,root.val)
            return max(max(left,right)+root.val,root.val)
        fun(root)
        return self.ret