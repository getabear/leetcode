from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#说明  二叉搜索树的所有左子节点比根节点小,所有右子节点比根节点大
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def fun(start,end):
            if(start>end):
                return [None]
            trees=[]
            for i in range(start,end+1):
                lefttrees=fun(start,i-1)
                righttrees=fun(i+1,end)

                for l in lefttrees:
                    for r in righttrees:
                        currenttree=TreeNode(i)
                        currenttree.left=l
                        currenttree.right=r
                        trees.append(currenttree)

            return trees

        return fun(1,n) if n else []
a=Solution()
print(a.generateTrees(3))