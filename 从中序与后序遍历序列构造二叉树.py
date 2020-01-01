from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def fun(inorder: List[int], postorder: List[int]):
            if not inorder:
                return
            root=TreeNode(postorder[-1])
            index=inorder.index(postorder[-1])
            root.left=fun(inorder[:index],postorder[:index])
            root.right=fun(inorder[index+1:],postorder[index:-1])
            return root
        return fun(inorder,postorder)