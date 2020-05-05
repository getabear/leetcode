class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:

        res=[]
        def fun(root):
            if not root:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)

        fun(root)
        slow,fast=0,1
        if len(res)<2:
            return True
        length=len(res)
        while fast<length:
            if res[slow]<=res[fast]:
                slow+=1
                fast+=1
            else:
                return False
        return True

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def fun(root,minval,maxval):
            if not root:
                return True
            if root.val>minval and root.val<maxval:
                pass
            else:
                return False
            if fun(root.left,minval,root.val)==False:
                return False
            if fun(root.right,root.val,maxval)==False:
                return False
            return True
        return fun(root,-(1<<31),1<<31-1)