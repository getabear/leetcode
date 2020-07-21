from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def fun(l,r):
            if l>r:
                return [None]
            trees=[]
            for i in range(l,r+1):

                left=fun(l,i-1)
                right=fun(i+1,r)
                for j in left:
                    for k in right:
                        tmp = TreeNode(i)
                        tmp.left=j
                        tmp.right=k
                        trees.append(tmp)
            return trees
        return fun(1,n) if n else []