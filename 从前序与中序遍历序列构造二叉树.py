from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#前序遍历   先根节点  左子树  右子树
#中序遍历   先左子树  根节点  右子树
class Solution1:
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

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def fun(preorder: List[int], inorder: List[int]):
            if len(preorder)==0:
                return None
            root=TreeNode(preorder[0])
            for index,i in enumerate(inorder):
                if i==preorder[0]:
                    break

            root.left=fun(preorder[1:index+1],inorder[:index])
            root.right=fun(preorder[index+1:],inorder[index+1:])
            return root
        return fun(preorder,inorder)



