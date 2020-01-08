from typing import List
from git import er

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #提交通过,击败6.63%的用户,迭代方法下次来
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret=[]
        def fun(root: TreeNode):
            if not root:
                return
            fun(root.left)
            fun(root.right)
            self.ret.append(root.val)
            return

        fun(root)
        return self.ret

b=er()
a=Solution()
nums=[1,None,2,3]
head=b.creat_er(nums)
print(a.postorderTraversal(head))