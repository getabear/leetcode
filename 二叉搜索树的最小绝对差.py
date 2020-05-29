class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums=[]
        def fun(root):
            if not root:
                return
            fun(root.left)
            nums.append(root.val)
            fun(root.right)
        fun(root)
        res=1<<31
        for i in range(1,len(nums)):
            j=i-1
            res=min(nums[i]-nums[j],res)
        return res