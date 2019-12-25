# import git

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)



#
# node=creat_er([5,4,8,11,None,13,4,7,2,None,None,None,1])
# a=Solution()
# print(a.hasPathSum(node,22))