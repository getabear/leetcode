from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def fun(preorder: List[int], inorder: List[int]):
            if not preorder:
                return
            root=TreeNode(preorder[0])
            i=inorder.index(preorder[0])             #得到根节点下标
            root.left=fun(preorder[1:i+1],inorder[:i])              #左子树
            root.right=fun(preorder[i+1:],inorder[i+1:])            #右子树
            return root
        return fun(preorder,inorder)

