from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, depth):
            if not root: return
            if depth == len(res):
                res.insert(0, [])
            res[-(depth + 1)].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res

#一层一层遍历,最后反转
class Solution1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret = []
        def fun(root: TreeNode,depth):
            if not root:
                return
            if len(ret)==depth:
                ret.append([])
            ret[depth].append(root.val)
            fun(root.left,depth+1)
            fun(root.right,depth+1)
        fun(root,0)
        ret.reverse()
        return ret

