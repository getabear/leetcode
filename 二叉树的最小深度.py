# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root=None
    def add(self,item):
        node=TreeNode(item)
        if self.root==None:
            # print(node.val)
            self.root=node
        else:
            q=[self.root]
            while(True):
                pop_node=q.pop(0)
                # print(pop_node.val)
                if pop_node.left is None:
                    pop_node.left=node
                    return
                elif pop_node.right is None:
                    pop_node.right=node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root.val:
            return 0
        children=[root.left,root.right]
        if not any(children):
            return 1
        res = float('inf')
        for child in children:
            if child:
                res=min(self.minDepth(child),res)
        return res+1

l=[3,9,20,None,None,15,7]
root=Tree()
for i in l :
    root.add(i)

a=Solution()
print(a.minDepth(root.root))
