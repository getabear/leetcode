from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret=[]
        def fun(root,s):
            #到达叶子节点，记录结果并返回
            if root.left==None and root.right==None:
                ret.append(s+str(root.val))
                return
            tmp=str(root.val)+"->"
            if root.left:
                fun(root.left,s+tmp)
            if root.right:
                fun(root.right,s+tmp)
        if not root:
            return []
        fun(root,"")
        return ret
