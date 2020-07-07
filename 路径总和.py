class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def fun(root,val):
            if not root:
                return False
            # 判断是否到达叶子节点
            val+=root.val
            if not root.left and not root.right:
                return val==sum
            if(fun(root.left,val)):
                return True
            return fun(root.right,val)
        return fun(root,0)





#
from git import creat_er
node=creat_er([5,4,8,11,None,13,4,7,2,None,None,None,1])
a=Solution()
print(a.hasPathSum(node,22))