from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret=[]
        def fun(root: TreeNode, sum: int,nums):
            #到达叶子节点
            if root.left==None and root.right==None:
                if sum-root.val==0:
                    nums.append(root.val)
                    ret.append(nums[:])
                    return
                return
            if root.left:
                fun(root.left,sum-root.val,nums+[root.val])
            if root.right:
                fun(root.right,sum-root.val,nums+[root.val])
            return
        if root:
            fun(root,sum,[])
        return ret

