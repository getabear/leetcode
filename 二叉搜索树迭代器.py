# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        self.push(root)

    def push(self,root):
        while root:
            self.stack.append(root)
            root=root.left
        return

    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmp=self.stack.pop()
        if tmp.right:
            self.push(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not self.stack==[]
